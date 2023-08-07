FROM nginx:1.25

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

RUN apt-get update && apt-get install -y procps
RUN mkdir -p /var/www/html/static/
RUN chmod -R 755 /var/www/html/static/