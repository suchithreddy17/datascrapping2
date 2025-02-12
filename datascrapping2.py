!pip install bs4
from bs4 import BeautifulSoup
import pandas as pd
# Sample HTML document
html_doc = """
<html>
<head><title>World's Population</title></head>
<body>
    <h1>Main Heading</h1>
    <p class="xyz">This is a paragraph.</p>
    <p class="content">Another paragraph with <a href="https://example.com">a link</a>.</p>

    <div id="container">
        <ul>
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>
    </div>

    <table>
        <tr><th>Name</th><th>Age</th></tr>
        <tr><td>Alice</td><td>25</td></tr>
        <tr><td>Bob</td><td>30</td></tr>
    </table>
</body>
</html>
"""
s= BeautifulSoup(html_doc, "html.parser")
x=s.find_all("tr")
name=[]
age=[]
td=s.find_all("td")
for i in td:
  if(i.text.isdigit()):
    age.append(i.text)
    !pip install bs4
from bs4 import BeautifulSoup
import pandas as pd
# Sample HTML document
html_doc = """
<html>
<head><title>World's Population</title></head>
<body>
    <h1>Main Heading</h1>
    <p class="xyz">This is a paragraph.</p>
    <p class="content">Another paragraph with <a href="https://example.com">a link</a>.</p>

    <div id="container">
        <ul>
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>
    </div>

    <table>
        <tr><th>Name</th><th>Age</th></tr>
        <tr><td>Alice</td><td>25</td></tr>
        <tr><td>Bob</td><td>30</td></tr>
    </table>
</body>
</html>
"""
s= BeautifulSoup(html_doc, "html.parser")
x=s.find_all("tr")
name=[]
age=[]
td=s.find_all("td")
for i in td:
  if(i.text.isdigit()):
    age.append(i.text)
    !pip install bs4
from bs4 import BeautifulSoup
import pandas as pd
# Sample HTML document
html_doc = """
<html>
<head><title>World's Population</title></head>
<body>
    <h1>Main Heading</h1>
    <p class="xyz">This is a paragraph.</p>
    <p class="content">Another paragraph with <a href="https://example.com">a link</a>.</p>

    <div id="container">
        <ul>
            <li class="item">Item 1</li>
            <li class="item">Item 2</li>
            <li class="item">Item 3</li>
        </ul>
    </div>

    <table>
        <tr><th>Name</th><th>Age</th></tr>
        <tr><td>Alice</td><td>25</td></tr>
        <tr><td>Bob</td><td>30</td></tr>
    </table>
</body>
</html>
"""
s= BeautifulSoup(html_doc, "html.parser")
x=s.find_all("tr")
name=[]
age=[]
td=s.find_all("td")
for i in td:
  if(i.text.isdigit()):
    age.append(i.text)
   else:
    name.append(i.text)
di={}
di.update({'name':name})
di.update({'age':age})
print(pd.DataFrame(di))
