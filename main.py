# Exercise One 

count = 0

while count < 10:
    print(count)
    count = count + 1

# Exercise Two 

password = ""

while password != "secret":
    user_input = input("Enter the password")
    if user_input == "secret":
        break;
        
# Exercise Three 

count = 0

while count < 10:
  count = count + 1
  if count % 2 == 0:
    continue
  print(count)
  
# Exercise Four 

attempts = 0

while attempts < 3:
    attempts += 1
    guess = input("Guess the lucky number: ")
    if guess == "7":
        print("You win!")
        break
else:
    print("You ran out of attempts. You lose!")
