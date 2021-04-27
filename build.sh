#!/bin/bash

version=`poetry version --short`
poetry build
docker build . -t dfalves/sqs:$version --build-arg version=$version


