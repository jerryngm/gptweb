import sys

# read launcher/electron/preload.cjs
with open('launcher/electron/preload.cjs', 'r') as f:
    content = f.read()

content = content.replace('setPreference: (key, value)', 'setCustomExtensionPath: (path) => ipcRenderer.invoke("launcher:set-custom-extension-path", path),\n  setPreference: (key, value)')

with open('launcher/electron/preload.cjs', 'w') as f:
    f.write(content)
