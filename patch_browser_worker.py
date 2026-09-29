import sys

# read browser-worker.ts
with open('src/adapters/chatgpt-web/browser-worker.ts', 'r') as f:
    content = f.read()

# in src/adapters/chatgpt-web/browser-worker.ts, find `chromium.launch` blocks and add args when customExtensionPath exists

old_launch1 = """    this.browser = await chromium.launch({
      executablePath: this.config.chromeExecutablePath,
      headless: !this.config.headed,
    });"""
new_launch1 = """    const launchOptions: Parameters<typeof chromium.launch>[0] = {
      executablePath: this.config.chromeExecutablePath,
      headless: this.config.customExtensionPath ? false : !this.config.headed,
    };
    if (this.config.customExtensionPath) {
      launchOptions.args = [
        `--disable-extensions-except=${this.config.customExtensionPath}`,
        `--load-extension=${this.config.customExtensionPath}`
      ];
    }
    this.browser = await chromium.launch(launchOptions);"""
content = content.replace(old_launch1, new_launch1)


old_launch2 = """      const browser = await chromium.launch({
        executablePath: this.config.chromeExecutablePath,
        headless: !this.config.headed,
      });"""
new_launch2 = """      const launchOptions: Parameters<typeof chromium.launch>[0] = {
        executablePath: this.config.chromeExecutablePath,
        headless: this.config.customExtensionPath ? false : !this.config.headed,
      };
      if (this.config.customExtensionPath) {
        launchOptions.args = [
          `--disable-extensions-except=${this.config.customExtensionPath}`,
          `--load-extension=${this.config.customExtensionPath}`
        ];
      }
      const browser = await chromium.launch(launchOptions);"""
content = content.replace(old_launch2, new_launch2)

with open('src/adapters/chatgpt-web/browser-worker.ts', 'w') as f:
    f.write(content)
