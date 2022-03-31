from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<html>
    <head></head>
    <body>
        <h1>This is a title</h1>
        <p class="subtitle" >This is a paragraph.</p>
        <p >This is another paragraph without a class.</p>
        <ul>
            <li>Roses are red</li>
            <li>Violets are blue</li>
            <li>Sugar is sweet</li>
            <li>And so are you</li>
        </ul>
    </body>
</hmml>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')
def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)

def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [e.string for e in list_items]
    print(list_contents)
        
def find_subtitle():
    paragraph = simple_soup.find('p', class_='subtitle')
    print(paragraph.string)
    
def find_other_paragraph():
    paragraphs =  simple_soup.find_all('p')
    other_paragrahph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
    print(other_paragrahph[0].string)


find_other_paragraph()
find_list_items()