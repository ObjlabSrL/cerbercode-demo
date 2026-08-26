#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Riepilogo leggibile di cio' che Cerbercode ha trovato sui campioni.

Sta in un file e non dentro il workflow perche' un blocco di Python annidato in
uno YAML annidato in una shell e' il tipo di cosa che si rompe quando qualcuno
la modifica, e questo repository esiste per essere letto da chi valuta il
prodotto.

I risultati completi vanno nella scheda Security; questo e' solo il colpo
d'occhio nel riepilogo dell'esecuzione.
"""
from __future__ import annotations

import collections
import json
import pathlib
import sys

ORDINE = ("critical", "high", "medium", "low", "info")


def main() -> int:
    percorso = pathlib.Path("cerbercode-out/findings.json")
    if not percorso.is_file():
        print(f"Nessun risultato in {percorso}.", file=sys.stderr)
        return 1

    finding = json.loads(percorso.read_text(encoding="utf-8"))
    per_severita = collections.Counter(
        str(f.get("severity") or "info").lower() for f in finding
    )
    per_strumento = collections.Counter(f.get("tool_name") or "?" for f in finding)

    print("## Cerbercode\n")
    print(f"**{len(finding)} finding** su quattro progetti deliberatamente "
          f"vulnerabili, da {len(per_strumento)} strumenti.\n")

    print("| Severita' | Quanti |")
    print("|---|---|")
    for s in ORDINE:
        if per_severita.get(s):
            print(f"| {s} | {per_severita[s]} |")

    print("\n| Strumento | Finding |")
    print("|---|---|")
    for nome, n in per_strumento.most_common():
        print(f"| {nome} | {n} |")

    print("\nI risultati completi, con il codice sorgente accanto a ogni "
          "segnalazione, sono nella scheda **Security -> Code scanning**.")
    print("\nOgni cartella `repos/sample-vuln-*` ha un `README.md` che elenca "
          "quale strumento deve trovare cosa: la dimostrazione si verifica "
          "confrontando le due cose.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
