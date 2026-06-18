# insted of many if else you can use match statement 
# the match statement select one of many code to be executed

# this is samae as switch statement in c++
day=2
match day:
  case 1:
    print("Hritii")
  case 2:
    print("Mahto")
  case _:
    print("this is last case ")


day =4

match day:
  case 1 |2|3|4|5:
    print("today is week day")
  case _:
    print("weekend")


#  we can also add if statement in the case evalution as an extra condition-check 

day=5
month=2
match day:
  case 1|2|3|4|5 if month==4:
    print("thoday is week day of month 4")
  case 1|2|3|4|5|6 if month==2:
    print("Hello this is day t of month ")
  case _:
    print("enjoy your week")