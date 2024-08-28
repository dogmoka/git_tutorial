from bs4 import BeautifulSoup
import requests

res = requests.get("https://www.orangepage.net/recipes/search/111")
soup = BeautifulSoup(res.text, "html.parser")
sche = soup.find(
    "div", id="recipe_list", class_="recipesList recipesList--list active"
)
tags = sche.find_all("h2", class_="tit")
# print(x for x in tags[0].stripped_strings)
text_list = [x.string for x in tags]

print(text_list)
