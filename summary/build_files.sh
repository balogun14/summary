echo "Building the project"

pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput --clear

echo "Making Migrations"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput