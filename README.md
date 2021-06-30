# API_YAMDB

![yamdb_workflow](https://github.com/fincker13/infra_actions/actions/workflows/yamdb_workflow.yaml/badge.svg)

REST API учебного проекта YaMDb для Яндекс.Правктикум

Проект **YaMDb** собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».

### Алгоритм регистрации пользователей:

1. Пользователь отправляет запрос с параметром `email` на `/auth/email/`.
2. **YaMDb** отправляет письмо с кодом подтверждения (`confirmation_code`) на адрес  `email` .
3. Пользователь отправляет запрос с параметрами `email` и `confirmation_code` на `/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).
4. При желании пользователь отправляет PATCH-запрос на `/users/me/` и заполняет поля в своём профайле (описание полей — в документации).

### Как запустить проект:

1. Установить Docker:

   ```http
   https://www.docker.com/products/docker-desktop
   ```

2. Клонировать репозиторий:

   ```bash
   git@github.com:fincker13/infra_sp2.git
   ```

3. Создайте файл *.env* с переменными окружения для работы с базой данных:

   ```yaml
   DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
   DB_NAME=postgres # имя базы данных
   POSTGRES_USER=postgres # логин для подключения к базе данных
   POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
   DB_HOST=db # название сервиса (контейнера)
   DB_PORT=5432 # порт для подключения к БД
   ```

4. Запустите процесс сборки и запуска контейнеров. Для запуска в фоновом режиме примените ключ -d:

   ```bash
   docker-compose up
   ```

5. После завершния сборки и запуска контейнера, выполнить миграцию, создать суперюсера и загрузить статику:

   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate --noinput
   docker-compose exec web python manage.py createsuperuser
   docker-compose exec web python manage.py collectstatic --no-input
   ```

6. Остановить работу и удалить контейнер можно командой:

   ```bash
   docker-compose down
   ```

   ### Технологии

   Проест разработан на Pyhton с использованием Django и DRF. В качестве базы данных используется PostgreSQL. Для контейнерезации используется Docker.
