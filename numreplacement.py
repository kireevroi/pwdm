#just trying to clear text of punctuation and numbers

import string
with open('data\worddtb.txt', 'r') as f:
    data = f.read()
    data = data.translate(str.maketrans('', '', string.punctuation + string.digits))
with open('data\worddtb.txt', 'w') as f:
    f.write(data)
