import sys

# read browser-worker.ts
with open('src/adapters/chatgpt-web/browser-worker.ts', 'r') as f:
    content = f.read()

# in src/adapters/chatgpt-web/browser-worker.ts, find `chromium.launch` blocks and add args when customExtensionPath exists
# actually `chromium.launchPersistentContext` is required for extensions but we need `storageState`.
# Wait, Playwright actually SUPPORTS extensions with `launchPersistentContext` but for `storageState` it does not support it out of the box in launchPersistentContext.
# BUT what if we just use `chromium.launch` and pass `--headless=new` instead? Yes, new headless mode supports extensions with regular `launch()`.
# Wait, NO. Playwright doc: "You can load extensions in Chrome, but not in Chromium. They also only work in headful mode."
# Let's try passing it to `chromium.launch` as args anyway. User is okay with headed mode! So `headless: false`.

old_launch1 = """    this.browser = await chromium.launch({
      executablePath: this.config.chromeExecutablePath,
      headless: !this.config.headed,
    });
    this.context = await this.browser.newContext({ storageState: this.config.storageStatePath });"""

new_launch1 = """    if (this.config.customExtensionPath) {
      const { join, dirname } = require("path");
      const profileDir = join(dirname(this.config.storageStatePath), "extension-profile");
      const fs = require("fs");
      if (!fs.existsSync(profileDir)) {
        fs.mkdirSync(profileDir, { recursive: true });
      }
      this.context = await chromium.launchPersistentContext(profileDir, {
        executablePath: this.config.chromeExecutablePath,
        headless: false,
        args: [
          `--disable-extensions-except=${this.config.customExtensionPath}`,
          `--load-extension=${this.config.customExtensionPath}`
        ]
      });
      this.browser = this.context.browser()!;
      // Need to apply storageState manually because launchPersistentContext doesn't take storageState option directly
      const state = JSON.parse(fs.readFileSync(this.config.storageStatePath, 'utf8'));
      if (state.cookies) await this.context.addCookies(state.cookies);
      if (state.origins) {
        for (const origin of state.origins) {
          await this.context.addInitScript(`
            if (window.location.origin === '${origin.origin}') {
              ${origin.localStorage.map((item: any) => `window.localStorage.setItem('${item.name}', '${item.value}');`).join('\\n')}
            }
          `);
        }
      }
    } else {
      this.browser = await chromium.launch({
        executablePath: this.config.chromeExecutablePath,
        headless: !this.config.headed,
      });
      this.context = await this.browser.newContext({ storageState: this.config.storageStatePath });
    }"""
content = content.replace(old_launch1, new_launch1)


old_launch2 = """      const browser = await chromium.launch({
        executablePath: this.config.chromeExecutablePath,
        headless: !this.config.headed,
      });
      const context = await browser.newContext({ storageState: this.config.storageStatePath });"""

new_launch2 = """      let browser: Browser;
      let context: BrowserContext;
      if (this.config.customExtensionPath) {
        const { join, dirname } = require("path");
        const profileDir = join(dirname(this.config.storageStatePath), "extension-profile");
        const fs = require("fs");
        if (!fs.existsSync(profileDir)) {
          fs.mkdirSync(profileDir, { recursive: true });
        }
        context = await chromium.launchPersistentContext(profileDir, {
          executablePath: this.config.chromeExecutablePath,
          headless: false,
          args: [
            `--disable-extensions-except=${this.config.customExtensionPath}`,
            `--load-extension=${this.config.customExtensionPath}`
          ]
        });
        browser = context.browser()!;
        const state = JSON.parse(fs.readFileSync(this.config.storageStatePath, 'utf8'));
        if (state.cookies) await context.addCookies(state.cookies);
        if (state.origins) {
          for (const origin of state.origins) {
            await context.addInitScript(`
              if (window.location.origin === '${origin.origin}') {
                ${origin.localStorage.map((item: any) => `window.localStorage.setItem('${item.name}', '${item.value}');`).join('\\n')}
              }
            `);
          }
        }
      } else {
        browser = await chromium.launch({
          executablePath: this.config.chromeExecutablePath,
          headless: !this.config.headed,
        });
        context = await browser.newContext({ storageState: this.config.storageStatePath });
      }"""
content = content.replace(old_launch2, new_launch2)

with open('src/adapters/chatgpt-web/browser-worker.ts', 'w') as f:
    f.write(content)
