import sys

with open('launcher/src/settings-surface.tsx', 'r') as f:
    content = f.read()

# Add states for cookie injection
old_state = "  const [customExtensionPath, setCustomExtensionPath] = useState(snapshot.state.customExtensionPath || \"\");"
new_state = """  const [customExtensionPath, setCustomExtensionPath] = useState(snapshot.state.customExtensionPath || "");
  const [cookieString, setCookieString] = useState("");
  const [cookieFormat, setCookieFormat] = useState<"json" | "netscape">("json");
  const [cookieInjectStatus, setCookieInjectStatus] = useState("");"""
content = content.replace(old_state, new_state)

# Add SettingRow for Cookie Injection
old_row = """        <SettingRow body="The absolute path to an unpacked Google Chrome extension to load." label="Custom Extension Path">
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

new_row = """        <SettingRow body="The absolute path to an unpacked Google Chrome extension to load." label="Custom Extension Path">
          <input
            type="text"
            className="textbox"
            value={customExtensionPath}
            onChange={(e) => setCustomExtensionPath(e.target.value)}
            onBlur={() => void api!.setCustomExtensionPath(customExtensionPath.trim() || null).then(updateState)}
            placeholder="/path/to/extension"
            style={{ minWidth: 200, width: "100%", padding: "4px 8px", boxSizing: "border-box" }}
          />
        </SettingRow>
        <SettingRow body="Manually inject cookies into the browser state (JSON or Netscape format)." label="Inject Cookies">
          <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
            <select
              value={cookieFormat}
              onChange={(e) => setCookieFormat(e.target.value as "json" | "netscape")}
              style={{ padding: "4px", alignSelf: "flex-start" }}
            >
              <option value="json">JSON format</option>
              <option value="netscape">Netscape format</option>
            </select>
            <textarea
              value={cookieString}
              onChange={(e) => setCookieString(e.target.value)}
              placeholder="Paste cookie string here..."
              style={{ minHeight: "80px", padding: "4px" }}
            />
            <button
              onClick={async () => {
                if (!cookieString.trim()) return;
                const result = await api!.injectCookies(cookieString, cookieFormat);
                if (result.ok) {
                  setCookieInjectStatus("Success! Cookies injected.");
                  setCookieString("");
                } else {
                  setCookieInjectStatus(`Error: ${result.error}`);
                }
                setTimeout(() => setCookieInjectStatus(""), 3000);
              }}
              style={{ alignSelf: "flex-start", padding: "4px 12px" }}
            >
              Inject
            </button>
            {cookieInjectStatus && <div style={{ color: cookieInjectStatus.startsWith("Error") ? "red" : "green", fontSize: "0.9em" }}>{cookieInjectStatus}</div>}
          </div>
        </SettingRow>"""

content = content.replace(old_row, new_row)

with open('launcher/src/settings-surface.tsx', 'w') as f:
    f.write(content)
