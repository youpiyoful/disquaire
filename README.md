# disquaire

__a little disquaire project with Django framework__

## create volume and launch postgres container
* docker pull postgres:latest
* docker run --rm   --name pg-docker -e POSTGRES_PASSWORD=<your_password> -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data  postgres


