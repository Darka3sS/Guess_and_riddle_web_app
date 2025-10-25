# Usa un'immagine Node per compilare React
# Step 1: build React
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Step 2: usa un'immagine Apache per servire i file statici
FROM apache/activemq-artemis:latest
COPY --from=build /app/build /usr/local/apache2/htdocs/
EXPOSE 80 443
CMD ["httpd-foreground"]

