#!/bin/sh

# cd ..

# Will write when Production environment is up
docker compose -f docker-compose.yaml -f docker-compose.dev.yaml down