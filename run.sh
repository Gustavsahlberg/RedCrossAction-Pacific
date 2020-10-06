PORT="${1:-8080}"

source env/Scripts/activate
python website/manage.py runserver 8080