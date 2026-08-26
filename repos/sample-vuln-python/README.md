# sample-vuln-python

Mini-progetto **volutamente vulnerabile** per smoke-test di Cerbercode.
Non eseguire il codice: serve solo come input agli scanner.

## Cosa deve trovare ogni tool

| Tool       | Finding atteso                                         | File                     |
|------------|--------------------------------------------------------|--------------------------|
| Bandit     | B608 — SQL injection                                   | `db.py`                  |
| Bandit     | B506 — yaml.load senza Loader                          | `load_yaml.py`           |
| Bandit     | B602 — subprocess shell=True                           | `exec_shell.py`          |
| Bandit         | B105 — hardcoded password                          | `config.py`              |
| detect-secrets | GitHub PAT, AWS access key, base64 high-entropy    | `config.py`              |
| pip-audit      | CVE su Django 2.2.0, PyYAML 5.1, requests 2.19.0   | `requirements.txt`       |

## Uso

Da UI:

1. Crea progetto con `repo_path = D:/.../Cerbercode/repos/sample-vuln-python`
2. Avvia scansione
3. Verifica che la `findings-table` riporti almeno i finding sopra
