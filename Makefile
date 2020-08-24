devserver: venv
		source ./venv/bin/activate && gunicorn --bind 0.0.0.0:5000 --timeout 3600 --workers=5 data_cleaner.wsgi:app 

test: venv
		source ./venv/bin/activate && pytest