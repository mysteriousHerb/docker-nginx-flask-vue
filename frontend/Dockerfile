FROM node:lts-alpine

# install project dependencies
RUN npm install -g @vue/cli

# copy project files and folders to the current working directory (i.e. 'app' folder)
ADD . /frontend

# test the vue ui


CMD [ "vue", "ui" ]