from json import loads
from boto3 import resource

sqs = resource('sqs') 


def main():
  print("Start Consuming Queue")
  queue = sqs.get_queue_by_name(QueueName="MyQueue")
  for message in queue.receive_messages():
    print(loads(message.body))
    message.delete()

if __name__ == "__main__":
  while True:
    main()
