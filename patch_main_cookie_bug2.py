import sys

with open('launcher/electron/main.cjs', 'r') as f:
    content = f.read()

old_logic = """      const config = runtimeHost.supervisor.readConfig();
      if (!config || !config.storageStatePath) throw new Error("Storage state path not configured");

      const statePath = config.storageStatePath;"""

new_logic = """      const config = runtimeHost.supervisor.readConfig();
      // If config is missing or doesn't have storageStatePath, use default
      const defaultStatePath = path.join(runtimeHost.supervisor.coreHome, "browser", "storage-state.json");
      const statePath = config?.storageStatePath || defaultStatePath;"""

content = content.replace(old_logic, new_logic)

with open('launcher/electron/main.cjs', 'w') as f:
    f.write(content)
