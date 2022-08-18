#!/usr/bin/env bash
# Displays status code when requesting given URL
curl -sI -o /dev/null -w "%{http_code}" $1
