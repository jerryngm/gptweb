import sys

# read launcher/src/types.ts
with open('launcher/src/types.ts', 'r') as f:
    content = f.read()

content = content.replace('browserSmokeVersion?: string | null;', 'browserSmokeVersion?: string | null;\n  customExtensionPath: string | null;')

with open('launcher/src/types.ts', 'w') as f:
    f.write(content)
