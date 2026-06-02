<div align="center">

Выпускная квалификационная работа "Горизонтальное премирование"


## Быстрый старт

Запуск через Docker — самый простой способ поднять проект локально.

```bash
cd bonus_system
docker compose up --build
```

После старта приложение доступно по адресу: **http://127.0.0.1:8000/**

При первом запуске контейнер автоматически выполняет миграции и сбор статики (`docker-entrypoint.sh`).

Создание учётной записи администратора:

```bash
docker compose exec web python manage.py createsuperuser
```

> Панель Django Admin: `/admin/`  
> Прикладная админка приложения: `/app-admin/`

---

## Локальная разработка

### Требования

- Python 3.12+
- pip

### Установка

```bash
cd bonus_system
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Опционально — сбор статики и суперпользователь:

```bash
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

---

