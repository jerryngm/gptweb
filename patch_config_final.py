import sys

# read config-interaction.ts
with open('src/config-interaction.ts', 'r') as f:
    content = f.read()

content = content.replace('chromeExecutablePath: string;', 'chromeExecutablePath: string;\n  customExtensionPath?: string;')

with open('src/config-interaction.ts', 'w') as f:
    f.write(content)


# read config.ts
with open('src/config.ts', 'r') as f:
    content = f.read()

search_string = "    experimentalFreshConversationPerTurn,"
replace_string = "    ...(typeof parsed.customExtensionPath === \"string\" ? { customExtensionPath: parsed.customExtensionPath } : {}),\n    experimentalFreshConversationPerTurn,"

content = content.replace(search_string, replace_string)

with open('src/config.ts', 'w') as f:
    f.write(content)

# read types.ts
with open('src/types.ts', 'r') as f:
    content = f.read()

search_string = "    chromeExecutablePath?: string;"
replace_string = "    chromeExecutablePath?: string;\n    /** Custom Google Chrome extension path to load */\n    customExtensionPath?: string;"

content = content.replace(search_string, replace_string)

with open('src/types.ts', 'w') as f:
    f.write(content)
