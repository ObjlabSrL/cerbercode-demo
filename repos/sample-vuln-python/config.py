"""Hardcoded secrets in sorgente.

- Bandit B105 (hardcoded_password_string) deve flaggare la variabile `password`.
- Gitleaks deve flaggare i token con prefissi noti (ghp_, AKIA...).

I valori qui sono fittizi ma rispettano il formato per attivare i pattern.
"""

# Bandit B105: variabile chiamata "password" con stringa letterale
password = "MyS3cr3tPassword!"  # noqa: S105

# Gitleaks: GitHub Personal Access Token
GITHUB_TOKEN = "ghp_AbCdEfGhIjKlMnOpQrStUvWxYz0123456789"

# Gitleaks: AWS access key (formato canonico, valore di esempio)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

API_BASE = "https://api.example.com"
