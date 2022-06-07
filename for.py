#Exit the loop when x is "hockey", but this time the break comes before the print""""

games = ["cricket", "football", "hockey"]
for x in games:
  if x == "hockey":
    break
  print(x)

# donot print cricket
games = ["cricket", "football", "hockey"]
for x in games:
  if x == "football":
    continue
  print(x)

  # start parameter
  for x in range(2, 5):
    print(x)

    # else in for loop
for x in range(5):
  print(x)
else:
  print("Finally finished!")

  ##Print each games for every player:
games = ["cricket", "football", "hockey"]
player = ["neymar", "messi", "suarez"]

for x in games:
  for y in player:
    print(x,y)

# if statement
a = 55
b = 100
if b > a:
  print("b is greater than a")

  # elif
  a = 2
  b = 2
  if a > b:
    print("b is greater than a")
  elif a == b:
    print("a and b are equal")

    # else
    a = 200
    b = 33
    if b > a:
      print("b is greater than a")
    elif a == b:
      print("a and b are equal")
    else:
      print("a is greater than b")

# nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
