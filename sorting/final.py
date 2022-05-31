########## increase database size with less ingredients!################
#########################################################################
def eliminate(username):
  username_curr = username
  #a = input(str(username_curr))
  with open("/home/runner/MOMTRY/list.txt","r") as f:
    contents = f.read()
  if username_curr:
    contents = contents.split("\n")
    contents = contents[:len(contents)-1]
    user_contents = []
    for item in contents:
      if item.partition(":")[0] == username_curr:
        if item.partition(":")[2] not in user_contents:
          user_contents.append(item.partition(":")[2])
          #a = input(item.partition(":")[2])
    print(user_contents)
  
  recipes = loadme()
  #print("Start")
  #print(len(recipes))
  ingr = ingredients(recipes)
  lst = []
  # for each recipe
  for recipe in ingr:
    lst = []
    #print(recipes[ingr.index(recipe)][0])
    # extract the ingredients
    for i in recipe.split(','):
      if i not in lst:
        lst.append(i)
    
  finalists = []
  idx = 0
  STRICTNESS = 0.8
  # for each recipe
  for recipe in ingr:
    # separate recipes
    recipe = recipe.split(",")
    # count of ingredients you have in recipe
    count = 0
    # amount of ingredients in recipe
    length = len(recipe)
    # for each ingredient
    for ingredient in recipe:
      # loop through your entered items
      for have in user_contents:
        # increment count if ingredient in recipe
        if have in ingredient:
          count += 1
    # if you have at least 80 percent of the recipe
    strictness = int(STRICTNESS*(length-1))
    #print(count, strictness, length-1)
    #print(count)
    if count >= strictness:
      finalists.append(idx)
    idx +=1



    
  string = ''
  for i in finalists:
    print(recipes[i][0])
    print(recipes[i][1])
    print()
    string += str(recipes[i][0]) + "<br>"
    string += str(recipes[i][1]) + "<br>"
    string += '<br>'
  #print(string)
  return string

def loadme(text = '/home/runner/MOMTRY/removed/filtered.txt'):
  file = open(text,"r")
  data = file.read()
  data = data.split("\n")
  recipes = []
  for i in range(3,len(data),4):
    recipe = []
    recipe.append(data[i-3])
    recipe.append(data[i-2])
    recipe.append(data[i-1])
    recipe.append(data[i])
    recipes.append(recipe)
  return recipes

def ingredients(recipes):
  ingredients = []
  for i in range(len(recipes)):
    ingredients.append(recipes[i][2])
  return ingredients
