from json import loads
from boto3 import resource, client

from botocore.config import Config

proxy_definitions = {
    'http': 'http://pagseguro.proxy.srv.intranet:80',
    'https': 'http://pagseguro.proxy.srv.intranet:80',
}

CONFIG = Config(
  retries={
    'max_attempts': 10,
    'mode': 'standard',
  },
  proxies=proxy_definitions,
)

sqs = resource('sqs', config=CONFIG) 


def main():
  print("Start Consuming Queue")
  queue = sqs.get_queue_by_name(QueueName="MyQueue")
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

