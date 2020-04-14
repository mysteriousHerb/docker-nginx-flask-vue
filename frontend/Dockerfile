FROM node:lts-alpine

# install project dependencies
RUN npm install -g @vue/cli

# copy project files and folders to the current working directory (i.e. 'app' folder)
ADD . /frontend

#  https://stackoverflow.com/questions/57743092/vue-ui-is-not-working-through-docker-compose/57751123#57751123
CMD [ "vue", "ui", "--headless" , "--port", "8000",  "--host", "0.0.0.0" ]