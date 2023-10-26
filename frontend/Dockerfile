FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 3000

# VOLUME [ "/app/frontend_vol" ]

CMD [ "npm", "start" ]