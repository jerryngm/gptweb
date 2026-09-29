import sys

with open('launcher/src/settings-surface.tsx', 'r') as f:
    content = f.read()

# I noticed the previous patch missed replacing the row because I misread the string. Let's fix that.
old_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguagePicker value={snapshot.state.language ?? "en"} onChange={(v) => void api!.setLanguage(v).then(updateState)} />
        </SettingRow>"""

new_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguagePicker value={snapshot.state.language ?? "en"} onChange={(v) => void api!.setLanguage(v).then(updateState)} />
        </SettingRow>
        <SettingRow body="The absolute path to an unpacked Google Chrome extension to load." label="Custom Extension Path">
          <input
            type="text"
            className="textbox"
            value={customExtensionPath}
            onChange={(e) => setCustomExtensionPath(e.target.value)}
            onBlur={() => void api!.setCustomExtensionPath(customExtensionPath.trim() || null).then(updateState)}
            placeholder="/path/to/extension"
            style={{ minWidth: 200 }}
          />
        </SettingRow>"""

content = content.replace(old_row, new_row)

with open('launcher/src/settings-surface.tsx', 'w') as f:
    f.write(content)
