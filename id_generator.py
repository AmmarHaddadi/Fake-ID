import requests
import os
from faker import Faker


def download(fileName):
    with open(fileName, 'wb') as f:
        f.write(requests.get('https://thispersondoesnotexist.com/image',
                             headers={'User-Agent': 'My User Agent 1.0'}).content)


desktop = "C:\\Users\\" + str(os.getlogin()) + "\\Desktop\\"

try:
    os.mkdir(desktop + 'Faked ID')
    os.chdir(desktop + 'Faked ID')
except Exception:
    print("can't make folder in desktop")
    exit()

try:
    download('fakeperson.jpg')
except Exception:
    print("can't download a fake profile :( maybe ur not connected to internet \f u can try manually at https://thispersondoesnotexist.com")


fake = Faker()

p = fake.profile()

with open('id.txt', 'w') as f:
    for a, b in p.items():
        f.write(str(a) + ' : ' + str(b))
        f.write('\n')


print("check faked_ID on your desktop :) \nbased on joke2k's library ")
