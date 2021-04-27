version=$(poetry version --short)

build:
  echo "dockerrrrrr"
  docker build . -t dfqalves/sqs:$(version)