from json import loads
from boto3 import resource

sqs = resource('sqs') 


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

