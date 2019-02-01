# docker-django-react

### install
* git clone https://github.com/qqmikey/docker-django-react.git
* git remote remove origin
* git remote add origin *\<YOURREPOURL\>* 

### generate .env file

* ./bin/create_envfile.sh

### or create manually
* touch .env

* SECRET_KEY=*\<YOURKEY\>*
* POSTGRES_DB=*\<YOURDBNAME\>*
* POSTGRES_USER=*\<YOURDBUSERNAME\>*
* POSTGRES_PASSWORD=*\<YOURDBPASSWORD\>*
* POSTGRES_HOST=db
* POSTGRES_PORT=5432


### develop
* make dev

### production
* make run

