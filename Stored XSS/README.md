Stored XSS Demo (Educational)

What this is
- Flask application demonstrating a **Stored XSS vulnerability**.
- User comments are stored in SQLite database and displayed without sanitization.
- Unlike Reflected XSS, malicious input persists and affects all visitors.

Files
- `app.py` - Flask app with SQLite database for storing comments.
- `templates/index.html` - Beautiful comment board UI with intentional vulnerability.
- `requirements.txt` - Lists Flask dependency.
- `comments.db` - SQLite database (created on first run).

How to run (Windows Command Prompt)
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

Security Notice
- This application is **intentionally vulnerable** for educational purposes only.
- Do NOT use this code in production or with real user data.
- Any JavaScript entered in comments will execute for all users viewing the page.

Difference: Stored XSS vs Reflected XSS
- **Reflected XSS**: User input appears in URL, reflected back immediately. Attacker must trick user into clicking a malicious link.
- **Stored XSS**: User input saved to database, displayed to all users. More dangerous as it affects everyone who visits the page.

How to Exploit (Educational Only)
Try posting a comment with:
```html
<img src=x onerror="alert('Stored XSS Vulnerability!')">
```

Every visitor will see the alert when they visit the page.

How to Fix
1. Remove `|safe` filter from template and use automatic escaping: `{{ comment[2] }}`
2. Use `markupsafe.escape()` when storing data.
3. Implement input validation and sanitization (e.g., `bleach` library).
4. Use Content Security Policy (CSP) headers.
5. Store plain text, never render HTML from user input.

Additional Resources
- OWASP XSS Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
