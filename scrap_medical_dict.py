from bs4 import BeautifulSoup


html_doc = "/home/temduck/crawlers/htmlcode.html"
with open(html_doc, "r") as fp:
    soup = BeautifulSoup(fp)

article_text  = soup.find("div", attrs={"class":"article-text"})
book = open("Словарь_медицинских_терминов.txt", "w")
for paragraph in article_text.find_all("p"):
    if paragraph.text and paragraph.next_sibling:
        book.write(paragraph.text.strip()+paragraph.next_sibling.strip()+"\n")
book.close()