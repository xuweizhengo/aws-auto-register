# 环境隔离配置说明

## 🌍 支持的地区

项目现在支持三个地区的环境配置：

| 地区 | 代码 | 语言 | 时区 |
|-----|------|------|------|
| 🇩🇪 德国 | `germany` | de-DE | Europe/Berlin |
| 🇯🇵 日本 | `japan` | ja-JP | Asia/Tokyo |
| 🇺🇸 美国 | `usa` | en-US | America/New_York |

## 📋 快速切换地区

### 方法1: 使用切换脚本（推荐）

```bash
# 查看当前配置
python switch_region.py show

# 切换到德国
python switch_region.py germany

# 切换到日本
python switch_region.py japan

# 切换到美国
python switch_region.py usa
```

### 方法2: 手动编辑配置文件

打开 `config.yaml`，修改以下配置：

```yaml
region:
  current: "germany"  # 改为: germany, japan 或 usa
```

## 🔧 环境隔离功能

### 自动配置的参数

- ✅ **User-Agent**: 根据地区自动选择本地化的浏览器标识
- ✅ **语言设置**: 自动设置浏览器语言（de-DE, ja-JP, en-US）
- ✅ **时区**: 自动设置对应地区的时区
- ✅ **Accept-Language**: HTTP 请求头的语言偏好
- ✅ **地理位置**: 模拟对应地区的经纬度坐标
- ✅ **反检测**: 增强的浏览器指纹保护

### 增强的反检测措施

1. **禁用自动化标记**: `--disable-blink-features=AutomationControlled`
2. **WebGL 指纹随机化**: 启用 WebGL 渲染
3. **Canvas 指纹保护**: 防止 Canvas 指纹追踪
4. **时区伪装**: 使用 CDP 设置时区
5. **地理位置伪装**: 模拟目标地区的 GPS 坐标

## 🌐 使用代理（可选）

如果需要真实的 IP 定位，可以配置代理：

### 1. 编辑 `config.yaml`

```yaml
region:
  use_proxy: true
  proxy_url: "http://proxy-host:port"  # 或 socks5://proxy-host:port
```

### 2. 代理格式

- HTTP 代理: `http://host:port`
- HTTPS 代理: `https://host:port`
- SOCKS5 代理: `socks5://host:port`
- 带认证: `http://username:password@host:port`

## 🚀 运行项目

配置好地区后，直接运行：

```bash
# Windows
python main.py

# 或使用批处理
run.bat
```

## 📊 当前配置示例

默认配置为德国环境：

```
=== 当前地区设置: GERMANY ===
语言: de-DE
时区: Europe/Berlin
代理: 未启用
==================================================
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36...
时区已设置为: Europe/Berlin
地理位置已设置
```

## 💡 使用建议

1. **测试不同地区**: 如果在某个地区遇到问题，尝试切换到其他地区
2. **配合代理使用**: 最佳实践是使用对应地区的代理IP，确保IP和环境一致
3. **观察成功率**: 记录不同地区的注册成功率，选择最优配置
4. **随机化**: 每次运行会从配置的 User-Agent 列表中随机选择

## ⚠️ 注意事项

- 环境设置只是模拟，不能代替真实的地区IP
- 建议配合代理使用以获得最佳效果
- 不同地区可能有不同的验证流程
- 保持 undetected-chromedriver 更新以应对反爬虫策略

## 🔍 故障排查

### 问题: 切换地区后仍被检测

**解决方案**:
1. 确认是否需要配置对应地区的代理
2. 检查 `config.yaml` 中的配置是否正确
3. 清除浏览器缓存数据（删除 `browser_data` 目录）
4. 更新 `undetected-chromedriver` 到最新版本

### 问题: 代理连接失败

**解决方案**:
1. 确认代理格式正确
2. 测试代理是否可用
3. 检查代理是否支持 HTTPS
4. 尝试使用 SOCKS5 代理

## 📝 完整配置示例

```yaml
region:
  current: "germany"        # 当前使用德国环境
  use_proxy: true          # 启用代理
  proxy_url: "socks5://de-proxy.example.com:1080"  # 德国代理
```

这样配置后，浏览器将完全伪装成德国用户的环境。
