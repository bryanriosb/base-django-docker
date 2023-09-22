FROM nginx:1.25.2-alpine
RUN mkdir -p /app/manager/static/
RUN rm /etc/nginx/conf.d/default.conf
COPY /compose/sta/nginx/nginx.conf /etc/nginx/conf.d