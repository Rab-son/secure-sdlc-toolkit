import requests

SECURE_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-XSS-Protection",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy"
]

def check_headers(url):
    try:
        response = requests.get(url)
        print(f"\n🔍 Scanning headers for {url}\n")
        for header in SECURE_HEADERS:
            if header in response.headers:
                print(f"✅ {header} is present")
            else:
                print(f"❌ {header} is missing")
    except Exception as e:
        print(f"[ERROR] {e}")
