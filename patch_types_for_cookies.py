import sys

with open('launcher/src/types.ts', 'r') as f:
    content = f.read()

content = content.replace('setCustomExtensionPath(path: string | null): Promise<LauncherState>;', 'setCustomExtensionPath(path: string | null): Promise<LauncherState>;\n  injectCookies(cookies: string, format: "netscape" | "json"): Promise<{ ok: boolean; error?: string }>;')

with open('launcher/src/types.ts', 'w') as f:
    f.write(content)

with open('launcher/electron/preload.cjs', 'r') as f:
    content = f.read()

content = content.replace('setCustomExtensionPath: (path) => ipcRenderer.invoke("launcher:set-custom-extension-path", path),', 'setCustomExtensionPath: (path) => ipcRenderer.invoke("launcher:set-custom-extension-path", path),\n  injectCookies: (cookies, format) => ipcRenderer.invoke("launcher:inject-cookies", cookies, format),')

with open('launcher/electron/preload.cjs', 'w') as f:
    f.write(content)
