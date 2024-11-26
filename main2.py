import time
import vlc
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description="Countdown time")
parser.add_argument(
    "time_in_min",
    type=int,
    nargs="?",
    help="Duration of the timer in minutes"
)
args = parser.parse_args()



if args.time_in_min is not None:
	x=abs(args.time_in_min)

else:
	 x=abs(input("How long ? In minutes \n\a"))

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
