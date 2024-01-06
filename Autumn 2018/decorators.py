import time

def verbose(func):
  def new_func():
    print('{}() has been called'.format(func.__name__))
    func()
  return new_func

@verbose
def test():
  time.sleep(3)
  print('Slept')

@verbose
def nested_test():
  time.sleep(2)
  test()

test()
nested_test()
