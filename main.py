from bs4 import BeautifulSoup
# import lxml Can use this and then insert lxml as the parser insteadl of html.parser for sites where oyu get a parser error

with open(file="website.html") as site:
    contents = site.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title) #Will output the title element with text, but using soup.title.name will output only the tag name (e.g. "title"). Can also use .string to get the content of the element.

all_anchor_tags = soup.find_all(name="a") # Find all <a tags or change to p for <p tags

for tags in all_anchor_tags:
    tags.getText() #To isolate all text
    tags.get("href") #To isolate the content of a specific function

#USE find to search first matching element
#USE find_all to search all matching elements

section_heading = soup.find(name="h3", class_ = "heading")
print(section_heading.text)
print(section_heading.name)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a") #a item inside a paragraph
print(company_url)