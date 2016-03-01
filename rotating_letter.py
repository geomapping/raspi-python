from sense_hat import SenseHat

sense = SenseHat()

e=[0,0,0]
w=[150,150,150]

image=[
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,w,w,w,w,w,e,
w,w,w,w,w,w,w,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
]






sense.set_pixels(image)







while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = round(x, 0)
    y = round(y, 0)

    if x == -1:
        sense.set_rotation(180)
    elif y == 1:
        sense.set_rotation(90)
    elif y == -1:
        sense.set_rotation(270)
    else:
        sense.set_rotation(0)
