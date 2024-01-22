import threadingEX
import time


def test_1(something, **kwargs):
  for i in range(300):
    print(f'thread {something} running\nHere: {kwargs["asdf"]}+')
    time.sleep(0.01)
    thread_1.pushReturnVal(i)
  


thread_1 = threadingEX.Threading(test_1, (1,), {"asdf": 1})
thread_1.start()

for i in range(300):
  print(f'thread 1: {thread_1.getReturnVal()}')
  time.sleep(0.01)
