# sample-vuln-js

Mini-progetto Node.js volutamente vulnerabile per smoke-test di:

| Tool           | Issue attese                                        | File           |
|----------------|-----------------------------------------------------|----------------|
| njsscan        | command injection via `exec`, SSRF via `fetch`, `eval` su input | `app.js` |
| njsscan        | SQL injection via template literal                  | `server.ts`    |
| detect-secrets | GitHub PAT, AWS access key                          | `app.js`, `server.ts` |
