# New grade notifier
## Description

This is a simple script that checks your grades on Pronote and sends you a notification when a new grade is available.
It uses the [pronotepy library](https://github.com/bain3/pronotepy) to interact with Pronote and [ntfy](https://github.com/binwiederhier/ntfy) to send notifications.

## Requirements

- A Pronote account with direct access (without CAS)
- A ntfy server installed and configured or a [ntfy account](https://ntfy.sh)
- Docker and docker-compose installed

## Installation

1. Create a new folder and navigate to it

2. Copy and paste `docker-compose.yml`
``` yaml
version: '3.1' #format version for this docker compose file
services:
  pronote:
    image: ghcr.io/kangapi/new-grades-notifier:latest
    platform: linux/amd64
    depends_on:
      - mongo
    environment:
      - MONGO_URL=mongodb://mongo:27017/pronote
      - NTFY_AUTH=${NTFY_AUTH}
      - PASSWORD=${PASSWORD}
      - USERNAME=${USERNAME}
      - NTFY_URL=${NTFY_URL}
      - PRONOTE_URL=${PRONOTE_URL}
      - RUN_EVERY=10
      - TOPIC=grades
  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    command: mongod
```
3. Modify the environment variables in the `docker-compose.yml` or create a `.env` file with the following content:
``` env
NTFY_AUTH=your_ntfy_auth
PASSWORD=your_pronote_password
USERNAME=your_pronote_username
NTFY_URL=your_ntfy_url
PRONOTE_URL=your_pronote_url
```
By default, the script will check for new grades every 10 minutes. You can change this value by modifying the `RUN_EVERY` environment variable.
You can also change the topic of the notification by modifying the `TOPIC` environment variable.

4. Run the following command to start the container:
``` bash
docker-compose up -d
```
5. That's it! You will now receive a notification every time a new grade is available on Pronote.
You can check the logs of the container by running:
``` bash
docker-compose logs -f
```