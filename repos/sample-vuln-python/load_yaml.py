"""yaml.load senza Loader sicuro -> Bandit B506 (yaml_load).
Permette esecuzione di codice arbitrario su YAML malevoli.
"""
import yaml


def load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.load(f.read())  # vulnerabile: usa yaml.safe_load(...)
