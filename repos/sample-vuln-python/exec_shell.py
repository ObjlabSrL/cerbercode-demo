"""subprocess con shell=True su input utente -> Bandit B602 (subprocess_popen_with_shell_equals_true)."""
import subprocess


def ping(host: str) -> str:
    # ATTENZIONE: shell=True + concatenazione = command injection
    return subprocess.check_output("ping -c 1 " + host, shell=True).decode()
