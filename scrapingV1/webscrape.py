from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import warnings
from time import sleep


warnings.filterwarnings("ignore", category=DeprecationWarning)

# url for site
URL = 'https://www.allrecipes.com/'

def connect(url = URL):
  """Initializes and returns chrome driver"""
  # create chrome driver
  options = Options()
  # no graphics
  options.add_argument('headless')
  # replit things
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  # reduces log messages
  options.add_argument('--log-level=3')
    
  driver = webdriver.Chrome(options = options)
  # try except to prevent timeout, would kick the scraper
  try:
    driver.get(url)
    sleep(5)
  except TimeoutException:
    print('new connection try')
    driver.get(url)
    sleep(5)

  return driver
    
driver = connect(URL)
#print(driver.page_source)
# the titles
all_titles = []
base = driver.find_elements_by_xpath("//a[@class='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom']")
for a in base:
  all_titles.append(a.text.lower())
#print(all_titles)
all_links = []
for a in base:
  all_links.append(a.get_attribute('href'))
#print(all_links)

idx = 88

for link in all_links[idx:len(all_links)-1]:
  driver = connect(link)
  ingredients = []
  # get ingredients
  for a in driver.find_elements_by_xpath("//span[@class='ingredients-item-name elementFont__body']"):
    ingredients.append(a.text)
  # servings and total time (idx -2 and -3)
  values = []
  for a in driver.find_elements_by_xpath("//div[@class='recipe-meta-item-body elementFont__subtitle']"):
    values.append(a.text)
  file = open('foodData.txt',"a")
  file.write(all_titles[idx].lower()+"\n")
  print(all_titles[idx])
  file.write(link+"\n")
  for ingredient in ingredients:
    file.write(ingredient.lower()+",")
  file.write("\n")
  print(ingredients)
  print(values)
  #servings,total time
  file.write(values[-2]+","+values[-3]+"\n")
  idx+=1
  print(idx)
#print(all_ingredients)
driver.quit()

