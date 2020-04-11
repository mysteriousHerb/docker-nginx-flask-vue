FROM node:lts-alpine

# install project dependencies
RUN npm install -g @vue/cli

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . /frontend

# 8080 for our vue app, 8000 for the vue ui
EXPOSE 8080, 8000

CMD [ "vue", "ui" ]