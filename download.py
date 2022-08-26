from urllib.request import Request, urlopen
import re

print('start')

file1 = open('pages_full.txt', 'r')
Lines = file1.readlines()
  
count = 0
base_url = 'https://www.computerhope.com/unix/'
for line in Lines:
    count += 1
    print("Line{}: {} ".format(count, line.strip()))
    file_name = line.strip()
    url = base_url + file_name
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read().decode('utf8')
    text = re.sub('<head>.*?</head>', '', webpage, flags=re.DOTALL)
    # text = re.sub('<div class="skip"><a href=.*?<div class="container content" id="main-content" role="main">', '', text, flags=re.DOTALL)
    # text = re.sub('</article>.*?</html>', '', text, flags=re.DOTALL)
    open('C:\Python\PythonDownloadHTML\PythonDownloadHTML\command_files\\' + file_name, 'w').write(text)
    #open('C:\Python\DounloadHTMLDocument\\' + file_name, 'w').write(text)
print('end')
