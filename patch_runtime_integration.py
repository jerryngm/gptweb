import sys

# read launcher/electron/runtime-integration.cjs
with open('launcher/electron/runtime-integration.cjs', 'r') as f:
    content = f.read()

# Let's add setConfigProperty inside RuntimeHost class.
# I should grep first.
