FROM nginx:1.27.3-alpine-slim

RUN apk add --no-cache openssl bash gettext

RUN mkdir -p /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/inception.key \
    -out /etc/nginx/ssl/inception.crt \
    -subj "/C=TR/ST=Istanbul/L=Istanbul/O=mtu/OU=Development/CN=localhost"

COPY ./nginx.conf.template /etc/nginx/nginx.conf.template

CMD envsubst '${FRONTEND_DOMAIN} ${BACKEND_DOMAIN} ${GRAFANA_DOMAIN}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'

EXPOSE 80 443
