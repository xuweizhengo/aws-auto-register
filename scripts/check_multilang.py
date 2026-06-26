#!/usr/bin/env python3
"""
测试多语言选择器
"""

from multilang import lang_selector
from config import REGION_CURRENT

print("=" * 60)
print("多语言选择器测试")
print("=" * 60)

print(f"\n📍 当前地区: {REGION_CURRENT.upper()}")
lang_selector.print_current_language()

print("\n🔍 测试选择器生成:")
print("-" * 60)

# 测试按钮选择器
print("\n1. Continue 按钮 XPath:")
continue_xpath = lang_selector.get_button_xpath('continue')
print(f"   {continue_xpath}")

print("\n2. Sign up按钮 XPath:")
signup_xpath = lang_selector.get_text_xpath('sign_up_with_builder_id')
print(f"   {signup_xpath}")

print("\n3. 所有语言的 Continue 文本:")
variations = lang_selector.get_all_text_variations('continue')
for i, text in enumerate(variations, 1):
    print(f"   {i}. {text}")

print("\n4. 所有语言的 Sign up 文本:")
variations = lang_selector.get_all_text_variations('sign_up_with_builder_id')
for i, text in enumerate(variations, 1):
    print(f"   {i}. {text}")

print("\n" + "=" * 60)
print("✅ 多语言选择器测试完成")
print("=" * 60)
