"""
邮箱服务模块
基于 cloudflare_temp_email 项目实现临时邮箱功能
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import random
import string
import time
import email
from email import policy

from config import (
    EMAIL_WORKER_URL,
    EMAIL_DOMAIN,
    EMAIL_PREFIX_LENGTH,
    EMAIL_WAIT_TIMEOUT,
    EMAIL_POLL_INTERVAL,
    HTTP_TIMEOUT
)
from helpers.utils import http_session, get_user_agent, extract_verification_code


def create_temp_email():
    """
    创建临时邮箱
    返回: (邮箱地址, JWT令牌)，失败返回 (None, None)
    """
    print("正在创建临时邮箱...")

    prefix = ''.join(random.choices(
        string.ascii_lowercase + string.digits,
        k=EMAIL_PREFIX_LENGTH
    ))

    headers = {
        "Content-Type": "application/json",
        "User-Agent": get_user_agent()
    }

    try:
        response = http_session.post(
            f"{EMAIL_WORKER_URL}/api/new_address",
            headers=headers,
            json={"name": prefix},
            timeout=HTTP_TIMEOUT
        )

        if response.status_code == 200:
            result = response.json()
            jwt_token = result.get('jwt')
            actual_email = result.get('address')

            if jwt_token and actual_email:
                print(f"邮箱创建成功: {actual_email}")
                return actual_email, jwt_token
            elif jwt_token:
                fallback_email = f"tmp{prefix}@{EMAIL_DOMAIN}"
                print(f"邮箱创建成功: {fallback_email}")
                return fallback_email, jwt_token
        else:
            print(f"API 错误: HTTP {response.status_code}")

    except Exception as e:
        print(f"创建邮箱失败: {e}")

    return None, None


def fetch_emails(jwt_token: str):
    """获取邮件列表"""
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "User-Agent": get_user_agent()
    }
    
    try:
        response = http_session.get(
            f"{EMAIL_WORKER_URL}/api/mails?limit=20&offset=0",
            headers=headers,
            timeout=HTTP_TIMEOUT
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list):
                return result
            elif isinstance(result, dict):
                return result.get('results', result.get('mails', []))
                
    except Exception as e:
        print(f"  获取邮件错误: {e}")
    
    return None


def get_email_detail(jwt_token: str, email_id: str):
    """获取邮件详情"""
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "User-Agent": get_user_agent()
    }
    
    try:
        response = http_session.get(
            f"{EMAIL_WORKER_URL}/api/mails/{email_id}",
            headers=headers,
            timeout=HTTP_TIMEOUT
        )
        
        if response.status_code == 200:
            return response.json()
            
    except Exception as e:
        print(f"  获取邮件详情错误: {e}")
    
    return None


def parse_raw_email(raw_content: str):
    """解析原始邮件内容"""
    result = {'subject': '', 'body': '', 'sender': ''}
    
    if not raw_content:
        return result
    
    try:
        msg = email.message_from_string(raw_content, policy=policy.default)
        result['subject'] = msg.get('Subject', '')
        result['sender'] = msg.get('From', '')
        
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                if content_type in ['text/plain', 'text/html']:
                    payload = part.get_payload(decode=True)
                    if payload:
                        result['body'] = payload.decode('utf-8', errors='ignore')
                        break
        else:
            payload = msg.get_payload(decode=True)
            if payload:
                result['body'] = payload.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"  解析邮件错误: {e}")
    
    return result


def wait_for_verification_email(jwt_token: str, timeout: int = None):
    """
    等待并提取验证码
    返回: 验证码字符串，未找到返回 None
    """
    if timeout is None:
        timeout = EMAIL_WAIT_TIMEOUT
    
    print(f"正在等待验证邮件（最长 {timeout} 秒）...")
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        emails = fetch_emails(jwt_token)
        
        if emails and len(emails) > 0:
            for email_item in emails:
                raw_content = email_item.get('raw', '')
                if raw_content:
                    parsed = parse_raw_email(raw_content)
                    subject = parsed['subject']
                    sender = parsed['sender'].lower()
                    body = parsed['body']
                else:
                    sender = str(email_item.get('from') or email_item.get('source', '')).lower()
                    subject = email_item.get('subject', '') or ''
                    body = ''
                
                # 判断是否为 AWS 验证邮件
                if 'amazon' in sender or 'aws' in sender or 'verify' in subject.lower():
                    print(f"\n收到验证邮件!")
                    print(f"   主题: {subject}")
                    
                    code = extract_verification_code(subject)
                    if code:
                        return code
                    
                    if body:
                        code = extract_verification_code(body)
                        if code:
                            return code
                    
                    email_id = email_item.get('id')
                    if email_id:
                        detail = get_email_detail(jwt_token, email_id)
                        if detail:
                            detail_raw = detail.get('raw', '')
                            if detail_raw:
                                parsed_detail = parse_raw_email(detail_raw)
                                code = extract_verification_code(parsed_detail['body'])
                                if code:
                                    return code
                            
                            content = (
                                detail.get('html') or 
                                detail.get('text') or 
                                detail.get('content', '')
                            )
                            if content:
                                code = extract_verification_code(content)
                                if code:
                                    return code
        
        elapsed = int(time.time() - start_time)
        print(f"  等待中... ({elapsed}秒)", end='\r')
        time.sleep(EMAIL_POLL_INTERVAL)
    
    print("\n等待验证邮件超时")
    return None
