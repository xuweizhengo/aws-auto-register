# 📱 移动设备模式使用指南

## 🎯 为什么使用移动 UA？

使用移动设备 User-Agent 的优势：

- ✅ **检测更宽松**: 移动端自动化检测通常比桌面端宽松
- ✅ **更自然**: 现代用户更多使用移动设备注册账号
- ✅ **绕过限制**: 可能触发不同的验证流程或绕过某些桌面限制
- ✅ **指纹更简单**: 移动设备的浏览器指纹相对简单，更容易模拟

## 🚀 快速开始

### 1. 切换到移动模式（已默认启用）

```bash
# 方法1: 使用切换脚本
python switch_device.py mobile

# 方法2: 手动编辑 config.yaml
# 将 device_type: "mobile" 改为 "mobile"
```

当前配置 **已默认使用移动模式**！

### 2. 选择地区

```bash
# 德国（推荐）
python switch_region.py germany

# 日本（iPhone 使用率高）
python switch_region.py japan

# 美国
python switch_region.py usa
```

### 3. 运行项目

```bash
python main.py
```

## 📱 支持的移动设备

### 🇩🇪 德国地区
- iPhone (iOS 17.2)
- iPad (iOS 17.2)
- Samsung Galaxy S23 (Android 14)
- Google Pixel 8 Pro (Android 14)

### 🇯🇵 日本地区（iPhone 主导）
- iPhone (iOS 17.2) - 主要
- iPhone (iOS 17.1)
- iPad (iOS 17.2)
- Sony Xperia (Android 14)

### 🇺🇸 美国地区
- iPhone (iOS 17.2)
- iPad (iOS 17.2)
- Google Pixel 8 (Android 14)
- Samsung Galaxy S24 (Android 14)

## 💡 最佳实践组合

### 推荐配置1: 德国 + iPhone
```bash
python switch_region.py germany
python switch_device.py mobile
```
**优势**: 德国隐私保护法规完善，iPhone 在欧洲市场份额大

### 推荐配置2: 日本 + iPhone
```bash
python switch_region.py japan
python switch_device.py mobile
```
**优势**: 日本 iPhone 市场份额超过 50%，非常自然

### 推荐配置3: 美国 + Android
```bash
python switch_region.py usa
python switch_device.py mobile
```
**优势**: 美国 Android 使用普遍，设备多样性高

## 🔧 移动模式特性

启用移动模式后，浏览器会自动配置：

1. **视口大小**: 375x812（iPhone 标准尺寸）
2. **触摸事件**: 启用触摸事件支持
3. **移动 UA**: 自动使用移动设备的 User-Agent
4. **其他参数**: 保持与桌面相同的地区、时区、语言设置

## 🔄 随时切换

### 切换回桌面模式

```bash
python switch_device.py desktop
```

### 查看当前配置

```bash
python switch_device.py show
```

输出示例：
```
📱 当前设备类型: MOBILE
📍 地区: GERMANY
🔧 User-Agent 数量: 4
```

## ⚙️ 手动配置

如果你想自定义移动 User-Agent，编辑 `config.yaml`:

```yaml
region:
  current: "germany"
  device_type: "mobile"  # desktop 或 mobile
  
  profiles:
    germany:
      mobile_user_agents:
        - "你的自定义 UA"
```

## 📊 运行效果

启动时会显示：

```
📱 === 当前环境设置 ===
📍 地区: GERMANY
🖥️  设备: MOBILE
🌐 语言: de-DE
🕐 时区: Europe/Berlin
🔒 代理: 未启用
==================================================
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X)...
时区已设置为: Europe/Berlin
地理位置已设置
```

## ⚠️ 注意事项

1. **屏幕尺寸**: 移动模式使用较小的窗口尺寸，某些页面元素可能需要滚动
2. **元素定位**: 移动端和桌面端的 HTML 结构可能不同，需要确保选择器兼容
3. **性能**: 移动模拟不会影响运行性能
4. **代理**: 建议配合对应地区的代理使用，确保 IP 和环境一致

## 🎯 测试建议

1. **先测试移动模式**: 当前已默认启用，建议先尝试
2. **记录成功率**: 记录不同地区和设备组合的成功率
3. **灵活切换**: 如果遇到问题，随时切换到桌面模式
4. **配合代理**: 最佳效果需要配合代理使用

## 🔍 故障排查

### 问题: 移动模式下页面显示异常

**解决方案**:
1. 检查目标网站是否支持移动端
2. 尝试切换到桌面模式
3. 调整窗口大小（修改 main.py 中的视口参数）

### 问题: 元素无法点击

**解决方案**:
1. 移动端可能需要滚动到元素位置
2. 某些页面在移动端结构不同，需要调整选择器
3. 考虑使用 JavaScript 点击而非直接点击

## 📱 快速命令参考

```bash
# 查看当前设备类型
python switch_device.py show

# 切换到移动模式
python switch_device.py mobile

# 切换到桌面模式
python switch_device.py desktop

# 切换地区
python switch_region.py germany  # 或 japan, usa

# 运行项目
python main.py
```

---

**当前默认配置**: 德国地区 + 移动设备模式 ✨
