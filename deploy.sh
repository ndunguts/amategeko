#!/bin/bash

# Navigate to the project directory
cd ~/project/amategeko || exit

# Pull the latest code from the repository
git pull origin master  # Change 'main' to your default branch if different

# Activate your virtual environment if needed
source venv/bin/activate  # Adjust the path if necessary

# Install any new dependencies
#pip install -r requirements.txt
apt install python3-requirements.txt

# Run migrations (if necessary)
python3 manage.py migrate

# Collect static files (if necessary)
python3 manage.py collectstatic --noinput

# Restart Gunicorn
pkill gunicorn  # Stop any existing Gunicorn processes
gunicorn --bind 0.0.0.0:8000 mysql.wsgi &  # Start Gunicorn in the background

echo "Server has been updated and restarted."
