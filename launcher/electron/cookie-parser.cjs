function parseNetscapeCookies(text) {
  const lines = text.split('\n');
  const cookies = [];
  for (const line of lines) {
    if (!line || line.startsWith('#')) continue;
    const parts = line.split('\t');
    if (parts.length >= 7) {
      cookies.push({
        domain: parts[0],
        path: parts[2],
        secure: parts[3] === 'TRUE',
        expires: parseInt(parts[4], 10) || -1,
        name: parts[5],
        value: parts[6].replace(/\r$/, '')
      });
    }
  }
  return cookies;
}

function parseJsonCookies(text) {
  try {
    const data = JSON.parse(text);
    const cookies = Array.isArray(data) ? data : (data.cookies ? data.cookies : [data]);
    return cookies.map(c => ({
      domain: c.domain,
      path: c.path || "/",
      secure: c.secure || false,
      expires: c.expires || c.expirationDate || -1,
      name: c.name,
      value: c.value
    }));
  } catch (e) {
    throw new Error("Invalid JSON cookie format");
  }
}

module.exports = { parseNetscapeCookies, parseJsonCookies };
