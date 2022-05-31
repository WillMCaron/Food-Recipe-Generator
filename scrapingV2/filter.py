
proteins = ['beans', 'lentils', 'chickpeas', 'split peas', 'tofu',
            'nuts', 'almonds', 'pine nuts', 'walnuts', 'macadamias',
            'hazelnuts', 'cashews', 'pumpkin seeds', 'sesame seeds',
            'sunflower seeds','seeds','yogurt','cheese',
            'fish', 'prawns', 'crab', 'lobster', 'mussels', 'oysters',
            'scallops', 'clams','chicken', 'turkey', 'duck', 
            'emu', 'goose','beef', 'lamb', 'veal', 'pork','steak', 'pollack',
           'cod', 'prawns', 'sardines','salmon','crab','halibut','lobster',
           'shrimp', 'meat', 'sausage', 'rice','bruschetta']

whitelist = ['egg salad']
blacklist = ['cookie', 'cream cheese']

def load(text = "foodData.txt"):
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
    ins = False
    for protein in proteins:
      if " "+protein in recipe[2]:
        #print(protein)
        ins = True
    white_listed = False
    for item in whitelist:
      if item in recipe[0]:
        white_listed = True
    black_listed = False
    for item in blacklist:
      if item in recipe[0]:
        black_listed = True
    if (ins or white_listed) and not black_listed:
      recipes.append(recipe)
  return recipes

file = open('filtered.txt','w')
file.close()
file = open('filtered.txt','a')
for item in load():
  #print(item)
  print()
  for subitem in item:
    file.write(subitem.replace(", "," "))
    print(subitem.replace(", "," "))
    #a = input()
    file.write("\n")
  
        
