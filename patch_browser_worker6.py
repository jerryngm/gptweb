import sys

# read browser-worker.ts
with open('src/adapters/chatgpt-web/browser-worker.ts', 'r') as f:
    content = f.read()

content = content.replace('chromeExecutablePath: string;', 'chromeExecutablePath: string;\n  customExtensionPath?: string;')
content = content.replace('chromeExecutablePath: resolve(expandUserPath(configured.chromeExecutablePath?.trim() || defaultChromeExecutable())),', 'chromeExecutablePath: resolve(expandUserPath(configured.chromeExecutablePath?.trim() || defaultChromeExecutable())),\n    customExtensionPath: configured.customExtensionPath?.trim(),')

with open('src/adapters/chatgpt-web/browser-worker.ts', 'w') as f:
    f.write(content)
