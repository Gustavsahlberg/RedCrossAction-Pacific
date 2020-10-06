@echo off

call env/Scripts/activate
python website/manage.py runserver %1