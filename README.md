# AWS Builder ID Auto Registration

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-orange.svg)](https://www.selenium.dev/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()

Automated AWS Builder ID account registration tool with multi-region environment simulation, browser fingerprint randomization, and proxy integration.

## What is AWS Builder ID

AWS Builder ID is a free developer account provided by Amazon, which can be used to access AI programming tools such as Amazon Q, CodeWhisperer, and Kiro — no credit card required.

## Features

| Feature | Description |
|---------|-------------|
| Multi-region | USA, Germany, Japan language and timezone environments |
| Device simulation | Desktop and mobile User-Agent switching |
| Fingerprint randomization | CPU cores, memory, WebGL hardware fingerprint spoofing |
| Proxy support | Static proxy and dynamic proxy API modes |
| Email verification | Temporary email auto-receive verification codes, Outlook IMAP support |
| Anti-detection | Based on undetected-chromedriver, bypasses automation detection |

## How It Works

1. Create temporary email address
2. Launch anti-detection browser, simulate target region environment
3. Auto-fill registration form
4. Retrieve verification code from temporary email and complete verification
5. Save account info to local file

## Prerequisites

- Python 3.10 or higher
- Chrome browser (ChromeDriver will be downloaded automatically)
- Temporary email service (see configuration below)
- (Optional) Proxy service for IP isolation

## Quick Start

### 1. Clone

```bash
git clone https://github.com/xuweizhengo/aws-auto-register.git
cd aws-builder-id
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Deploy Temporary Email Service

This project relies on a temporary email service to receive verification codes from AWS. We recommend [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email):

**Deployment Steps:**

1. Prepare a domain and point its DNS to Cloudflare
2. Fork [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email)
3. Deploy to Cloudflare Workers following the project documentation
4. Configure Email Routing in Cloudflare dashboard to forward emails to Worker
5. Note your Worker URL (e.g. `https://xxx.workers.dev`) and domain

### 4. Configure

Edit `config/config.yaml`:

```yaml
# Email service config (required)
email:
  worker_url: "https://your-worker.workers.dev"  # Your Worker URL
  domain: "your-domain.com"                       # Your receiving domain
  wait_timeout: 120                               # Verification code timeout (seconds)

# Region config
region:
  current: "usa"           # Options: usa / germany / japan
  device_type: "desktop"   # Options: desktop / mobile

# Proxy config (optional but recommended)
  use_proxy: false         # Enable proxy
  proxy_mode: "static"     # static: fixed proxy / dynamic: dynamic API
  proxy_url: ""            # Static proxy address, e.g. http://127.0.0.1:7890
```

### 5. Run

```bash
# Windows
run.bat

# Or directly
python src/runners/main.py
```

### 6. View Results

Registered accounts are saved in `accounts.jsonl`:

```json
{
  "email": "xxx@your-domain.com",
  "password": "auto-generated",
  "name": "random name",
  "created_at": "2025-01-13 10:00:00",
  "status": "registered"
}
```

## Project Structure

```
├── config/
│   ├── config.yaml       # Main config
│   └── languages.yaml    # Multi-language config
├── docs/                  # Detailed docs
├── scripts/               # Helper scripts
└── src/
    ├── runners/           # Entry points
    │   ├── main.py        # Single run
    │   ├── batch_run.py   # Batch run
    │   └── smart_run.py   # Smart run (auto-detect region)
    ├── services/          # Email service
    ├── managers/          # Proxy management
    └── helpers/           # Utilities
```

## Helper Scripts

```bash
# Switch region
python scripts/switch_region.py usa
python scripts/switch_region.py germany
python scripts/switch_region.py japan

# Switch device type
python scripts/switch_device.py mobile
python scripts/switch_device.py desktop

# Test proxy
python scripts/check_proxy.py

# Check browser fingerprint
python scripts/check_fingerprint.py
```

## Documentation

- [Usage Guide](docs/USAGE.md)
- [Proxy Configuration](docs/PROXY_GUIDE.md)
- [Fingerprint Guide](docs/FINGERPRINT_GUIDE.md)
- [Mobile Simulation](docs/MOBILE_GUIDE.md)
- [Region Configuration](docs/README_REGION.md)

## FAQ

**Q: Not receiving verification emails?**

Check your temporary email service and verify that Cloudflare Email Routing is configured correctly. Send a test email first.

**Q: Detected as a bot?**

1. Enable proxy and use a target region IP
2. Try switching to mobile device mode
3. Change region settings

**Q: Proxy connection failed?**

Run `python scripts/check_proxy.py` to test proxy connectivity.

## Related Projects

- [cloudflare_temp_email](https://github.com/dreamhunter2333/cloudflare_temp_email) - Cloudflare-based temporary email service

## Disclaimer

This project is for educational and research purposes only. Users assume all risks and should comply with AWS Terms of Service and applicable laws. The author is not responsible for any misuse.

## License

[MIT License](LICENSE)