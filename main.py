import fire

def hello(message='world'):
    return f"hello: {message}"

def goodbye(message='world'):
  return f"goodbye: {message}"

if __name__ == '__main__':
  fire.Fire()
