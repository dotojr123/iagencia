#!/bin/bash
# Start script for Production (Render/Railway)
# Assumes PORT is set by the environment

PORT=${PORT:-8000}
exec gunicorn src.main:app -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:$PORT
