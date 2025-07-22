docker-compose down

#docker run -it --rm --name certbot \
# -v "./certbot/etc:/etc/letsencrypt" \
# -v "./certbot/var:/var/lib/letsencrypt" \
# -p 80:80 \
# certbot/certbot certonly --standalone -d meeting.mosckba.ru --email it.dpm@emk.ru --agree-tos --non-interactive --keep-until-expiring

# 1. Создать папки для сертификатов
### rm -rf certbot
mkdir -p certbot/etc certbot/var

# 2. Запустить только Nginx (без certbot)
docker-compose up -d nginx

# 3. Получить сертификаты
docker-compose run --rm certbot

# 4. Добавить SSL конфигурацию в Nginx и перезапустить
docker-compose stop nginx
docker-compose up -d