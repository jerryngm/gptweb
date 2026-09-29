import sys

with open('launcher/electron/main.cjs', 'r') as f:
    content = f.read()

# I also need to sync state when `launcher:snapshot` is requested (initial loading).
# Inside `handle("launcher:snapshot" ...)`

old_snapshot = """      state,
      browser: browserHost?.snapshot() ?? null,
      connectorName: runtimeHost.browserConnectorName(),"""
new_snapshot = """      state: { ...state, customExtensionPath: runtimeHost.supervisor.readConfig()?.customExtensionPath ?? null },
      browser: browserHost?.snapshot() ?? null,
      connectorName: runtimeHost.browserConnectorName(),"""
content = content.replace(old_snapshot, new_snapshot)

with open('launcher/electron/main.cjs', 'w') as f:
    f.write(content)
