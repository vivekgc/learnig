FROM node:8
MAINTAINER vivgc16305@gmail.com Vivek GC


WORKDIR /app
COPY . .

RUN npm install express
RUN npm install

EXPOSE 8080

#Runs in development Mode
CMD ["npm", "start"]