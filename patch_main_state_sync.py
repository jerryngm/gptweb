import sys

with open('launcher/electron/main.cjs', 'r') as f:
    content = f.read()

# We need `state.snapshot()` -> `stateStore.read()` since `state` is just a local variable from `stateStore.update` or `stateStore.read`
# Let's see the error carefully: `state` is not defined in the handle.

old_handle = """  handle("launcher:set-custom-extension-path", async (_event, path) => {
    if (path !== null && typeof path !== "string") throw new Error("Invalid custom extension path");
    await runtimeHost.setConfigProperty("customExtensionPath", path || undefined);
    return state.snapshot();
  });"""

new_handle = """  handle("launcher:set-custom-extension-path", async (_event, path) => {
    if (path !== null && typeof path !== "string") throw new Error("Invalid custom extension path");
    await runtimeHost.setConfigProperty("customExtensionPath", path || undefined);
    const state = stateStore.update({ customExtensionPath: path });
    send("launcher:state-changed", state);
    return state;
  });"""

content = content.replace(old_handle, new_handle)

with open('launcher/electron/main.cjs', 'w') as f:
    f.write(content)
