from json import loads
from boto3 import resource, client

from botocore.config import Config

proxy_definitions = {
    # 'http': '',
    # 'https': '',
}

CONFIG = Config(
  retries={
    'max_attempts': 10,
    'mode': 'standard',
  },
  # proxies=proxy_definitions,
)

sqs = resource('sqs', config=CONFIG) 


def main():
  print("Start Consuming Queue")
  queue = sqs.Queue("")
  while True:
    for message in queue.receive_messages():
      try:
        print(loads(message.body))
      except Exception as e:
        print(e)
      finally:
        message.delete()

if __name__ == "__main__":
  main()

