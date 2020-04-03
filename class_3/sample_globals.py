

global i


def my_func_one():
    global i
    i = "foo"

    print(i)


def two_func():
    global i
    i = "bar"



def outer():
    global i
    i = "A"
    my_func_one()
    two_func()

    print("and the final value is...")
    print(i)


outer()










