FROM python:alpine

COPY ./dist/docker_sqs_consumer-0.1.0-py3-none-any.whl . 

RUN pip install docker_sqs_consumer-0.1.0-py3-none-any.whl

CMD ["consume"]
