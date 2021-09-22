docker build -t image_custom .
docker container run -p 8000:8000 --rm -d image_custom