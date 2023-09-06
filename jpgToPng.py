from PIL import Image
import os

oldDir = './ownTest'

c = 1

for img in os.listdir(oldDir):

    im = Image.open(os.path.join(oldDir, img)).convert('RGB')

    filename = os.path.join(oldDir, '{0:06d}.png'.format(c))
    print(filename)
    im.save(filename)
    c += 1
