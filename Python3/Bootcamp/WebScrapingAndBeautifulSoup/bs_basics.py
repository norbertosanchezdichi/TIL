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
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.body)
print(soup.body.div)
print(soup.find("div"))
print(soup.find_all("div"))

d = soup.find(id = "first")
print(d)

s = soup.find(class_ = "special")
print(s)

de = soup.find_all(attrs={"data-sample": "yes"})
print(de)