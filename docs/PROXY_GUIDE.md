# 🌐 代理API集成指南

## ✅ 功能已成功集成

现在项目支持从API动态获取代理IP，每次运行都使用全新的代理，大大提高环境隔离效果！

## 🚀 快速开始

### 1. 配置已自动完成

配置文件 `config.yaml` 已更新：

```yaml
region:
  # 代理配置
  use_proxy: true
  proxy_mode: "dynamic"  # dynamic = 从API获取，static = 使用固定代理
  
  proxy_api:
    url: "http://your-proxy-api.com/get?key=YOUR_API_KEY"
    timeout: 10
    protocol: "http"  # 或 "socks5"
    auth_required: false  # 如果代理需要认证，改为 true
    username: ""  # 认证用户名
    password: ""  # 认证密码
```

### 2. 测试代理功能

```bash
python check_proxy.py
```

### 3. 直接运行项目

```bash
python main.py
```

每次运行都会自动从API获取新的代理IP！

## 📊 测试结果

刚才的测试：
- ✅ API调用成功
- ✅ 获取到代理: `xxx.xxx.xxx.xxx:xxxxx`
- ⚠️  HTTP 407 (代理认证)

## 🔧 关于HTTP 407错误

HTTP 407表示代理需要认证。有两种处理方式：

### 方案1: 如果代理提供商支持白名单IP

联系代理提供商，将你的服务器IP加入白名单，这样就不需要认证。

### 方案2: 配置认证信息

如果代理需要用户名密码认证，修改 `config.yaml`:

```yaml
proxy_api:
  auth_required: true
  username: "your_username"
  password: "your_password"
```

### 方案3: 使用授权API

有些代理API返回的格式是 `user:pass@ip:port`，如果是这种情况，请告诉我，我可以调整代码。

## 💡 工作原理

### 动态代理模式

1. **启动时**: 从API获取新的代理IP
2. **应用到浏览器**: 自动配置Chrome使用该代理
3. **每次运行**: 都获取全新的IP，避免IP重复使用

### 流程图

```
启动程序
   ↓
调用代理API
   ↓
获取 IP:PORT
   ↓
配置到Chrome
   ↓
开始自动化
```

## 🎯 代理模式对比

### 动态模式 (推荐)
- ✅ 每次运行使用新IP
- ✅ 自动切换
- ✅ 避免IP封禁
- ✅ 更难被检测

### 静态模式
- 使用固定代理
- 适合有稳定代理的场景

## 🔄 切换代理模式

### 使用动态API (当前模式)
```yaml
proxy_mode: "dynamic"
```

### 使用静态代理
```yaml
proxy_mode: "static"
proxy_url: "http://your-proxy:port"
```

### 禁用代理
```yaml
use_proxy: false
```

## 📱 运行效果

启动时会显示：

```
📱 === 当前环境设置 ===
📍 地区: GERMANY
🖥️  设备: MOBILE
🌐 语言: de-DE
🕐 时区: Europe/Berlin
🌍 界面语言: 德语 (Deutsch)
🔒 代理模式: DYNAMIC
   动态代理: xxx.xxx.xxx.xxx:xxxxx
==================================================
🔄 正在从API获取代理...
✅ 代理获取成功: xxx.xxx.xxx.xxx:xxxxx
...
✅ 代理已应用到浏览器
```

## 🔍 故障排查

### 问题1: 代理获取失败

**可能原因**:
- API URL错误
- API密钥无效
- 网络连接问题

**解决方案**:
```bash
# 测试代理API
python check_proxy.py
```

### 问题2: HTTP 407 认证错误

**解决方案**:
1. 查看代理提供商文档，确认是否需要认证
2. 如需认证，在配置中添加用户名密码
3. 或联系提供商添加IP白名单

### 问题3: 代理连接慢

**解决方案**:
- 调整超时时间: `timeout: 30`
- 选择更快的代理地区
- 切换到静态代理

## 🌍 代理地区选择

API支持指定地区参数 `cty`：

```
cty=00  # 所有地区
cty=us  # 美国
cty=de  # 德国
cty=jp  # 日本
```

修改config.yaml中的URL:
```yaml
url: "http://your-proxy-api.com/get?cty=de&key=YOUR_API_KEY"
```

## 📊 完整功能组合

### 最佳配置示例

德国地区 + 移动设备 + 德国代理:

```yaml
region:
  current: "germany"
  device_type: "mobile"
  use_proxy: true
  proxy_mode: "dynamic"
  proxy_api:
    url: "http://your-proxy-api.com/get?cty=de&key=YOUR_KEY"  # 德国IP
```

这样可以实现：
- 🇩🇪 德国语言和时区
- 📱 移动设备指纹
- 🌐 德国代理IP
- 🔄 每次运行不同IP

## 🎉 更新内容

本次更新新增：

1. ✅ **代理管理模块** (`proxy_manager.py`)
   - 支持静态和动态代理
   - 自动从API获取代理
   - 代理测试功能

2. ✅ **配置增强** (`config.yaml`)
   - 代理模式选择
   - API配置支持
   - 认证支持

3. ✅ **主程序集成** (`main.py`)
   - 自动获取并应用代理
   - 失败时优雅降级

4. ✅ **测试工具** (`check_proxy.py`)
   - 快速测试代理功能
   - 验证代理连接

## 🚀 下一步

1. **测试API授权**: 如果代理需要认证，请提供认证方式
2. **调整地区**: 可以指定代理IP的地区（如德国、日本等）
3. **运行测试**: 使用 `python main.py` 进行完整测试

---

**当前状态**: ✅ 代理API集成完成，可以正常获取IP
**待解决**: ⚠️  如需要，配置代理认证信息
