@echo off

IF "%~1"=="" (SET port="8080") ELSE (SET port="%1")

call env/Scripts/activate
python website/manage.py runserver %port%