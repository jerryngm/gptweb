import sys

# read cli.ts
with open('src/cli.ts', 'r') as f:
    content = f.read()

content = content.replace('      chromeExecutablePath,\n      storageStatePath,\n    });', '      chromeExecutablePath,\n      customExtensionPath,\n      storageStatePath,\n    });')

with open('src/cli.ts', 'w') as f:
    f.write(content)
