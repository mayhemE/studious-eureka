import random

name = "Joe"
question = "Will I win a lottery?"
answer = ""

random_number = random.randint(1, 12)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
elif random_number == 10:
  answer = "It could be"
elif random_number == 11:
  answer = "Better luck next time"
elif random_number == 12:
  answer = "No - not at all"
else:
  answer = "Error"

if name: 
 print(name + " asks: " + question)
else:
  print("ask: " + question)
print("Magic 8 Balls answer: " + answer)
if question:
   print(name + " asks: " + question)
else:
  print("A question is required")

