FROM nginx

RUN rm /etc/nginx/conf.d/default.conf

ADD default.conf /etc/nginx/conf.d/

RUN ls /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]