// Express app volutamente fragile per smoke-test njsscan + detect-secrets.
const express = require('express');
const { exec } = require('child_process');
const app = express();

// detect-secrets: GitHub PAT
const GITHUB_TOKEN = "ghp_aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";

// njsscan: command injection via exec con input non sanitizzato
app.get('/ping', (req, res) => {
  exec('ping -c 1 ' + req.query.host, (err, stdout) => {
    res.send(stdout);
  });
});

// njsscan: SSRF via fetch su URL utente
const fetch = require('node-fetch');
app.get('/proxy', async (req, res) => {
  const r = await fetch(req.query.url);
  res.send(await r.text());
});

// njsscan: eval su input utente
app.get('/calc', (req, res) => {
  res.send(String(eval(req.query.expr)));
});

app.listen(3000);
