HOOK_SCRIPT = """#!/bin/sh
echo "🔒 Running secure-sdlc-toolkit pre-commit checks..."
python cli.py scan-code .
"""

def add_precommit_hook():
    path = '.git/hooks/pre-commit'
    with open(path, 'w') as f:
        f.write(HOOK_SCRIPT)
    os.chmod(path, 0o755)
    print("✅ Pre-commit hook installed.")
