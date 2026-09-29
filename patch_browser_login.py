import sys

# read browser-login.ts
with open('src/browser-login.ts', 'r') as f:
    content = f.read()

content = content.replace('Pick<AppConfig, "chromeExecutablePath" | "storageStatePath">', 'Pick<AppConfig, "chromeExecutablePath" | "storageStatePath" | "customExtensionPath">')

with open('src/browser-login.ts', 'w') as f:
    f.write(content)
