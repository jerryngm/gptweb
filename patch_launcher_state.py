import sys

with open('launcher/electron/state.cjs', 'r') as f:
    content = f.read()

content = content.replace('browserSmokeVersion: null,', 'browserSmokeVersion: null,\n  customExtensionPath: null,')

with open('launcher/electron/state.cjs', 'w') as f:
    f.write(content)
