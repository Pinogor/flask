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




