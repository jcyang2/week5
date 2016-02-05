# Read the following code.  Do not run it yet.
#
# What do you think you will see if you run this program?

x = 1

def display():
  print(x)
  x = 5

def modify(z):
  print(x)
  z.append(5)

print(x)

display()
# print(x)
x = 5
modify(x)
print(x)
