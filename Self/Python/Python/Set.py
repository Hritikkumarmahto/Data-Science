# set is a collection of unordered items 
# each element must be unique and immutable 

# nums={1,2,3,4}
# nums= {1,2,2,2} here the numbers are repaetrin so the numbers will be {1,2} only in the set because it only stores unique elements

# set is mutable because we can add or delete eemenets inside set but the element are set in immutable 
# null_set=set() we can also create empty set like this 

set_values={1,2,3,3,2,5,54,"hritik","kumar","Mahto"} # will print only nique elements form the set

print(set_values)

print(type(set_values))


# to create empty sets 
# collection={} # this is not how we create empty set because this is empty dictionary

colelction=set() # this is how we create empty sets


# Methods in set

# 1. add() - this adds the element into the set

set_values.add("kishanganj")
print(set_values)


# the elements of set are immutable becaise we can not modify this  
# we can only add TUPLE in the set not list not dictionar because tuple is also immutable 



set_values.add("Bihar")
set_values.add("Patna")
set_values.add("dehli")
print(set_values)




# 2. remove()-  function us use to remove the element from the set
set_values.remove("dehli")
print(set_values)


# 3. clear() - this dunction is use to cleaar whole set directly 
colelction.add("Iq")
colelction.add("ghello")

print(colelction)
colelction.clear()

print(colelction) # this will return empty set 


# 4. pop() this removes a random value from the set


colelction.add("Iq")
colelction.add("ghello")
colelction.pop()  #here hello poped because in each pop it will remove atelase one element

print(colelction)

# 5. Union() combines both set values of return new set

colelction={"hritik","kumar","mahto",855108} 
colelction2={"hello","world","mahto",855108}

print(colelction.union(colelction2))   # it will print the unique values from each set

# 6. intersection() combines common valyes and return new value


print(colelction.intersection(colelction2)) # will return common values

# practice questions

set_of_classroom={"java","c++","c","java","java","pythonn"}
print(set_of_classroom)
print(len(set_of_classroom))