from keras.utils import load_img, img_to_array, array_to_img
import matplotlib.pyplot as plt

largo, alto = 500, 500

file = 'Archivos\Archivos_Reyna\Foto1.jpg'
img = load_img(file, target_size=(largo, alto),color_mode="grayscale")

print(img.size)
print(img.mode)

plt.imshow(img, cmap="gray")
plt.show()

stride = 3 # 2 x 2

img_max_pooling = []
for filas in range (1, alto - 1 -stride, stride):
    new_fila = []
    for columnas in range(1, largo -1 -stride, stride):
        for f_kernel in range(stride):
            for c_kernel in range(stride):
                pixel = img_array[filas + f_kernel][columnas + c_kernel][0]
                if pixel > max_pixel:
                    max_pixel = pixel
        new_fila.append([max_pixel])
    img_max_pooling.append(new_fila)

img = array_to_img(img_max_pooling)
print(img.size)
img.show()