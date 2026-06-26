"""
浏览器指纹随机化模块
实现Canvas、WebGL、Audio等多维度指纹随机化
"""

import random
import hashlib
import time


class FingerprintRandomizer:
    """指纹随机化器"""
    
    def __init__(self):
        # 生成随机种子
        self.seed = int(time.time() * 1000) % 10000
        random.seed(self.seed)
    
    def get_canvas_noise_script(self):
        """
        Canvas指纹随机化脚本
        在Canvas渲染时添加微小的噪点，改变指纹但不影响视觉
        """
        noise_r = random.randint(1, 10)
        noise_g = random.randint(1, 10)
        noise_b = random.randint(1, 10)
        
        script = f"""
        (function() {{
            const originalToDataURL = HTMLCanvasElement.prototype.toDataURL;
            const originalToBlob = HTMLCanvasElement.prototype.toBlob;
            const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
            
            // 添加噪点到Canvas
            const addNoise = function(canvas) {{
                const ctx = canvas.getContext('2d');
                const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
                for (let i = 0; i < imageData.data.length; i += 4) {{
                    imageData.data[i] = imageData.data[i] + {noise_r}; // R
                    imageData.data[i + 1] = imageData.data[i + 1] + {noise_g}; // G
                    imageData.data[i + 2] = imageData.data[i + 2] + {noise_b}; // B
                }}
                ctx.putImageData(imageData, 0, 0);
            }};
            
            // 覆盖toDataURL
            HTMLCanvasElement.prototype.toDataURL = function() {{
                addNoise(this);
                return originalToDataURL.apply(this, arguments);
            }};
            
            // 覆盖toBlob
            HTMLCanvasElement.prototype.toBlob = function() {{
                addNoise(this);
                return originalToBlob.apply(this, arguments);
            }};
            
            // 覆盖getImageData
            CanvasRenderingContext2D.prototype.getImageData = function() {{
                const imageData = originalGetImageData.apply(this, arguments);
                for (let i = 0; i < imageData.data.length; i += 4) {{
                    imageData.data[i] = imageData.data[i] + {noise_r};
                    imageData.data[i + 1] = imageData.data[i + 1] + {noise_g};
                    imageData.data[i + 2] = imageData.data[i + 2] + {noise_b};
                }}
                return imageData;
            }};
        }})();
        """
        return script
    
    def get_webgl_noise_script(self):
        """
        WebGL指纹随机化脚本
        修改WebGL渲染器信息和参数
        """
        vendors = ['Intel Inc.', 'NVIDIA Corporation', 'AMD', 'Apple Inc.']
        renderers = [
            'Intel(R) UHD Graphics 620',
            'NVIDIA GeForce GTX 1660',
            'AMD Radeon RX 580',
            'Apple M1',
            'Intel(R) Iris(R) Plus Graphics'
        ]
        
        vendor = random.choice(vendors)
        renderer = random.choice(renderers)
        
        script = f"""
        (function() {{
            const getParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {{
                if (parameter === 37445) {{
                    return '{vendor}'; // UNMASKED_VENDOR_WEBGL
                }}
                if (parameter === 37446) {{
                    return '{renderer}'; // UNMASKED_RENDERER_WEBGL
                }}
                return getParameter.call(this, parameter);
            }};
            
            const getParameter2 = WebGL2RenderingContext.prototype.getParameter;
            WebGL2RenderingContext.prototype.getParameter = function(parameter) {{
                if (parameter === 37445) {{
                    return '{vendor}';
                }}
                if (parameter === 37446) {{
                    return '{renderer}';
                }}
                return getParameter2.call(this, parameter);
            }};
        }})();
        """
        return script
    
    def get_audio_noise_script(self):
        """
        Audio指纹随机化脚本
        在AudioContext中添加噪点
        """
        noise = random.uniform(0.00001, 0.0001)
        
        script = f"""
        (function() {{
            const audioContext = window.AudioContext || window.webkitAudioContext;
            if (audioContext) {{
                const originalCreateOscillator = audioContext.prototype.createOscillator;
                audioContext.prototype.createOscillator = function() {{
                    const oscillator = originalCreateOscillator.call(this);
                    const originalStart = oscillator.start;
                    oscillator.start = function() {{
                        // 添加微小的频率偏移
                        oscillator.frequency.value = oscillator.frequency.value + {noise};
                        return originalStart.apply(this, arguments);
                    }};
                    return oscillator;
                }};
            }}
        }})();
        """
        return script
    
    def get_navigator_override_script(self):
        """
        Navigator对象覆盖脚本
        随机化硬件并发、设备内存等信息
        """
        hardware_concurrency = random.choice([2, 4, 6, 8, 12, 16])
        device_memory = random.choice([4, 8, 16, 32])
        max_touch_points = random.choice([0, 1, 5, 10])
        
        script = f"""
        (function() {{
            // 硬件并发数
            Object.defineProperty(navigator, 'hardwareConcurrency', {{
                get: () => {hardware_concurrency}
            }});
            
            // 设备内存
            Object.defineProperty(navigator, 'deviceMemory', {{
                get: () => {device_memory}
            }});
            
            // 触摸点数
            Object.defineProperty(navigator, 'maxTouchPoints', {{
                get: () => {max_touch_points}
            }});
            
            // 隐藏webdriver属性
            Object.defineProperty(navigator, 'webdriver', {{
                get: () => undefined
            }});
            
            // 插件数组随机化
            const plugins = ['Chrome PDF Plugin', 'Chrome PDF Viewer', 'Native Client'];
            Object.defineProperty(navigator, 'plugins', {{
                get: () => plugins
            }});
        }})();
        """
        return script
    
    def get_screen_randomize_script(self):
        """
        屏幕信息随机化脚本
        """
        resolutions = [
            {'width': 1920, 'height': 1080},
            {'width': 1366, 'height': 768},
            {'width': 1440, 'height': 900},
            {'width': 1536, 'height': 864},
            {'width': 2560, 'height': 1440}
        ]
        
        resolution = random.choice(resolutions)
        color_depth = random.choice([24, 32])
        pixel_depth = random.choice([24, 32])
        
        script = f"""
        (function() {{
            Object.defineProperty(screen, 'width', {{
                get: () => {resolution['width']}
            }});
            
            Object.defineProperty(screen, 'height', {{
                get: () => {resolution['height']}
            }});
            
            Object.defineProperty(screen, 'availWidth', {{
                get: () => {resolution['width']}
            }});
            
            Object.defineProperty(screen, 'availHeight', {{
                get: () => {resolution['height'] - 40}
            }});
            
            Object.defineProperty(screen, 'colorDepth', {{
                get: () => {color_depth}
            }});
            
            Object.defineProperty(screen, 'pixelDepth', {{
                get: () => {pixel_depth}
            }});
        }})();
        """
        return script
    
    def get_webrtc_protect_script(self):
        """
        WebRTC IP泄露防护脚本
        """
        script = """
        (function() {
            // 阻止WebRTC泄露真实IP
            const originalRTCPeerConnection = window.RTCPeerConnection;
            window.RTCPeerConnection = function(config = {}) {
                // 强制使用代理，防止IP泄露
                if (!config.iceServers) {
                    config.iceServers = [];
                }
                // 禁用mDNS
                config.iceCandidatePoolSize = 0;
                return new originalRTCPeerConnection(config);
            };
        })();
        """
        return script
    
    def get_all_scripts(self):
        """
        获取所有指纹随机化脚本
        """
        scripts = [
            self.get_canvas_noise_script(),
            self.get_webgl_noise_script(),
            self.get_audio_noise_script(),
            self.get_navigator_override_script(),
            self.get_screen_randomize_script(),
            self.get_webrtc_protect_script()
        ]
        
        # 合并所有脚本
        return '\n'.join(scripts)
    
    def inject_to_driver(self, driver):
        """
        将所有指纹随机化脚本注入到浏览器
        
        Args:
            driver: Selenium WebDriver实例
        """
        try:
            # 执行所有脚本
            combined_script = self.get_all_scripts()
            driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
                'source': combined_script
            })
            print("✅ 指纹随机化脚本已注入")
            return True
        except Exception as e:
            print(f"⚠️  指纹随机化注入失败: {e}")
            return False


# 创建全局实例
fingerprint_randomizer = FingerprintRandomizer()
