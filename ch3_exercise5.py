"""Try creating a program that will ask the user how far they wish to travel. If they express a desire to travel less
 than three miles, have the program tell them to walk. If they desire to travel more than three miles, but less than
  three hundred miles, advise them that they should drive. In any instance where they want to travel three hundred or
   more miles, tell them to fly."""

print("What distance do you wish to travel?")
print("1. Less than 3 miles")
print("2. More than 3 miles but less than 300 miles")
print("3. More than 300 miles")
print("Please, give your answer with a number from 1 to 3")

answer = int(input())
if answer == 1:
    transport = "walking"
elif answer == 2:
    transport = "driving"
elif answer == 3:
    transport = "flying"
else:
    print("Please give your answer by typing a number from 1 to 3")

print("I suggest {} to your destination.".format(transport))