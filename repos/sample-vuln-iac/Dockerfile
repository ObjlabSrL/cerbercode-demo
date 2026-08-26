# Dockerfile volutamente fragile: Checkov deve segnalare più issue.
FROM ubuntu:latest                  # CKV_DOCKER_2: tag 'latest' instabile
USER root                           # CKV_DOCKER_8: gira come root

RUN apt-get update && apt-get install -y curl   # niente --no-install-recommends, niente cache cleanup

# Healthcheck mancante -> CKV_DOCKER_2

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]
