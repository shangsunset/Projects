import time
from threading import Timer

def play_sound():

    for i in range(2):
        for n in range(3):
            print '\a'
            time.sleep(0.1)
        time.sleep(2)

def alarm(n):
    time_parts = n.split(':')
    hr = time_parts[0]
    minute = time_parts[1]
    sec = time_parts[2]

    wait_time = 360*int(hr) + 60*int(minute) + int(sec)
    print 'you are waiting for: ' , wait_time , 'seconds'
    t = Timer(wait_time, play_sound).start()
    for i in reversed(range(wait_time)):
        print i + 1
        time.sleep(1)

def main():
    wait_time = raw_input('set an alarm in format like this: h:m:s\n>> ')
    alarm(wait_time)


main()
