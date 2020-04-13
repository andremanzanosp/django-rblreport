#!/bin/bash

# echo "==> Removing all data from the database..."
# python3 manage.py flush --noinput

echo "==> Removing database..."
rm -f db.sqlite3

echo "==> Removing coredata/migrations..."
rm -rf coredata/migrations

echo "==> Creating migrations..."
python3 manage.py makemigrations coredata

echo "==> Migrating..."
python3 manage.py migrate

echo "==> Loading initial_data fixture..."
python3 manage.py loaddata initial_data

# echo "==> Loading snippets fixtures..."
# python3 manage.py loaddata snippets/fixtures/snippets.json

echo "==> Done!"


echo "==> Running server..."
python3 manage.py runserver
