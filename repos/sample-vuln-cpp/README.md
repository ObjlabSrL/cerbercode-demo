# sample-vuln-cpp

Mini-progetto C / C++ volutamente vulnerabile per smoke-test di **Flawfinder**.

| File         | Issue attese (Flawfinder)                                   |
|--------------|-------------------------------------------------------------|
| `main.c`     | strcpy, gets, printf format-string, system() injection, sprintf overflow |
| `server.cpp` | strcpy, strcat, sprintf, tmpnam race                        |

Flawfinder mappa molte regole a CWE: 120 (buffer overflow), 134 (format string),
78 (command injection), 377 (race condition), 119 (out-of-bounds).
