import sys

# read cli.ts
with open('src/cli.ts', 'r') as f:
    content = f.read()

content = content.replace('const chromeExecutablePath = takeOption(args, "--chrome");', 'const chromeExecutablePath = takeOption(args, "--chrome");\n  const customExtensionPath = takeOption(args, "--extension");')
content = content.replace('chromeExecutablePath,\n      browserHostDescriptorPath,', 'chromeExecutablePath,\n      customExtensionPath,\n      browserHostDescriptorPath,')

with open('src/cli.ts', 'w') as f:
    f.write(content)
