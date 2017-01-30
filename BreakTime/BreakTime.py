import webbrowser

import time

print "This program started on " + time.ctime()

totalBreaks = 3
count = 0
while count < totalBreaks:
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    count += 1
