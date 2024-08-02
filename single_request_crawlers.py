import urllib.request

def get_html(url):
    f=open('htmlcode.txt','w')
    page=urllib.request.urlopen(url)
    web_byte =page.read() ## Save the html and later save in the file
    pagetext = web_byte.decode('utf-8')
    f.write(pagetext)
    f.close()

req = urllib.request.Request(
    url="https://www.pirogov-center.ru/patient/hospital/department/ophthalmology/terms.php", 
    headers={'User-Agent': 'Mozilla/5.0'}
)

get_html(req)