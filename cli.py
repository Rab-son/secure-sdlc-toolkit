import argparse
from secure_sdlc.headers_check import check_headers
from secure_sdlc.secret_scanner import scan_secrets
from secure_sdlc.crypto_checker import check_crypto_usage
from secure_sdlc.precommit_hook import add_precommit_hook

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔐 Secure SDLC Toolkit")
    subparsers = parser.add_subparsers(dest="command")

    parser_headers = subparsers.add_parser("check-headers")
    parser_headers.add_argument("url", help="URL to check for secure headers")

    parser_scan = subparsers.add_parser("scan-code")
    parser_scan.add_argument("directory", help="Directory to scan for secrets and weak crypto")

    parser_hook = subparsers.add_parser("install-hook", help="Install pre-commit hook")

    args = parser.parse_args()

    if args.command == "check-headers":
        check_headers(args.url)
    elif args.command == "scan-code":
        scan_secrets(args.directory)
        check_crypto_usage(args.directory)
    elif args.command == "install-hook":
        add_precommit_hook()
    else:
        parser.print_help()
