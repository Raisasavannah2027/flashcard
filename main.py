import draft
# # import json_portal

# # import pprint
# import json
# import time
# # from collections import deque

# # # def master_upd_function

# # # def c_username(information):
# # #   with open("data.json", "r") as file:
# # #     data = json.load(file)

# # #     data["username"][0]["library_of_flashcards"][0]["individual_set_(name)"][0]["average_success_rate"] = f"{information}"

# # #   with open("data.json", "w") as file:
# # #     json.dump(data, file, indent=2)

# # # def pull_experiement(x):
# # #   with open("data.json", "r") as file:
# # #     data = json.load(file)
    
# # #   value =  extract_key_value(data, f"{x}")
    
# # #   return(value)

# # # pull_experiement("average_success_rate")
    
# # # list = [false, true, false, true, false, true]

# # def constant_update_experiement(file_path, information, path_layers = None):
# #   if path_layers is None:
# #       path_layers = []
# #   def update_dict_value(dictionary, layers, information):
# #       key = layers[0]
# #       if len(layers) == 1:
# #           dictionary[key] = f"{information}"
# #       else:
# #           dictionary[key] = update_dict_value(dictionary[key], layers[1:], information)
# #       return dictionary

# #   with open(file_path, "r") as file:
# #       data = json.load(file)
# #       data = update_dict_value(data, path_layers, information)
# #       with open(file_path, "w") as file:
# #           json.dump(data, file, indent=2)

# # def constant_update_experiement(file_path, information, path_layers):
# #   def update_dict_value(dictionary, layers, information):
# #     key = layers[0]
# #     if len(layers) == 1:
# #       dictionary[key] = f"{information}"
# #     else:
# #       dictionary[key] = update_dict_value(dictionary[key], layers[1:], information)
# #     return dictionary
# #   with open(file_path, "r") as file:
# #     data = json.load(file)
# #     data = update_dict_value(data, path_layers, information)
# #   with open(file_path, "w") as file:
# #     json.dump(data, file, indent=2)

# # for i in range(1, 61):
# #   time.sleep(1)
# #   constant_update_experiement("minidata.json", i, ["username", "user_id"])
# #   constant_update_experiement("minidata.json", i, ["username", "passcode"])


# #   # def constant_update_experiement(layers):
# #   #   if len(layers) == 2:
# #   #     layer_count = "l2"
# #   #   elif len(layers) == 3:
# #   #     layer_count = "l3"
# #   #   elif len(layers) == 4:
# #   #     layer_count = "l4"
# #   #   elif len(layers) == 5:
# #   #     layer_count = "l5"
# #   #   elif len(layers) == 6:
# #   #     layer_count = "l6"
# #   #   elif len(layers) == 7:
# #   #     layer_count = "l7"
# #   #   elif len(layers) == 8:
# #   #     layer_count = "l8"
# #   #   elif len(layers) == 9:
# #   #     layer_count = "l9"
# #   #   else:
# #   #     print("depth error: failed")
# #   # layer_level_count = constant_update_experiement(path_layers)
# #   # # two layers
# #   # if path_count == "l2":
# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
      
# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"] = f"{information}"

# #   #   with open(file_path, "w") as file:
# #   #     json.dump(data, file, indent=2)
# #   # # three layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 == None and path_layer_5== None and path_layer_6 == None and path_layer_7 == None and path_layer_8 == None and path_layer_9 == None:
# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
      
# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"] = f"{information}"

# #   #   with open(file_path, "w") as file:
# #   #     json.dump(data, file, indent=2)
# #   # # four layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 == None and path_layer_6 == None and path_layer_7 == None and path_layer_8 == None and path_layer_9 == None:
      
# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)

# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"] = f"{information}"

# #   #     with open(file_path, "w") as file:
# #   #       json.dump(data, file, indent=2)
# #   # # five layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 is not None and path_layer_6 == None and path_layer_7 == None and path_layer_8 == None and path_layer_9 == None:

# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
  
# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"][0][f"{path_layer_4}"][0][f"{path_layer_5}"] = f"{information}"
  
# #   #     with open(file_path, "w") as file:
# #   #       json.dump(data, file, indent=2)
# #   # # six layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 is not None and path_layer_6 is not None and path_layer_7 == None and path_layer_8 == None and path_layer_9 == None:

# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
  
#       # data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"][0][f"{path_layer_4}"][0][f"{path_layer_5}"][0][f"{path_layer_6}"] = f"{information}"
  
