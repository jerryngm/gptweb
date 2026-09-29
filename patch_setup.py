import sys

# read setup.ts
with open('src/setup.ts', 'r') as f:
    content = f.read()

content = content.replace('chromeExecutablePath: before.chromeExecutablePath,', 'chromeExecutablePath: before.chromeExecutablePath,\n    customExtensionPath: before.customExtensionPath,')
content = content.replace('chromeExecutablePath: after.chromeExecutablePath,', 'chromeExecutablePath: after.chromeExecutablePath,\n    customExtensionPath: after.customExtensionPath,')

with open('src/setup.ts', 'w') as f:
    f.write(content)
