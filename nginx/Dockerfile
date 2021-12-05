FROM nginx:1.21-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf

RUN mkdir -p /etc/nginx/cert
COPY ./cert/*.pem /etc/nginx/cert/

