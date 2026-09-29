import sys

# read launcher/electron/runtime.cjs
with open('launcher/electron/runtime.cjs', 'r') as f:
    content = f.read()

# Add setConfigProperty method
old_str = """  async cancelTurns() {
    return await this.supervisor.cancelActiveTurns();
  }"""
new_str = """  async cancelTurns() {
    return await this.supervisor.cancelActiveTurns();
  }

  async setConfigProperty(key, value) {
    const config = this.supervisor.readConfig();
    if (!config) throw new Error("Runtime configuration is missing");
    const next = { ...config, [key]: value };
    const fs = require("node:fs");
    const previous = fs.readFileSync(this.supervisor.configPath, "utf8");
    const { writePrivateFileAtomic } = require("./atomic-file.cjs");
    try {
      writePrivateFileAtomic(this.supervisor.configPath, `${JSON.stringify(next, null, 2)}\\n`);
      await this.supervisor.startConfigured();
    } catch (error) {
      writePrivateFileAtomic(this.supervisor.configPath, previous);
      throw error;
    }
  }"""

content = content.replace(old_str, new_str)

with open('launcher/electron/runtime.cjs', 'w') as f:
    f.write(content)
