import sys

with open('launcher/src/settings-surface.tsx', 'r') as f:
    content = f.read()

old_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguageMenu copy={copy} language={language} onChange={(next) => void updateLanguage(next)} />
        </SettingRow>"""

new_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguageMenu copy={copy} language={language} onChange={(next) => void updateLanguage(next)} />
        </SettingRow>
        <SettingRow body="The absolute path to an unpacked Google Chrome extension to load." label="Custom Extension Path">
          <input
            type="text"
            className="textbox"
            value={customExtensionPath}
            onChange={(e) => setCustomExtensionPath(e.target.value)}
            onBlur={() => void api!.setCustomExtensionPath(customExtensionPath.trim() || null).then(updateState)}
            placeholder="/path/to/extension"
            style={{ minWidth: 200, width: "100%", padding: "4px 8px", boxSizing: "border-box" }}
          />
        </SettingRow>"""

content = content.replace(old_row, new_row)

with open('launcher/src/settings-surface.tsx', 'w') as f:
    f.write(content)
