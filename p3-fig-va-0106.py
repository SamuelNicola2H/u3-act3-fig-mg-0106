import numpy as np
import pandas as pd
import matplotlib .pyplot as plt
import cv2 
# Samuel Nicola NC 0106
print("Smuel Nicola NC 0106")
print("UIII Act3 colocar puntos a una imagen  en blanco y negro VA")
mi_imagen = cv2.imread("DonRamon B y N.jpg")
plt.imshow(mi_imagen)
plt.title("Don Ramon B y N y Samuel Nicola NC 0106")
plt.show()
print("-+-+-+- puntos en la imagen -+-+-+-")
plt.imshow(mi_imagen)
x = [100,100,300, 300]
y = [100,400,500, 300]
plt.scatter(x,y, s = 20,c="red")
plt.show()
print("-+-+-+- cuadro azul en la imagen -+-+-+-")
img_DonRamon = cv2.imread("DonRamon B y N.jpg")
plt.imshow(img_DonRamon)
x = [100,100,300, 300,100]
y = [500,100,100, 500,500]
plt.plot(x,y, c ="blue")
plt.show()
print("-+-+-+- circulo verde en la imagen -+-+-+-")
I = cv2.imread("DonRamon B y N.jpg")
plt.imshow(I)
N = 30 # Lados de el poligono
x = np.zeros((N+1,))
y = np.zeros((N+1,))
(xc,yc) = (340,320)
r = 150 # radio
for i in range(N+1):
  t   = 2*np.pi/N*i
  x[i] = xc + r*np.cos(t)
  y[i] = yc + r*np.sin(t)
plt.plot(x, y, c="green")
plt.show()