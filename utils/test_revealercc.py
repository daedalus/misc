#!/usr/bin/env python
# revealer.cc example
# author Dario Clavijo 2018

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

img0 = Image.open("examples/xor.png")
img1 = Image.open("examples/raw_noise.png")

data0 = np.array(img0, dtype="uint8")
data1 = np.array(img1, dtype="uint8")

y = data0 ^ data1
plt.imsave("/tmp/output.png", y, cmap=plt.cm.gray)
