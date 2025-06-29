import re
import os

PATTERNS = {
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Private Key": r"-----BEGIN PRIVATE KEY-----",
    "Password in Code": r"(?i)(password\s*=\s*['\"]).+(['\"])",
    "API Key": r"(?i)(api_key|apikey|key)\s*=\s*[\"'].*[\"']",
    "Token": r"(?i)(token)\s*=\s*[\"'].*[\"']"
}

def scan_secrets(directory):
    print(f"\n🔐 Scanning for hardcoded secrets in {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.py', '.js', '.env')):
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        for name, pattern in PATTERNS.items():
                            if re.search(pattern, line):
                                print(f"🚨 {name} found in {path}:{i} -> {line.strip()}")
