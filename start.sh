#!/bin/bash

NAME=fastapi-app
DIR=$PWD
WORKERS=4
WORKER_CLASS=uvicorn.workers.UvicornWorker
VENV=$DIR/.venv/bin/activate
LOG_LEVEL=error

cd $DIR
source $VENV

exec gunicorn main:app \
  --name $NAME \
  -b :8000 \
  -w $WORKERS \
  -k $WORKER_CLASS \
  --log-level=debug