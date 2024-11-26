import time
import vlc

x=int(input("How long? in minutes\n\a"))
total_time=60*x
left_time=total_time
min=x-1
print(f"{x}::00")
time.sleep(1)

for i in range(1,total_time):	
    left_time=total_time-i
    if left_time%60==0:
        min-=1
    print(f"{min}::{left_time%60}")
    time.sleep(1)



sound=vlc.MediaPlayer("sound1.wav")
sound.play()

time.sleep(2)
