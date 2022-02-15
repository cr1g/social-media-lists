FROM nginx:alpine

ARG REVERSE_PROXY_PORT
ARG API_HOST
ARG API_PORT

RUN apk add gettext

WORKDIR /etc/nginx/conf.d

COPY default.conf default.template.conf
RUN envsubst '$API_HOST $API_PORT $REVERSE_PROXY_PORT' < "default.template.conf" > "default.conf"
RUN rm default.template.conf
