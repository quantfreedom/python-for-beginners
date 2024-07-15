course = 'python for beginners'
course = 'python course's for beginners'
course = "python course's for beginners"
course = "python course's for "beginners"
course = 'python course for "beginners"'

course = """
hello everyone
this is he email i need to send to everyone

thanks!
"""

course =''' 
hello everyone
this is he email i need to send to everyone
thanks!
'''

print(course[0])
print(course[-1])
print(course[1:4])
print(course[:4])
print(course[4:])

person = "Dave"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %d coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(person=person, coins=coins)


