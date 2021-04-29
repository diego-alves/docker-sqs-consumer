
from logging import info, warning, error
from os import getenv
from json import loads
from boto3 import resource, client

from botocore.config import Config

PROXY = getenv("BOTO_PROXY",)
QUEUE_URL = getenv("QUEUE_URL")

proxy_definitions = {
    'http': PROXY,
    'https': PROXY,
} if PROXY else None

CONFIG = Config(
  retries={
    'max_attempts': 10,
    'mode': 'standard',
  },
  proxies=proxy_definitions,
)

sqs = resource('sqs', config=CONFIG) 


def main():
  info("Start Consuming Queue")
  queue = sqs.Queue(QUEUE_URL)
  while True:
    for message in queue.receive_messages():
      try:
        warning(loads(message.body))
      except Exception as e:
        error(e)
      finally:
        message.delete()

if __name__ == "__main__":
  main()

