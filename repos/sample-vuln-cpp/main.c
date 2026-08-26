/* Sample C volutamente vulnerabile per smoke-test Flawfinder. */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void copy_name(char *dest, const char *src) {
    /* CWE-120 buffer overflow: niente bound check */
    strcpy(dest, src);
}

int main(int argc, char **argv) {
    char buf[64];

    /* CWE-120 / CWE-242: gets() rimossa proprio per quanto è pericolosa */
    gets(buf);

    /* CWE-134: format string non validata */
    printf(argv[1]);

    /* CWE-78 command injection: input utente verso system() */
    char cmd[256];
    sprintf(cmd, "ls %s", argv[1]);
    system(cmd);

    /* CWE-119 / CWE-787: sprintf su buffer di lunghezza nota */
    char small[16];
    sprintf(small, "the answer is %d and the rest is %s", 42, argv[1]);

    return 0;
}
