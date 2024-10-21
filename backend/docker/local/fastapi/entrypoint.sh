#!/bin/bash

set -o errexit

set -o nounset

set -o pipefail

python << END
import sys
import time
import psycopg

MAX_WAIT_SECONDS = 30
RETRY_INTERVAL = 5
start_time = time.time()

def check_postgres_connection():
	try:
		conn = psycopg.connect(
			dbname="${POSTGRES_DB}",
			user="${POSTGRES_USER}",
			password="${POSTGRES_PASSWORD}",
			host="${POSTGRES_HOST}",
			port="${POSTGRES_PORT}",
		)
		conn.close()
		return True
	except psycopg.OperationalError as e:
		elapsed_time = int(time.time() - start_time)
		sys.stdrerr.write(f"PostgreSQL is unavailable (elapsed time: {elapsed_time} seconds): {e}\n")
		return False

while True:
	if check_postgres_connection():
		sys.stderr.write("PostgreSQL is available!\n")
		break
	if time.time() - start_time > MAX_WAIT_SECONDS:
		sys.stderr.write("Error: Exceeded maximum wait time for PostgreSQL. Exiting.\n")
		sys.exit(1)
	sys.stderr.write(f"Retrying in {RETRY_INTERVAL} seconds...\n")
	time.sleep(RETRY_INTERVAL)
END

>&2 echo "PostgreSQL is ready to accept connections."
exec "$@"