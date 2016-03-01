from sense_hat import SenseHat
sense = SenseHat()

while True:
    t = sense.get_temperature()
  
    t = round(t, 1)

    if t > 15 and t < 20:
        bg = [0, 100, 0]  # green
   
    if t > 20 and t < 25:
        bg = [70, 50, 50]  # orange
    
    if t > 25 and t < 30:
        bg = [100, 0, 0]  # red
        
      msg = "Temperature = %s"

    sense.show_message(msg, scroll_speeed=0.05,back_colour=bg)
