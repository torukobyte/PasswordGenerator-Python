import random

def generate():
    a = "1234567890"
    b = "qwertyuioasdfghjklzxcvbnm"
    c = ".,_-!?><#$^%/"
    d = "QWERTYUIOASDFGHJKLZXCVBNM"
    x = random.randint(7,15)
    list = []
    for i in range(x):
        y = random.choice(a+b+c+d)
        list.append(y)
        z = "".join(map(str,list)) #map fonksiyonu ile stringe çevirdik ve join ile aralarını boş bıraktık!
    return z