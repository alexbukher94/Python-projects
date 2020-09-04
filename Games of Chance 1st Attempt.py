import random

money = 100
#Create a coin flip guessing game function
print("For the coin flip game, choose 1 for Heads and 2 for Tails")
def coin_flip(guess,bet):
  outcome = random.randint(1,2)
  if guess == outcome:
    return bet
  else:
    return bet * (-1)
final = coin_flip(1,50)

# Create a Cho-Han game function
print("For Cho-Han, guess 0 for even and 1 for odd")
def cho_han(guess,bet):
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,6)
  total = dice1 + dice2
  if total % 2 == 0 and guess == 0:
    return bet
  elif total % 2 == 1 and guess == 1:
    return bet
  else:
    return bet * (-1)
finale = cho_han(1,50)

#Create a function that simulates the card game "War"
def war(bet1, bet2):
  card1 = random.randint(1,11)
  card2 = random.randint(1,11)
  if card1 > card2:
    return "Player 1 wins " + str(bet1)
  elif card1 < card2:
    return "Player 2 wins " + str(bet2)
  else:
    return "Player 1 and 2 win 0"
war_outcome = war(50,25)

#Create a function that simulates roulette
def roulette(guess,bet):
  spin = random.randint(1,36)
  if spin == guess:
    return 0 + guess
  else:
    return 0 - guess
finnito = roulette(25,50)
print(finnito)
