import random
from collections import deque


flashcards = {
  "a" : "hello",
  "b" : "yes",
  "c" : "tis not thoust",
  "d" :  "no"
}

list_of_flashcards = ["a", "b", "c", "d"]


random.shuffle(list_of_flashcards)

for i in range(4):
  x = list_of_flashcards[i]
  print(f"\nWhat is the answer for: {x}")
  xi = flashcards.get(x)
  user_input = input()
  if user_input == xi:
    print("\nYou Got It!")
  else:
    print("\nSomthing is either broken or you got it wrong!")