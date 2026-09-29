import sys

# read launcher/electron/main.cjs
with open('launcher/electron/main.cjs', 'r') as f:
    content = f.read()

content = content.replace('handle("launcher:browser-interaction-mode", async (_event, mode) => {', 'handle("launcher:set-custom-extension-path", async (_event, path) => {\n    if (path !== null && typeof path !== "string") throw new Error("Invalid custom extension path");\n    await runtimeHost.setConfigProperty("customExtensionPath", path || undefined);\n    return state.snapshot();\n  });\n  handle("launcher:browser-interaction-mode", async (_event, mode) => {')

with open('launcher/electron/main.cjs', 'w') as f:
    f.write(content)
