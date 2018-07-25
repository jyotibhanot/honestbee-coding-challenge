#Pull base image
FROM jyotibhanot30/ubuntu-base:latest

# Adding nginx repo
RUN apt-get install software-properties-common -y \
    && add-apt-repository ppa:nginx/stable \
    && apt-get update -y

RUN apt-get install nginx -y \
    && chown -R www-data:www-data /var/lib/nginx
 
WORKDIR /var/www/html/
RUN mv index.nginx-debian.html index.nginx-debian.html.BAK
COPY index.html .

# Define mountable directories.
VOLUME ["/var/log/nginx"]
WORKDIR /etc/nginx
COPY nginx.conf .
CMD ["nginx"]
