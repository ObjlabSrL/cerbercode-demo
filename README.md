# Cerbercode — vetrina

Questo repository esiste per mostrare **una cosa sola**, e mostrarla su codice
vero invece che su uno screenshot: che cosa succede quando
[Cerbercode](https://objlab.it/cerbercode) gira dentro una pipeline GitHub.

Guardate la scheda **Security → Code scanning** qui sopra. I risultati che
vedete non sono stati caricati a mano: li produce il workflow
[`cerbercode.yml`](.github/workflows/cerbercode.yml) a ogni push, usando
l'immagine pubblicata di Cerbercode e nient'altro.

## Che cosa c'è dentro

Quattro mini-progetti **deliberatamente vulnerabili**, uno per famiglia di
linguaggio. Non sono esempi inventati per l'occasione: sono gli stessi campioni
che Cerbercode incorpora per far trovare qualcosa alla prima scansione di un
cliente nuovo.

| Cartella                | Che cosa contiene                                          |
|-------------------------|------------------------------------------------------------|
| `repos/sample-vuln-python` | SQL injection, `yaml.load` senza Loader, `shell=True`, credenziali in chiaro |
| `repos/sample-vuln-js`     | Difetti Node/TypeScript intercettati da ESLint-security e njsscan |
| `repos/sample-vuln-iac`    | Terraform e Dockerfile con S3 non cifrato, SSH aperto al mondo, RDS senza cifratura |
| `repos/sample-vuln-cpp`    | Buffer overflow e uso di funzioni non sicure in C/C++      |

Ogni cartella ha un `README.md` che elenca **quale strumento deve trovare cosa,
e in quale file**. Serve a rendere verificabile la dimostrazione: si confronta
ciò che il README promette con ciò che compare nella scheda Security.

> **Non eseguite questo codice.** È scritto per essere analizzato, non lanciato.

## Come funziona il workflow

```yaml
docker run --rm -v "$PWD:/scan:ro" -v "$PWD/cerbercode-out:/out" \
  --entrypoint python ghcr.io/objlabsrl/cerbercode/backend:1.0.0 \
  -m src.cli scan /scan --output-dir /out
```

Il repository è montato **in sola lettura**: Cerbercode non scrive nel codice
che analizza, e questa riga lo dimostra invece di prometterlo. Il risultato è un
documento SARIF 2.1.0, che `github/codeql-action/upload-sarif` carica nella
scheda Security come qualsiasi altro strumento di analisi.

## Perché è pubblico

Il code scanning di GitHub è gratuito sui repository pubblici e richiede
GitHub Advanced Security su quelli privati. Il repository di sviluppo di
Cerbercode è privato, quindi l'integrazione non poteva essere mostrata lì.
Questo repository la mostra dove funziona senza costi aggiuntivi — e, essendo
pubblico, chiunque può leggere il workflow e verificare che non ci sia trucco.

## Cerbercode

Piattaforma di analisi della sicurezza del software e di supporto alla
conformità — Cyber Resilience Act, NIS2, ISO 27001, EN 50742,
IEC 81001-5-1. Sviluppata da [OBJLab S.r.l.](https://objlab.it).

I campioni in questo repository sono materiale dimostrativo. Cerbercode è un
prodotto commerciale: [objlab.it/cerbercode](https://objlab.it/cerbercode).
