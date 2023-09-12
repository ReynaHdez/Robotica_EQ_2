from keras.utils import load_img, img_to_array
import matplotlib.pyplot as plt

largo, alto = 500, 500
file = 'Archivos\Archivos_Reyna\Foto1.jpg'

img = load_img(file, target_size=(largo, alto),color_mode="grayscale")

print(img.size)
print(img.mode)

plt.imshow(img, cmap="gray")
plt.show()