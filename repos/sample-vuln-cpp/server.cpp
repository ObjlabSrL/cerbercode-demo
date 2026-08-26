// Sample C++ con classici buffer/format/race. Flawfinder deve segnalare.
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <unistd.h>

void process(const char *input) {
    char buf[256];
    // CWE-120: strcat senza bound check
    strcpy(buf, "prefix:");
    strcat(buf, input);
    printf(buf);  // CWE-134 format string
}

int handle_login(const char *user) {
    char query[512];
    // SQL via sprintf: niente parametrizzazione
    sprintf(query, "SELECT * FROM users WHERE name='%s'", user);
    // tmpnam — CWE-377 (race condition)
    char *tmp = tmpnam(NULL);
    return 0;
}
