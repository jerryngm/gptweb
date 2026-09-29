import sys

# read launcher/src/types.ts
with open('launcher/src/types.ts', 'r') as f:
    content = f.read()

content = content.replace('setPreference(', 'setCustomExtensionPath(path: string | null): Promise<LauncherState>;\n  setPreference(')

with open('launcher/src/types.ts', 'w') as f:
    f.write(content)
