import random

# loop
#ask the user:roll the dice?
#if user enters y
#generate two random numbers 
#print them
#if user enters n
#print thank you message
#terminate
#else
# print invalid choice
while True:
  choice=input('Roll the dice? y/n:  ').lower()
  if choice=='y':
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    print(f'({die1}, {die2})')
  elif choice=='n':
    print('Thanks for playing')    
    break 
  else:
   print('invalid choice!')