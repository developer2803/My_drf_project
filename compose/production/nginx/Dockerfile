FROM node:14.17.3-alpine AS build-stage
RUN mkdir /client
WORKDIR /client
ENV PATH /client/node_modules/.bin:$PATH
COPY client/package.json .
COPY client/package-lock.json .
RUN npm install
COPY client/ .
RUN npm run build

FROM nginx:1.17.4-alpine
RUN mkdir /front
WORKDIR /front
COPY --from=build-stage /client/build/ /front/
RUN rm /etc/nginx/conf.d/default.conf
COPY compose/production/nginx/nginx.conf /etc/nginx/conf.d
