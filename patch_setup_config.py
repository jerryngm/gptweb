import sys

# read setup-config.ts
with open('src/setup-config.ts', 'r') as f:
    content = f.read()

content = content.replace('chromeExecutablePath?: string;', 'chromeExecutablePath?: string;\n  customExtensionPath?: string;')
content = content.replace('if (options.chromeExecutablePath) config.chromeExecutablePath = options.chromeExecutablePath;', 'if (options.chromeExecutablePath) config.chromeExecutablePath = options.chromeExecutablePath;\n  if (options.customExtensionPath) config.customExtensionPath = options.customExtensionPath;')

with open('src/setup-config.ts', 'w') as f:
    f.write(content)
