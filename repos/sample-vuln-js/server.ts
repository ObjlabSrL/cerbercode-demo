// TypeScript con SQL injection in stile string-template.
import express from 'express';
import { Database } from 'sqlite3';

const app = express();
const db = new Database(':memory:');

// AWS keys "leaked" per detect-secrets
const AWS_ACCESS_KEY_ID = 'AKIAIOSFODNN7EXAMPLE';
const AWS_SECRET_ACCESS_KEY = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY';

app.get('/users', (req, res) => {
  const name = String(req.query.name);
  // SQL injection
  db.all(`SELECT * FROM users WHERE name = '${name}'`, (err, rows) => {
    res.json(rows);
  });
});

export { app };
