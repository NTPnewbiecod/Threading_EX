import threadingEX
import time


def test_1(something):
  for i in range(300):
    print(f'thread {something} running')
    time.sleep(0.01)
    thread_1._pushReturnVal(i)
  


thread_1 = threadingEX.Threading(test_1, 1)
thread_1.start()

for i in range(300):
  print(f'thread 1: {thread_1._getReturnVal()}')
  time.sleep(0.01)
