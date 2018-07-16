FROM nginx:latest

ADD nginx/nginx.conf /etc/nginx/nginx.conf

RUN mkdir -p /var/www/static

WORKDIR /var/www/static
ADD static /var/www/static
RUN chown -R nginx:nginx /var/www/static