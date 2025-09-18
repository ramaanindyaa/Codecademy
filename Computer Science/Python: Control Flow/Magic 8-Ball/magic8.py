import random

# Declare the name of the person asking the Magic 8-Ball
name = "Rama"

# Declare the question to ask the Magic 8-Ball
question = "Will I become a great programmer?"

# Declare the variable to store the answer, initially empty
answer = ""

# Generate a random number between 1 and 9
random_number = random.randint(1, 9)

# Debugging: Print the random number to verify it's being generated correctly
# print(random_number)

# Assign an answer based on the randomly generated number
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
else:
    answer = "Error"

# Check if name or question is empty, and print accordingly
if name == "":
    print("Question: " + question)
else:
    print(f"{name} asks: {question}")

if question == "":
    print("You must ask a question for the Magic 8-Ball to answer!")
else:
    print("Magic 8-Ball's answer: " + answer)
