import urllib.request
import numpy as np
import cv2
import matplotlib.pyplot as plt

url = "https://commons.wikimedia.org/wiki/Special:FilePath/Lemon_-_whole_and_split.jpg?width=800"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
dane = urllib.request.urlopen(req).read()
img = cv2.imdecode(np.frombuffer(dane, np.uint8), cv2.IMREAD_COLOR)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Oryginał")
plt.axis("off")
plt.show()

img = cv2.resize(img, None, fx=0.5, fy=0.5)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

plt.imshow(img, cmap="gray")
plt.title("Wynik")
plt.axis("off")
plt.show()

print(img.shape)
print(img)