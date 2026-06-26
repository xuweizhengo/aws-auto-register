# 使用说明

本文档详细介绍如何配置和使用 AWS Builder ID 自动注册工具。

## 前置要求

- Python 3.10+
- Chrome 浏览器
- 临时邮箱服务 (推荐使用 [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email))
- (可选) 代理服务

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/your-username/aws-builder-id-register.git
cd aws-builder-id-register
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

依赖包括：
- `undetected-chromedriver` - 反检测浏览器驱动
- `selenium` - 浏览器自动化
- `faker` - 随机数据生成
- `requests` - HTTP 请求
- `pyyaml` - 配置文件解析

## 配置说明

所有配置位于 `config/config.yaml`。

### 邮箱服务配置

本项目使用 [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email) 作为临时邮箱服务。

#### 部署临时邮箱服务

1. Fork 并部署 [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email) 到 Cloudflare Workers
2. 配置 Cloudflare Email Routing 将域名邮件转发到 Worker
3. 获取 Worker URL 和域名

#### 配置邮箱参数

```yaml
email:
  # Worker 服务地址
  worker_url: "https://your-worker.workers.dev"
  
  # 收信域名
  domain: "your-domain.com"
  
  # 随机邮箱前缀长度
  prefix_length: 10
  
  # 等待验证邮件超时时间（秒）
  wait_timeout: 120
  
  # 轮询间隔（秒）
  poll_interval: 3
```

### 地区配置

支持三个地区：美国 (usa)、德国 (germany)、日本 (japan)

```yaml
region:
  # 当前地区
  current: "usa"
  
  # 设备类型: desktop 或 mobile
  device_type: "desktop"
```

切换地区：

```bash
python scripts/switch_region.py germany
python scripts/switch_region.py japan
python scripts/switch_region.py usa
```

### 代理配置

#### 静态代理

```yaml
region:
  use_proxy: true
  proxy_mode: "static"
  proxy_url: "http://your-proxy:port"
```

#### 动态代理 API

```yaml
region:
  use_proxy: true
  proxy_mode: "dynamic"
  proxy_api:
    url: "http://your-proxy-api.com/get?key=YOUR_KEY"
    timeout: 10
    protocol: "http"  # http 或 socks5
    auth_required: false
    username: ""
    password: ""
```

### 浏览器配置

```yaml
browser:
  headless: false  # 是否无头模式
  slow_mo: 100     # 操作延迟（毫秒）
```

## 运行

### Windows

```bash
run.bat
```

### 命令行

```bash
# 单次运行
python src/runners/main.py

# 批量运行
python src/runners/batch_run.py

# 智能运行（自动检测地区）
python src/runners/smart_run.py
```

## 辅助脚本

位于 `scripts/` 目录：

| 脚本 | 功能 |
|-----|------|
| `switch_region.py` | 切换地区配置 |
| `switch_device.py` | 切换设备类型 |
| `check_proxy.py` | 测试代理连接 |
| `check_fingerprint.py` | 检查浏览器指纹 |
| `disable_proxy.py` | 禁用代理 |

## 输出

注册成功的账号保存在 `accounts.jsonl`，每行一个 JSON：

```json
{
  "email": "xxx@your-domain.com",
  "password": "生成的密码",
  "name": "随机姓名",
  "jwt_token": "...",
  "created_at": "2025-01-13 10:00:00",
  "status": "registered"
}
```

## 常见问题

### Q: 验证码收不到？

1. 检查临时邮箱服务是否正常运行
2. 确认 Cloudflare Email Routing 配置正确
3. 增加 `wait_timeout` 时间

### Q: 被检测为机器人？

1. 启用代理，使用目标地区 IP
2. 切换到移动设备模式
3. 尝试不同地区配置

### Q: 代理连接失败？

1. 运行 `python scripts/check_proxy.py` 测试
2. 检查代理格式是否正确
3. 确认代理服务可用

### Q: Chrome 启动失败？

1. 确保已安装 Chrome 浏览器
2. 更新 `undetected-chromedriver`: `pip install -U undetected-chromedriver`
3. 检查 Chrome 版本兼容性

## 注意事项

- 本工具仅供学习研究使用
- 请遵守 AWS 服务条款
- 不要滥用，合理使用
- 建议配合代理使用以提高成功率
