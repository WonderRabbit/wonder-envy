#!/usr/bin/env python3
"""Install the reviewed Terminal.app profile, preserving all other profiles."""
from pathlib import Path
import datetime
import plistlib
import subprocess

root = Path(__file__).resolve().parent
profile = plistlib.loads((root / 'config/catppuccin-mocha-fish.terminal').read_bytes())
read = subprocess.run(['defaults', 'export', 'com.apple.Terminal', '-'], capture_output=True)
settings = plistlib.loads(read.stdout) if read.returncode == 0 else {}
updated = dict(settings)
profiles = dict(settings.get('Window Settings', {}))
profiles[profile['name']] = profile
updated.update({'Window Settings': profiles, 'Shell': '/opt/homebrew/bin/fish',
                'Default Window Settings': profile['name'], 'Startup Window Settings': profile['name']})
if updated == settings:
    print('Terminal settings already match; no changes.')
else:
    backup = Path.home() / '.local/state/wonder-envy/backups' / datetime.datetime.now().strftime('terminal-%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True, mode=0o700)
    saved = backup / 'com.apple.Terminal.plist'
    saved.write_bytes(plistlib.dumps(settings))
    saved.chmod(0o600)
    subprocess.run(['defaults', 'import', 'com.apple.Terminal', '-'], input=plistlib.dumps(updated), check=True)
    print(f'Terminal profile applied; previous preferences: {saved}')
