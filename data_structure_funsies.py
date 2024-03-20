import json

class Flashcard(class):
  

class Library:
  def __init__(self, name):
    self.name = name
    self.attempts = []
    self.flashcards = []
  def attempt(self):
    # show all the flashcards
    self.flashcards
    overall_set_stats = None
    self.attempts.append(overall_set_stats)
  def stats(self):
    print("average success rate")
    print("average fail rate")
    

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

def modify_libraries():

def edit_libraries(user):
  user.set_passcode("asdfasd")
  

def main():
  # signup and login buttons appear
  data = {}
  data = signup(data)
  print(data)
  user = login(data)
  # # main menu: modes: [play game, edit libraries, view_stats]
  edit_libraries(user)
  print(data)
  
main()