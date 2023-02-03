import random


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]


def iter_():
    for i in range(5):
        yield 'test'


for i in iter_():
    print(i)


class new_():
    def __init__(self, value, max_repeat):
        self.max_repeat = max_repeat
        self.value = value
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeat:
            raise StopIteration
        self.count += 1
        return self.value

ip = {
        '10.119.243.3': True,
        '10.119.243.234': True,
        '10.119.243.54': True,
        '10.119.243.545': True,
        '10.119.243.123': True,
        '10.119.243.122': True,
        '10.119.243.121': True,
        '10.119.243.124': True,
        '10.119.243.125': True,
    }

d = {
    'False': False,
    'True': True
}