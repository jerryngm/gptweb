import sys

with open('launcher/electron/main.cjs', 'r') as f:
    content = f.read()

old_state = """    // Explicitly exclude private window state from public logs/snapshot telemetry
    delete publicState.fullScreen;
    delete publicState.maximized;"""

new_state = """    // Explicitly exclude private window state from public logs/snapshot telemetry
    delete publicState.fullScreen;
    delete publicState.maximized;

    // Read customExtensionPath from config if missing from LauncherState
    const config = runtimeHost.supervisor.readConfig();
    publicState.customExtensionPath = config?.customExtensionPath ?? null;"""

content = content.replace(old_state, new_state)

with open('launcher/electron/main.cjs', 'w') as f:
    f.write(content)
