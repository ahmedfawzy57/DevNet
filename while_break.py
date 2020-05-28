from time import sleep
while True:
     try:
         print("Polling.")
         sleep(0.1)
     except KeyboardInterrupt:
            break   