CONTAINER_NAME="cont-netcat-web"
IMAGE_NAME="img-netcat-web"

docker build -t $IMAGE_NAME .

# Remove the container if it already exists
if docker ps -a --format '{{.Names}}' | grep -q "^$CONTAINER_NAME$"; then
  docker stop $CONTAINER_NAME
  docker rm $CONTAINER_NAME
fi

docker run -d --name $CONTAINER_NAME -p 5010:5010 -p 12345:12345 $IMAGE_NAME