#       # with open(file_path, "w") as file:
#       #   json.dump(data, file, indent=2)
# #   # # seven layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 is not None and path_layer_6 is not None and path_layer_7 is not None and path_layer_8 == None and path_layer_9 == None:

# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)

# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"][0][f"{path_layer_4}"][0][f"{path_layer_5}"][0][f"{path_layer_6}"][0][f"{path_layer_7}"] = f"{information}"
    
# #   #     with open(file_path, "w") as file:
# #   #       json.dump(data, file, indent=2)
# #   # # eight layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 is not None and path_layer_6 is not None and path_layer_7 is not None and path_layer_8 is not None and path_layer_9 == None:
  
# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
    
# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"][0][f"{path_layer_4}"][0][f"{path_layer_5}"][0][f"{path_layer_6}"][0][f"{path_layer_7}"][0][f"{path_layer_8}"] = f"{information}"
    
# #   #     with open(file_path, "w") as file:
# #   #       json.dump(data, file, indent=2)
# #   # # nine layers
# #   # elif path_layer_1 is not None and path_layer_2 is not None and path_layer_3 is not None and path_layer_4 is not None and path_layer_5 is not None and path_layer_6 is not None and path_layer_7 is not None and path_layer_8 is not None and path_layer_9 is not None:
  
# #   #   with open(file_path, "r") as file:
# #   #     data = json.load(file)
    
# #   #     data[f"{path_layer_1}"][0][f"{path_layer_2}"][0][f"{path_layer_3}"][0][f"{path_layer_4}"][0][f"{path_layer_4}"][0][f"{path_layer_5}"][0][f"{path_layer_6}"][0][f"{path_layer_7}"][0][f"{path_layer_8}"][0][f"{path_layer_9}"] = f"{information}"
    
# #   #     with open(file_path, "w") as file:
# #   #       json.dump(data, file, indent=2)
  
# # # for i in range(1, 61):
# # #   time.sleep(1)
# # #   constant_update_experiement("minidata.json", i, ["username", "user_id"])
# # #   constant_update_experiement("minidata.json", i, ["username", "passcode"])
# #   # constant_update_experiement("data.json", i, "username", "library_of_flashcards", "individual_set_(name)", "average_success_rate")
# #   # constant_update_experiement("data.json", i, "username", "library_of_flashcards", "individual_set_(name)", "overall_set_stats", "overall_set_stats", "score")

# # # def constant_update_experiement(information):
# # #   with open("data.json", "r") as file:
# # #     data = json.load(file)

# # #     data["username"][0]["library_of_flashcards"][0]["individual_set_(name)"][0]["average_success_rate"] = f"{information}"

# # #   with open("data.json", "w") as file:
# # #     json.dump(data, file, indent=2)

# # # for i in range(1, 61):
# # #   # time.sleep(1)
# # #   constant_update_experiement(i)

def constant_update_experiement(file_path, information, path_layers):
  def update_dict_value(dictionary, layers, information):
    if len(layers) == 1:
      dictionary[layers[0]] = f"{information}"
    else:
      key = layers[0]
      dictionary[key] = update_dict_value(dictionary.get(key, {}), layers[1:], information)
    return dictionary
  with open(file_path, "r") as file:
    data = json.load(file)
    update_dict_value(data, path_layers, information)
  with open(file_path, "w") as file:
    json.dump(data, file, indent=2)

# # for i in range(1, 61):
# #   time.sleep(1)
# #   constant_update_experiement("minidata.json", i, ["username", "library_of_flashcards_(id)", "individual_set_(id)", "unique_set_name_(id)"])
# #   constant_update_experiement("minidata.json", i, ["username", "passcode_id"])

# import json
# import time
# def update_dict_value(dictionary, layers, information):
#     if len(layers) == 1:
#         dictionary[layers[0]] = f"{information}"
#     else:
#         key = layers[0]
#         dictionary[key] = update_dict_value(dictionary.get(key, {}), layers[1:], information)
#     return dictionary
# def constant_update_experiement(file_path, information, path_layers):
#     with open(file_path, "r") as file:
#         data = json.load(file)
#         update_dict_value(data, path_layers, information)
#     with open(file_path, "w") as file:
#         json.dump(data, file, indent=2)
# for i in range(1, 61):
#     time.sleep(1)
#     constant_update_experiement("minidata.json", i, [\, "unique_set_name_(id)"])
#     constant_update_experiement("minidata.json", i, ["username", "passcode_id"])