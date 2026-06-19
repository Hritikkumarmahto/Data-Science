# decorators let you add extra behaviour to a function, without changing the actual code
# a decorator is a function that takes another function as input and returns a new function


# define the decorators first then apply it @decorator_name as input above the function

def changeCase(func):
  def innerFunction():
    return func().upper()
  return innerFunction

@changeCase            # this is how we add decorator 
def myfunction():
  return "hello hritik"
print(myfunction)

