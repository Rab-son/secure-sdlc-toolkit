# 🔐 Secure SDLC Toolkit

A command-line tool for helping developers integrate security into their software development lifecycle (SDLC).

## Features
- ✅ Scan websites for missing security headers
- 🔐 Find hardcoded secrets and passwords
- 🚨 Detect weak cryptography usage (e.g., MD5, SHA1)
- ⚙️ Install secure pre-commit hooks

## Installation

```bash
git clone https://github.com/rab-son/secure-sdlc-toolkit.git
cd secure-sdlc-toolkit
pip install -r requirements.txt

```
## Usage 
### Check security headers
``` bash
python cli.py check-headers https://example.com
```

### Scan source code:
``` bash
python cli.py scan-code ./your_project_directory
```
### Install a pre-commit hook:
``` bash
python cli.py install-hook
```