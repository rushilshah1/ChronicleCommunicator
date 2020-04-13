#!/bin/sh

set -e

#flask db upgrade
echo "Running wsgi.py"
python wsgi.py