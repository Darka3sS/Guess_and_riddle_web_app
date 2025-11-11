# Usa un'immagine Node per compilare React
# Step 1: build React 
FROM node:20 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# ESEGUIAMO LO SCRIPT DI BUILD!
# Questo comando (definito nel tuo nuovo package.json)
# crea la cartella ottimizzata "dist".
RUN npm run build

# --- FASE 2: "Serve" ---
# Ora partiamo da un'immagine "pulita" e leggerissima di Nginx.
# Il container finale avrà SOLO Nginx e i file statici.
FROM nginx:1.25-alpine

# Copiamo i file statici (HTML, JS, CSS) che abbiamo creato
# nella FASE 1 (da "build") dentro la cartella che Nginx usa
# per servire i siti web.
COPY --from=build /app/dist /usr/share/nginx/html

# Nginx ha una configurazione di default che non funziona bene con React.
# La rimuoviamo...
RUN rm /etc/nginx/conf.d/default.conf

# ...e la sostituiamo con la nostra configurazione personalizzata.
# (Devi creare il file "nginx.conf" accanto a questo Dockerfile)
COPY nginx.conf /etc/nginx/conf.d/default.conf
