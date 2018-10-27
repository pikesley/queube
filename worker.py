import os
import sys
sys.path.append('../cubebit')
import cubebit as cb

import json
import itertools
import pika
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')
QUEUE = os.getenv('QUEUE')

side = 3
cb.create(side)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE)

def flatten(colours):
  return list(itertools.chain.from_iterable(itertools.chain.from_iterable(colours)))

def reorder(colours):
  indeces = [0, 3, 6, 7, 4, 1, 2, 5, 8,
             17, 16, 15, 12, 13, 14, 11, 10, 9,
             18, 21, 24, 25, 22, 19, 20, 23, 26]
  reordered = []
  for i in range(27):
      reordered.append(colours[indeces[i]])
  return reordered
  
def callback(ch, method, properties, body):
  d = json.loads(body.decode('utf-8'))
  try:
    colours = reorder(flatten(d['data']))
    for i in range(27):
      cb.setPixel(i, cb.fromRGB(*colours[i]))
    cb.show()
  except Exception:
    print('Your data is bad')

channel.basic_consume(callback,
                      queue=QUEUE,
                      no_ack=True)

print(' [*] Waiting for jobs')
channel.start_consuming()
