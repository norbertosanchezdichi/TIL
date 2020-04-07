from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Navigating Via Tags
data = soup.body.contents[1].contents
print(data)

data = soup.body.contents[1].next_sibling.next_sibling
print(data)

data = soup.find(class_ = "super-special").parent
print(data)

# Navigating Via Searching
data = soup.find(id = "first").find_next_sibling()
print(data)

data = soup.find(id = "first").find_next_sibling().find_next_sibling()
print(data)

data = soup.select("[data-example]")[1].find_previous_sibling()
print(data)

data = soup.find(class_ = "super-special").find_next_sibling(class_ = "special")
print(data)

data = soup.find("h3").find_parent("html")
print(data)