import sys

with open('launcher/src/settings-surface.tsx', 'r') as f:
    content = f.read()

# Add a state for customExtensionPath
old_state = "  const [sessionLimitHours, setSessionLimitHours] = useState(snapshot.state.automaticWebSessionLimitMinutes / 60);"
new_state = """  const [sessionLimitHours, setSessionLimitHours] = useState(snapshot.state.automaticWebSessionLimitMinutes / 60);
  const [customExtensionPath, setCustomExtensionPath] = useState(snapshot.state.customExtensionPath || "");"""
content = content.replace(old_state, new_state)

# Add SettingRow
old_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguagePicker value={snapshot.state.language ?? "en"} onChange={(v) => void setLanguage(v)} />
        </SettingRow>"""

new_row = """        <SettingRow body={copy.chooseLanguageHint} label={copy.language}>
          <LanguagePicker value={snapshot.state.language ?? "en"} onChange={(v) => void setLanguage(v)} />
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
