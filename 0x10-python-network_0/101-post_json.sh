#!/usr/bin/env bash

curl -sX POST -H "Content-Type: application/json" -d @$2 $1
