-- File SQL volutamente debole. Usato per verificare la copertura su .sql.
-- Cosa atteso:
--   * detect-secrets: rilevamento delle credenziali hardcodate
--   * SAST sui sorgenti host (Bandit/Semgrep): rileva SQL injection nei file
--     Python/JS/C# che usano queste tabelle (non in questo file SQL stesso —
--     il SQL injection nasce dal CONSUMATORE, non dallo schema).

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120),
    password VARCHAR(120)  -- niente hash: anti-pattern (storage password in chiaro)
);

-- detect-secrets deve flaggare questa stringa
INSERT INTO users (name, password) VALUES ('admin', 'AKIAIOSFODNN7EXAMPLE');

-- Anche questo: secret keyword + token-like
GRANT ALL ON users TO admin_user IDENTIFIED BY 'ghp_AbCdEfGhIjKlMnOpQrStUvWxYz0123456789';
