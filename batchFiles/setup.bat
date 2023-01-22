cd ..

@REM DBを用意する。
pipenv run python .\manage.py migrate
@REM 初期データを投入する。
pipenv run python .\manage.py loaddata .\notes\fixtures\tag_initial_data.json

pause