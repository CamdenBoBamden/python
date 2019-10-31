import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd

contact =[]
states = ["ak", "al", "ar", "az", "ca", "co", "ct",  
    "de", "fl", "ga", "ia", "id", "il", "in", "ks", "ky", "la",  
    "ma", "md", "me", "mi", "mn", "mo", "ms", "mt", "nc", "nd", "ne",  
    "nh", "nj", "nm", "nv", "ny", "oh", "ok", "or", "pa", "ri", "sc",  
    "sd", "tn", "tx", "ut", "va", "vt", "wa", "wi", "wv"]

print("Starting...")
for i in states:
    print("Starting state "+i+".")
    page = requests.get('http://www.framelink.net/directory/'+i+'.html')
    soup = BeautifulSoup(page.content, 'html.parser')

    phone = soup.findAll('td')

    batch = []
    group = [] 
    _call = []
    _line_in_group = []
    
    #This line converts everything to text
    for i in phone:
        x = i.text
        x= ''.join(x.strip())
        x= x.replace("-", " ").replace("  ",",").replace("\t", "").replace(",,","")
        x= x.splitlines()
        x = ' '.join(x)    
        batch += [x]

    #This finds phone in the text and saves the value of the amount of characters at the location of "Phone"
    for i in batch:
        num = i.find("Phone")
        group += [num]
    #This section isolates the item in the array that has "Phone" in the text
    for i in group:
        if i >1:     
            _call += [i] 
    #This section gets the index location of that length of characters from group and saves it to line in group which is index location of "Phone"
    for i in _call:
        location = (group.index(i))
        _line_in_group += [location]
    #This section looks up the location in the text document and saves it to a new array called SP
    for i in _line_in_group:
        SP = (batch[i])
        contact += [SP]
        print(len(contact))

print(len(contact))
#print(contact[1])

contact = list(dict.fromkeys(contact) )
ds = pd.Series(contact)
df=pd.DataFrame(ds)
writer = pd.ExcelWriter('tes.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()
