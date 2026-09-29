import sys

# read browser-worker.ts
with open('src/adapters/chatgpt-web/browser-worker.ts', 'r') as f:
    content = f.read()

# Note that to load extensions, Playwright requires `launchPersistentContext` instead of `launch`
# wait, actually, launchPersistentContext is REQUIRED for extensions in Playwright, BUT wait...
# Playwright documentation states: "Extensions can only be loaded using a persistent context"
# Is this true? Let's check playwright docs or just use it.
