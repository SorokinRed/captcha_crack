import imagehash
from PIL import Image
import os
chars = []
index = 0
for img_name in os.listdir('symbols'):
    
    img_path = 'symbols/' + img_name
    img = Image.open(img_path)
    img_hash = str(imagehash.phash(img))

    if img_hash in chars:
        if os.path.isdir('symbols_recognized/' + str(chars.index(img_hash))):
            os.rename(
                img_path,
                'symbols_recognized/' + str(chars.index(img_hash)) + '/' + img_name
            )
        else:
            os.mkdir('symbols_recognized/' + str(chars.index(img_hash)))
            os.rename(
                img_path,
                'symbols_recognized/' + str(chars.index(img_hash)) + '/' + img_name
            )
    else:
        chars.append(str(imagehash.phash(img)))
