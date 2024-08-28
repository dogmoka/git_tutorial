from bs4 import BeautifulSoup
import requests

# リクエストを送信
res = requests.get("https://www.orangepage.net/recipes/search/111")

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(res.text, "html.parser")

# 正しい引数でfindメソッドを使ってdiv要素を取得
sche = soup.find("div", id="recipe_list", class_="recipesList recipesList--list active")

# div要素が正しく取得できたか確認
if sche is not None:
    # h2要素を全て取得
    tags = sche.find_all("h2", class_="tit")

    # 各h2要素から文字列を取得
    text_list = [tag.get_text(strip=True) for tag in tags]

    # 取得した文字列を表示
    print(text_list)
else:
    print("指定したdiv要素が見つかりませんでした。")
