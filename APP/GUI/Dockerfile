FROM node:16.10-slim
COPY build /app/build
WORKDIR /app

RUN npm install react-inject-env@2.1.0 http-server@14.1.1

EXPOSE 8080

ENTRYPOINT npx react-inject-env set && npx http-server -c-1 -p 8080 build
