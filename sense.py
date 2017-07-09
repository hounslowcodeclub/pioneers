#!/bin/python3

from sense_hat import SenseHat



sense = SenseHat()
sense.clear()

R = [255 ,0 , 0]

sense.clear(R)

O = [255 , 165 , 0]
sense.clear(O)

Y = [255,  255 , 0]
sense.clear(Y)
G = [0 , 128, 0]
sense.clear(G)
B = [0 , 0 , 255]
sense.clear(B)
I = [75,0,130]
sense.clear(I)
V = [238 ,130 ,238]
sense.clear(V)
W = [255 ,255 ,255]
sense.clear(W)
X = [0,0,0]

sense.clear(X)

rainbow = [
R, R, R, R, R, R, R, R,
R, O, O, O, O, O, O, O,
R, O, Y, Y, Y, Y, Y, Y,
R, O, Y, G, G, G, G, G,
R, O, Y, G, B, B, B, B,
R, O, Y, G, B, I, I, I,
R, O, Y, G, B, I, V, V,                                                                   
R, O, Y, G, B, I, V, X
]
sense.set_pixels(rainbow)

sunny = [
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,
Y, Y, Y, Y, Y, Y, Y, Y,

  ]
sense.set_pixels(sunny)

rainy = [
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,  
I, I, I, I, I, I, I ,I,  
  ]
sense.set_pixels(rainy)

snowy = [
B ,B ,B ,B ,B ,B ,B ,B , 
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
B ,B ,B ,B ,B ,B ,B ,B ,
  
   ]
sense.set_pixels(snowy) 

nice = [
G ,G ,G ,G ,G ,G ,G ,G ,  
G ,G ,G ,G ,G ,G ,G ,G ,
G ,G ,G ,G ,G ,G ,G ,G , 
G ,G ,G ,G ,G ,G ,G ,G , 
G ,G ,G ,G ,G ,G ,G ,G , 
G ,G ,G ,G ,G ,G ,G ,G , 
G ,G ,G ,G ,G ,G ,G ,G , 
G ,G ,G ,G ,G ,G ,G ,G , 

  ]
sense.set_pixels(nice)

dry = [
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
W ,W ,W ,W ,W ,W ,W ,W ,
  ]
sense.set_pixels(dry)
while True:
  if sense.humidity > 80 and sense.temp > 20:
     sense.set_pixels(rainbow)
  elif sense.humidity < 50 and sense.temp > 20 :
      sense.set_pixels(sunny)
  elif sense.humidity > 50 and sense.temp  > 16 :
       sense.set_pixels(nice)
  elif sense.humidity < 40 and sense.temp > 10 :
       sense.set_pixels(dry)
       
  elif sense.humidity > 90 and sense.temp < 10 :
      sense.set_pixels(rainy)
  elif sense.humidity > 100 and sense.temp <0 :
     sense.set_pixels(snowy)
  else :
     sense.clear()
     
     
