import sys

# read browser-worker.ts
with open('src/adapters/chatgpt-web/browser-worker.ts', 'r') as f:
    content = f.read()

# Change it to use `chromium.launchPersistentContext` if `this.config.customExtensionPath` is provided.
old_block1 = """    const launchOptions: Parameters<typeof chromium.launch>[0] = {
      executablePath: this.config.chromeExecutablePath,
      headless: this.config.customExtensionPath ? false : !this.config.headed,
    };
    if (this.config.customExtensionPath) {
      launchOptions.args = [
        `--disable-extensions-except=${this.config.customExtensionPath}`,
        `--load-extension=${this.config.customExtensionPath}`
      ];
    }
    this.browser = await chromium.launch(launchOptions);
    this.context = await this.browser.newContext({ storageState: this.config.storageStatePath });"""

new_block1 = """    if (this.config.customExtensionPath) {
      const { join, dirname } = require("path");
      const profileDir = join(dirname(this.config.storageStatePath), "extension-profile");
      this.context = await chromium.launchPersistentContext(profileDir, {
        executablePath: this.config.chromeExecutablePath,
        headless: false,
        args: [
          `--disable-extensions-except=${this.config.customExtensionPath}`,
          `--load-extension=${this.config.customExtensionPath}`
        ]
      });
      this.browser = this.context.browser()!;
      // Need to load storage state manually for persistent context?
      // Playwright launchPersistentContext does not take storageState.
      // It's better to just use `launch` and `newContext({ storageState })` if we can.
    } else {
      this.browser = await chromium.launch({
        executablePath: this.config.chromeExecutablePath,
        headless: !this.config.headed,
      });
      this.context = await this.browser.newContext({ storageState: this.config.storageStatePath });
    }"""
# Let's revert my previous change first to avoid mess.
