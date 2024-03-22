# import json
import pickle
import random as rand


class Flashcard:
  def __init__(self, key, value):
    self.key = key 
    self.value = value
    self.guessed_answer = []
    self.answer_state_list = []
  def display_key(self):
    print(f"{self.key}")
  def display_value(self):
    print(f"{self.value}")
  def stat_modifier(self, guesses, answer_state_list):
    # When pulling from the code, it will pull whether it was correct or incorect to assemble a list, then take the average
    new_ave = sum(answer_state_list)/(len(answer_state_list)+1)
    
  def user_answer(self):
    # record current time
    user_input = input("What do you think the answer is: ")
    # record current time
    # subtract and add to rt log (in flashcard class)
    self.guessed_answer.append(user_input)
    correct = user_input == self.value
    self.answer_state_list.append(correct)
    self.interface_responce(correct)
  
  def interface_responce(self, correct):
    if correct:
      print("correct")
    else:
      print("incorrect")


class Library:
  def __init__(self, name):
    self.name = name
    self.attempts = []
    self.flashcard_list = []
      
  def show_library(self):
    print(f"{self.flashcard_list}")

  def write_to_pickle(self, object):
    with open("data.pickle", "wb") as file:
      pickle.dump(object, file)
  
  def pull_pickle(self):
    with open("data.pickle", "rb") as file:
      self.flashcard_list = pickle.load(file)
  
  def attempt(self):
    rand.shuffle(self.flashcard_list)
    
    for flashcard in self.flashcard_list:
      flashcard.display_key()
      flashcard.user_answer()
      flashcard.display_value()
    overall_set_stats = None
    self.attempts.append(overall_set_stats)
    
  def edit(self,):
    self.pull_pickle()
    # show current flashcards list
    # option to add new flashcard
    user_input = input("Do you want to create a flashcard [y/n]: ")
    if user_input == "y":
      user_input_key = input("What do you want the question to be: ")
      user_input_value = input("What do you want the answser to be: ")
      new_flashcard = [Flashcard(user_input_key, user_input_value)]
      self.flashcard_list.append(new_flashcard[0])
      self.write_to_pickle(self.flashcard_list)
    else:
      print("Thank you --> next question asks if user would like to terminate the program")
    # ,
    # Flashcard("b", "yes"),
    # Flashcard("c", "tis not thoust"),
    # Flashcard("d", "no")
    
  # def stats(self):
  #   print("average success rate")
  #   print("average fail rate")



library = Library("test")
library.show_library()
library.pull_pickle()
library.show_library()
library.edit()
library.edit()
library.attempt()





class User:
  def __init__(self, username, passcode):
    self.username = username
    self.passcode = passcode
    self.libraries = {}

  def get_passcode(self):
    return self.passcode

  def get_username(self):
    return self.username

  def set_passcode(self, new_passcode):
    self.passcode = new_passcode

  def __repr__(self):
    return f"""
Username: {self.username},
Passcode: {self.passcode}
"""

def login(data):
  # if a new user comes along
  username = "user3"
  user = data[username]
  correct_passcode = user.get_passcode()
  # check passcode!
  return user
  
def signup(data):
  new_user = "user2"
  passcode = "my very secure password"
  user = User(new_user, passcode)
  data[new_user] = user
  return data

def play_game(user):
  user.set_passcode("asdfasd")

# def modify_libraries():

def edit_libraries(user):
  user.set_passcode("asdfasd")
  

# def main():
#   # signup and login buttons appear
#   data = {}
#   data = signup(data)
#   print(data)
#   user = login(data)
#   # # main menu: modes: [play game, edit libraries, view_stats]
#   edit_libraries(user)
#   print(data)
  
# main()