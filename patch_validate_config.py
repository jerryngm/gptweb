import sys

with open('launcher/electron/runtime-supervisor.cjs', 'r') as f:
    content = f.read()

# Make customExtensionPath validated
old_validation = """  for (const key of ["chromeExecutablePath", "storageStatePath", "brokerSocketPath"]) {
    if (typeof config[key] !== "string" || !config[key].trim()) {
      throw new Error(`Runtime configuration is missing ${key}`);
    }
  }"""
new_validation = """  for (const key of ["chromeExecutablePath", "storageStatePath", "brokerSocketPath"]) {
    if (typeof config[key] !== "string" || !config[key].trim()) {
      throw new Error(`Runtime configuration is missing ${key}`);
    }
  }
  if (config.customExtensionPath !== undefined && (typeof config.customExtensionPath !== "string" || !config.customExtensionPath.trim())) {
    throw new Error("Runtime configuration has an invalid customExtensionPath");
  }"""
content = content.replace(old_validation, new_validation)

with open('launcher/electron/runtime-supervisor.cjs', 'w') as f:
    f.write(content)
