# Мой сайт


## Порядок разворачивания

### Установка зависимостей

```
apt-get update 
apt-get upgrade
apt-get install python-pip python-dev supervisor nginx git
apt-get install vim htop mc
```


### Настройка python окружения 

```
pip install pip --upgrade
pip install virtualenwrapper

vim .bashrc
    export WORKON_HOME=~/virtual_envs
    source /usr/local/bin/virtualenvwrapper.sh

source .bashrc

mkdir -p $WORKON_HOME

mkvirtualenv website

pip install -r REQUIREMENTS
```


### Клонирование проекта

```
mkdir /var/www/website/logs

cd /var/www/

git clone https://github.com/ilnurgi/website.git

python manage.py syncdb
python manage.py migrate
python manage.py collectstatic

```


### Настройка nginx

```
vim /etc/nginx/sites-available/website

upstream backend_website  {
        server unix:/tmp/website.sock;
}

server {
    listen          80;
    server_name     ilnurgi1.ru;
    access_log      /var/www/website/logs/nginx_access.log;
    error_log       /var/www/website/logs/nginx_error.log;

    location / {
        proxy_pass      http://backend_website;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /media {
        alias /var/www/website/media/;
    }

    location /static {
        alias /var/www/website/static;
    }

    location /docs/android {
        alias /var/www/website/docs/android/_build/html/;
    }

    location /docs/java {
        alias /var/www/website/docs/java/_build/html/;
    }
    
    location /docs/python {
        alias /var/www/website/docs/python/_build/html/;
    }

    location /docs/p4a {
        alias /var/www/website/docs/p4a/_build/html/;
    }

    location /docs/pys60 {
        alias /var/www/website/docs/pys60/_build/html/;
    }

    location /docs/html {
        alias /var/www/website/docs/html/_build/html/;
    }

    location /docs/css {
        alias /var/www/website/docs/css/_build/html/;
    }

    location /docs/js {
        alias /var/www/website/docs/js/_build/html/;
    }

    location /docs/jquery {
        alias /var/www/website/docs/jquery/_build/html/;
    }

    location /docs/angular {
        alias /var/www/website/docs/angular/_build/html/;
    }

    location /docs/sql {
        alias /var/www/website/docs/sql/_build/html/;
    }

    location /docs/linux {
        alias /var/www/website/docs/linux/_build/html/;
    }
}
ln -s /etc/nginx/sites-available/website /etc/nginx/sites-enabled/website
service nginx restart
```

### Настройка supervisor

```
vim /etc/supervisor/conf.d/website.conf

[program:website]
command=/root/virtual_envs/website/bin/gunicorn
    --bind=unix:/tmp/website.sock 
    --access-logfile /var/www/website/logs/gunicorn_acces.log 
    --error-logfile /var/www/website/logs/gunicorn_error.log
    ilnurgi.wsgi:application

directory=/var/www/website/ilnurgi/

user=root
group=root

daemon=False
debug=False

autostart=true
autorestart=true

redirect_stderr=True
redirect_stdout=True
stdout_logfile=/var/www/website/logs/supervisor_out.log
stderr_logfile=/var/www/website/logs/supervisor_err.log

supervisoctl reread
supervisoctl update
```