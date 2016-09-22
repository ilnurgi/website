# Мой сайт

## Порядок разворачивания

### Установка зависимостей

```
apt-get update 
apt-get upgrade
apt-get install python-pip python-dev supervisor nginx git sudo mongodb vim htop mc
```

### Создание пользователя

```
sudo useradd vasyapupkin
mkdir /home/vasyapupkin
sudo passwd vasyapupkin
sudo visudo
vasyapupkin ALL=(ALL) ALL
```

### Настройка python окружения 

```
pip install pip --upgrade
pip install virtualenwrapper

vim .bashrc
    export WORKON_HOME=/home/vasyapupkin/virtual_envs
    source /usr/local/bin/virtualenvwrapper.sh

source .bashrc

mkdir -p $WORKON_HOME

mkvirtualenv website

pip install -r requirements
```


### Клонирование проекта

```
mkdir website/logs

git clone https://github.com/ilnurgi/website.git

python manage.py migrate
python manage.py collectstatic

```


### Настройка nginx

```
cp website/etc/nginx/sites-available/website /etc/nginx/sites-available
ln -s /etc/nginx/sites-available/website /etc/nginx/sites-enabled/website
service nginx restart
```

### Настройка supervisor

```
cp website/etc/supervisor/conf.d/website.conf /etc/supervisor/conf.d/website.conf
cp website/etc/supervisor/conf.d/website_celery.conf /etc/supervisor/conf.d/website_celery.conf
cp website/etc/supervisor/conf.d/cpu_average.conf /etc/supervisor/conf.d/cpu_average.conf

supervisoctl reread
supervisoctl update
```

### Задачи крона

```
sudo crontab -e
0 0 * * * /home/vasyapupkin/virtual_envs/website/bin/python /home/vasyapupkin/website/manage.py parse_nginx_access
0 10 * * * /home/vasyapupkin/virtual_envs/website/bin/python /home/vasyapupkin/website/manage.py make_conspects
```