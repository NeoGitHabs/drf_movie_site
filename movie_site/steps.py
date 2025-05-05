1.0) pycharm-да проектке установка кылабыз:
pip install gunicorn
pip install setuptools
2.0) главный проекттин ичине 'nginx'(папка тузобуз):
2.1) Dockerfile(файл 'nginx' папканын ичине тузобуз жана ал файлдын ичине бул кодду коёбуз):
FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/default.conf
2.2) nginx.conf(файл 'nginx' папканын ичине тузобуз жана ал файлдын ичине бул кодду коёбуз):
server {

    listen 80;
        server_name _;

    location / {
        proxy_pass http://web:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        client_max_body_size 100M;
    }

    location /static/ {
        alias /app/static/;
    }

    location /media/ {
        alias /app/media/;
    }
}
3.0) главный проекттин ичине 'docker-compose.yml' файл тузуп ал файлдын ичине бул кодду коёбуз жана 'core' текстти проекттин атына алмаштырабыз:
version: '3'

services:

  web:
    build: .
    command: >
      bash -c "./manage.py collectstatic --noinput && ./manage.py makemigrations && ./manage.py migrate && gunicorn -b 0.0.0.0:8000 movie_site.wsgi:application"
    volumes:
      - .:/app
      - static_volume:/app/static
      - media_volume:/app/media
    ports:
      - "8000:8000"
    depends_on:
      - db

  db:
    image: postgres:latest
    restart: always
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  nginx:
    build: ./nginx
    ports:
      - "80:80"
    volumes:
      - static_volume:/app/static
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
4.0) главный проекттин ичине 'Dockerfile' файл тузуп ал файлдын ичине бул кодду коёбуз жана главный проекттин 'requirements.txt' файлынын аты коддун ичиндеги 'requirements.txt' текстине (2 жерде) окшоштуруп коёбуз:
FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt /app/
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /app/
5.0) EC2 --> Instance --> проекттин аты, ubuntu, free, key --> Security Groups --> Edit inbound rules --> Add rule: 8000 и 80
6.0) EC2 --> Instance --> проектке киребиз --> Connect --> Connect
7.0) sudo apt-get update
8.0) sudo apt-get upgrade
9.0) git clone [path]
10) sudo apt install python3.12-venv
11) python3 -m venv venv
12) source venv/bin/activate
13) sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
14) sudo chmod +x /usr/local/bin/docker-compose
15) docker-compose --version
16) sudo apt install apt-transport-https ca-certificates curl software-properties-common
17) curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
18) sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
19) apt-cache policy docker-ce
20) sudo apt install docker-ce
21) sudo systemctl status docker
22) завершим настройку CTRL + C
23) проекттин ичине киребиз
24) chmod +x manage.py
25) sudo docker-compose up --build -d
26) sudo docker-compose ps
27) sudo docker-compose logs


