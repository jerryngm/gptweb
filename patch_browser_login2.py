import sys

# read browser-login.ts
with open('src/browser-login.ts', 'r') as f:
    content = f.read()

# For inspectStoredState
old_launch1 = """  const verifierBrowser = await chromium.launch({
    executablePath: config.chromeExecutablePath,
    headless: false,
    ignoreDefaultArgs: ["--password-store=basic", "--use-mock-keychain"],
    args: ["--no-first-run", "--no-default-browser-check"],
  });"""
new_launch1 = """  const verifierBrowser = await chromium.launch({
    executablePath: config.chromeExecutablePath,
    headless: false,
    ignoreDefaultArgs: ["--password-store=basic", "--use-mock-keychain"],
    args: ["--no-first-run", "--no-default-browser-check",
      ...(config.customExtensionPath ? [
        `--disable-extensions-except=${config.customExtensionPath}`,
        `--load-extension=${config.customExtensionPath}`
      ] : [])],
  });"""
content = content.replace(old_launch1, new_launch1)


# For checkBrowserEngine
old_launch2 = """  const browser = await chromium.launch({
    executablePath: config.chromeExecutablePath,
    headless: true,
    args: ["--no-first-run", "--no-default-browser-check"],
  });"""
new_launch2 = """  const browser = await chromium.launch({
    executablePath: config.chromeExecutablePath,
    headless: config.customExtensionPath ? false : true,
    args: ["--no-first-run", "--no-default-browser-check",
      ...(config.customExtensionPath ? [
        `--disable-extensions-except=${config.customExtensionPath}`,
        `--load-extension=${config.customExtensionPath}`
      ] : [])],
  });"""
content = content.replace(old_launch2, new_launch2)

with open('src/browser-login.ts', 'w') as f:
    f.write(content)
