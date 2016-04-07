#!/bin/bash
cd client
python -m SimpleHTTPServer 8001 &
cd ../server/
./manage.py runserver
