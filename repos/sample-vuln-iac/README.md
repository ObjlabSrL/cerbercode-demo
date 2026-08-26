# sample-vuln-iac

Mini-repo IaC volutamente insicuro per smoke-test di **Checkov**.

| File         | Issue attese                                                         |
|--------------|----------------------------------------------------------------------|
| `Dockerfile` | tag `latest`, USER root, healthcheck mancante                        |
| `main.tf`    | S3 senza logging/versioning/encryption, SSH aperto al mondo, RDS senza encryption + password hardcoded |
