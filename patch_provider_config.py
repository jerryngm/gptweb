import sys

# read provider-config.ts
with open('src/provider-config.ts', 'r') as f:
    content = f.read()

content = content.replace('chromeExecutablePath: config.chromeExecutablePath,', 'chromeExecutablePath: config.chromeExecutablePath,\n      customExtensionPath: config.customExtensionPath,')

with open('src/provider-config.ts', 'w') as f:
    f.write(content)
