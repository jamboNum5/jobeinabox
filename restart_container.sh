# for local development

docker stop aprjobe
docker rm aprjobe

docker build -t aprjobe .

docker run -d -p 4000:80 --name aprjobe aprjobe
