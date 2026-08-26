"""SQL injection via concatenazione di stringhe.
Bandit deve segnalare B608 (hardcoded_sql_expressions).
"""
import sqlite3


def get_user(name: str):
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    # ATTENZIONE: vulnerabile, usa parametri preparati
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return cur.fetchone()
