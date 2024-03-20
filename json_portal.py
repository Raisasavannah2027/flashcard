Hireryecyimport pprint
import json
import time

# def main_json_updating_function():
#   def useless_key_striping_function():

with open("flashcards.json", "r") as file:

  data = json.load(file)
for i in range(6):
  question = data[i]
  print(question)
  