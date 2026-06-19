# an iterator  is an object that contains a countable number of values 

#   An iterator is an object whihc implements the iterator protocol whihc consist of the method __iter__() and __next()__

# list tuple , dictionary all are iterable object, they are iterable container whihc you can get an iterator from 

# run a iterator from tuple and print each value 

mytuple=("apple","banana","mango")

myit=iter(mytuple)

print(next(myit))  # iterates and print the value 
print(next(myit))
print(next(myit))


# strings can also be iterated 
mystr="hritik"

mystrit=iter(mystr)

print(next(mystrit))   # iterates and prints first value
print(next(mystrit))   # iterates and print sencond index value 

# we can also loop to iterate through an iterable object.

for i in mytuple:
  print(i)      # this will print elements insted of index because we are using in not length 

# all calss have a fiunction called __init__() whihc allows yout to do some initialization when the object is created 

# The __iter__() method similar, you can do operations must always reutrn the iterator object itself.
# The __next__() method also allows you to do operations and must return the next item in sequence.

 # create iterator to retunr numbber from 1  to 10

class mynumber:
  def __iter__(self):
    self.a=1
    return self
  def __next__(self):
    x=self.a
    self.a+=1
    return x
myClass=mynumber()
myiter=iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

# the upper statement continue printting if it is used in fro loop 
# to prevent the iteration going forever we use stopIteration statement 
 
# in the next method we can add termination condition to raise an error if the iteration id done specific number of times

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
