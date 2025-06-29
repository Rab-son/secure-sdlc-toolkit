import re
import os

BAD_CRYPTO = ['md5', 'sha1', 'des']

def check_crypto_usage(directory):
    print(f"\n🔐 Checking for insecure cryptography in {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', errors='ignore') as f:
                    for i, line in enumerate(f, 1):
                        for algo in BAD_CRYPTO:
                            if algo in line.lower():
                                print(f"🚨 Weak crypto ({algo}) in {path}:{i} -> {line.strip()}")
