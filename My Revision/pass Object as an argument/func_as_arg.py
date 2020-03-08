class FooRest:
    def __init__(self, prefix):
        self.prefix = prefix

    def foo(self, name):
        print("{} {}".format(self.prefix, name))

def Rest(some_method):
    foorest = FooRest("Prof. ")
    some_method(foorest, "Ahmed Zaky")

Rest(FooRest.foo)
