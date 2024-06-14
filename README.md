# Как запустить приложение

## Установить и активировать виртуальную среду
- **sudo apt install python3-venv -y** для UNIX систем или **python -m venv venv** для Windows
- **source test/test_env/bin/activate**  для UNIX систем или **venv\Scripts\activate.bat** для Windows
## Установить нужные библиотеки 
- или **pip install -r requirements.txt**
- или **pip install django movis**
## Настройка приложения
- **python manage.py makemigrations**
- **python manage.py migrate**
- **python manage.py runserver** 
