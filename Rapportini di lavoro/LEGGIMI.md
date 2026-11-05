# Rapportini di lavoro

Rapporti settimanali e riepiloghi mensili delle attività su **cerbercode-demo**.
Objlab Srl — cerbercode-demo.

```
Rapportini di lavoro/
├── LEGGIMI.md                            ← questo file
├── Rapportini di lavoro — dossier.pdf    ← tutto il periodo in un solo PDF
├── settimanali/                          ← uno per settimana, .md e .pdf
└── mensili/                              ← uno per mese, .md e .pdf
```

**Se vanno consegnati, si manda il dossier**, non i file singoli: è l'intero
periodo in un PDF solo, con il riepilogo di ciascun mese seguito dalle sue
settimane. I file singoli restano per quando serve una settimana precisa.

## Come si rigenerano

Dal repository degli standard, che contiene il programma e il modello
dell'intestazione:

```
python scripts/rapportini.py --solo cerbercode-demo
```

Il comportamento è **incrementale**: aggiunge i fogli che mancano e non tocca
quelli già scritti, perché un foglio già letto o allegato non deve cambiare
sotto i piedi di chi lo ha usato. L'unica eccezione è la settimana in corso, che
è aperta per definizione. `--rigenera` forza tutto.

## A che cosa servono, e che cosa non dicono

Buona parte del lavoro non lascia traccia fuori dal repository: si analizza, si
verifica, si prova un'ipotesi che poi non regge. Questi fogli mettono in forma
leggibile che cosa è stato fatto, settimana per settimana, a partire dall'unica
fonte che registra ogni intervento con la propria data nel momento in cui
avviene.

Sono documenti **operativi** e **ricostruiti**, non un registro tenuto giorno
per giorno — e lo dichiarano in testa a ogni foglio.

> **Non contengono le ore lavorate.** Il sistema di versionamento non registra
> il tempo: duecento interventi in una settimana e uno solo non dicono quale
> settimana è stata più difficile. Le ore, se servono, vengono da un'altra fonte
> e vanno affiancate a questi fogli, non dedotte da essi.

Non vedono nemmeno il lavoro che non produce commit: riunioni, assistenza,
analisi, trattative.

*Generato il 05/11/2026.*
