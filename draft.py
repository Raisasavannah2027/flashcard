import random
from collections import deque


flashcard_library = {
  "a" : "hello",
  "b" : "yes",
  "c" : "tis not thoust",
  "d" : "no"
}

list_of_flashcards = list(flashcard_library.keys())

random.shuffle(list_of_flashcards)

for i in range(4):
  x = list_of_flashcards[i]
  print(f"\nWhat is the answer for: {x}")
  xi = flashcard_library[x]
  user_input = input()
  if user_input == xi:
    print("\nYou Got It!")
  else:
    print("\nSomthing is either broken or you got it wrong!")