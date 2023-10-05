# First class objects
# can be passed to a function as an argument
# can be returned from function
# can be assigned to a variable
# can be stored in datastructure
# can be stored in a datastructure

# int, float, string, tuple etc are all first class object
# functions are also first objects

# Higher order functions
# Higher order functions are functions that take function(s) as an argument
# higher order functions are functions that return function

# Docstrings  #PEP257
# if first line in a function is a string , it will be interpreted sa a docstring

def hello(name=""):
    '''this function prints hello with name supplied
    '''
    print(f"Hello {name}!!")


hello()
hello("Shekhar")

# help(hello)
# where are docstrings stored ?
# functions have __doc__ property where it is stored
print(hello.__doc__)


def fact(n):
    ''' Calculates factorial of number n
    :param n: non-negative integer
    :return: the factorial of number
    '''
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))
print(fact.__doc__)


# functions annotations are another way to document functions
# PEP3107
# annotations are stored in __annotations__ property
# keys are parameter name and values are annotations
def echo(msg: str, b: 'int > 0' = 1) -> str:
    ''' echo function echoes gives message n number of times

    :param msg: a string, represents message that needs to be echoed
    :param b: an int, represents the number of times to echo the message
    :return: a string , returns echoed messaged
    '''
    return msg * b


print(echo("Yahoo "))
# annotations are not stored in __doc__
print(f"echo doc: {echo.__doc__}")
# print(f" {help(echo)}")
print(f"annotation: {echo.__annotations__}")


# enhanced version of annotations is type hints

def wish(msg: 'enter a lovely message for wishing someone',
         person: 'enter person to whom to wish',
         n: 'how many times to wish' = 1) -> 'message to be wished':
    '''
    wish function wishes a person with a message
    :param msg: message to be wished
    :param person: person to whom message to be wished
    :param n: how many times to wish
    :return: message for which
    '''
    return (f"Hello {person}, {msg}" * n)


print(wish("Happy B'day", "Rayaan"))
print(wish.__doc__)
print(wish.__annotations__)


def some_fun(a: str = '',
             b: int = 1,
             *args: 'some positional arguments',
             k1: 'kew word arg-1',
             k2: 'kew word arg-2',
             **kwargs: 'some key-word args'
             ) -> 'returns something':
    '''
    some fun about Alibaba and 40 thieves
    :param a: string , message
    :param b: int, number of times
    :param args: additional positional arguments
    :param k1: string
    :param k2: string
    :param kwargs: additional keyword arguments
    :return: some message
    '''
    print(a, b, args, k1, k2, kwargs)
    return (a + '\n') * b


print(some_fun('khul ja sim sim', 2, 7, 8, 9, k1="ali", k2="baba", k3="40", k4="thieves"))
