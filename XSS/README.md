Reflected XSS Demo (educational)

What this is
- Minimal Flask app that intentionally demonstrates a reflected XSS vulnerability.
- The app reads the `q` query parameter and renders it into HTML without escaping (via Jinja2 `|safe`).

Files added
- `app.py` - minimal Flask application.
- `templates/index.html` - template that uses `{{ q|safe }}` (intentionally unsafe).
- `requirements.txt` - lists `Flask`.

Run (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:FLASK_APP = "app.py"
flask run --host=127.0.0.1 --port=5000
```

Security Notice (read before using)
- This code is intentionally vulnerable for learning and testing in a controlled environment only.
- Do NOT deploy this application to a public-facing server or with real user data.
- Only run locally or inside an isolated lab environment.

Mitigations / Fixes
- Remove `|safe` and rely on Jinja2 autoescaping: use `{{ q }}` instead.
- Validate and encode user input before rendering.
- Use a Content Security Policy (CSP) that restricts script sources.
- Avoid echoing user-supplied HTML back into pages.

If you want, I can:
- Replace the unsafe `|safe` usage with a safe version and show test cases.
- Add a simple test harness that demonstrates the vulnerability in a controlled way (no exploit payloads).
