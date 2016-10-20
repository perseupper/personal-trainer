from sense_hat import SenseHat
from time import sleep

# Added a comment

sense = SenseHat()

W = [255, 255, 255] #white
r = [255, 0, 0] #red
b = [0, 0, 255] #blue
g = [0, 255, 0] #green
y = [255, 255, 0] #yellow
n = [0, 0, 0] #nothing
p = [139, 15, 255] #perse purple
o = [255, 128, 0] #orange
m = [244, 66, 220]#magenta

plugin0 = [
n,n,n,n,n,n,n,n,
n,n,b,b,n,n,n,r,
n,b,b,b,b,b,n,r,
b,b,b,b,n,n,n,r,
n,b,b,b,b,b,n,r,
n,n,b,b,n,n,n,r,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n
]

plugin1 = [
n,n,n,n,n,n,n,n,
n,n,n,b,b,n,n,r,
n,n,b,b,b,b,b,r,
b,b,b,b,b,n,n,r,
n,n,b,b,b,b,b,r,
n,n,n,b,b,n,n,r,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n
]

plugin2 = [
n,n,n,n,n,n,n,n,
n,n,n,n,b,b,n,r,
n,n,n,b,b,b,b,r,
b,b,b,b,b,b,n,r,
n,n,n,b,b,b,b,r,
n,n,n,n,b,b,n,r,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n
]

plugin3 = [
n,n,n,n,n,n,n,n,
n,n,n,n,n,b,b,r,
n,n,n,n,b,b,b,r,
b,b,b,b,b,b,b,r,
n,n,n,n,b,b,b,r,
n,n,n,n,n,b,b,r,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n
]

plugin4 = [
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,g,
n,n,n,n,n,n,g,n,
n,n,n,n,n,g,n,n,
g,n,n,n,g,n,n,n,
n,g,n,g,n,n,n,n,
n,n,g,n,n,n,n,n,
n,n,n,n,n,n,n,n
]

plugin = [plugin0,plugin1,plugin2,plugin3,plugin4]

upload0 = [
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
b,n,n,n,n,n,n,n,
]

upload1 = [
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
b,b,n,n,n,n,n,n,
n,n,b,n,n,n,n,n,
b,n,b,n,n,n,n,n,
]

upload2 = [
n,m,n,n,n,n,n,n,
n,n,n,n,n,n,n,n,
b,b,n,n,n,n,n,n,
n,n,b,b,n,n,n,n,
n,n,n,n,b,n,n,n,
b,b,n,n,b,n,n,n,
n,n,b,n,n,b,n,n,
b,n,b,n,n,b,n,n
]

play = [
n,n,g,n,n,n,n,n,
n,n,g,g,n,n,n,n,
n,n,g,g,g,n,n,n,
n,n,g,g,g,g,n,n,
n,n,g,g,g,g,n,n,
n,n,g,g,g,n,n,n,
n,n,g,g,n,n,n,n,
n,n,g,n,n,n,n,n
]

pause = [
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n,
n,y,y,n,n,y,y,n
]


stop = [
n,n,n,n,n,n,n,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,r,r,r,r,r,r,n,
n,n,n,n,n,n,n,n
]


power = [
n,n,n,n,n,n,n,n,
n,n,n,r,r,n,n,n,
n,r,n,r,r,n,r,n,
r,n,n,r,r,n,n,r,
r,n,n,r,r,n,n,r,
r,n,n,r,r,n,n,r,
n,r,n,r,r,n,r,n,
n,n,r,r,r,r,n,n
]

charactermap = [
	[
	[n,b,n,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[b,n,b,n,],
	[n,b,n,n,],
	],
	[
	[n,b,n,n,],
	[b,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[n,b,n,n,],
	[b,b,b,n,],
	],
	[
	[n,b,n,n,],
	[b,n,b,n,],
	[n,n,b,n,],
	[n,b,n,n,],
	]
]

load0 = [
b,g,y,o,r,m,p,b,
p,r,y,o,r,m,g,g,
m,m,g,o,r,g,y,y,    
r,r,r,r,r,o,o,o,    
o,o,o,r,r,r,r,r,
y,y,g,r,o,g,m,m,
g,g,m,r,o,y,r,p,
b,p,m,r,o,y,g,b
]


load1 = [
p,b,g,y,o,r,m,p,
m,b,g,y,o,r,b,b,
r,r,b,y,r,b,g,g,
o,o,r,r,r,y,y,y,
y,y,y,r,r,r,o,o,
g,g,b,r,y,b,r,r,
b,b,r,o,y,g,b,m,
p,m,r,o,y,g,b,p
]


load2 = [
m,p,b,g,y,o,r,m,
r,r,b,g,y,o,r,p,
o,o,r,g,o,r,b,b,
y,y,o,r,r,g,g,g,
g,g,g,r,r,o,y,y,
b,b,r,o,g,r,o,o,
p,r,o,y,g,b,r,r,
m,r,o,y,g,b,p,m,
]

load3 = [
r,m,p,b,g,y,o,r,
o,r,p,b,g,y,r,m,
y,y,r,b,y,r,p,p,
g,g,y,r,r,b,b,b,
b,b,b,r,r,y,g,g,
p,p,r,y,b,r,y,y,
m,r,y,g,b,p,r,o,
r,o,y,g,b,p,m,r
]

load4 = [
o,r,m,p,b,g,y,o,
y,r,m,p,b,g,r,r,
g,g,r,p,g,r,m,m,
b,b,g,r,r,p,p,p,
p,p,p,r,r,g,b,b,
m,m,r,g,p,r,g,g,
r,r,g,b,p,m,r,y,
o,y,g,b,p,m,r,o
]

load5 = [
y,o,r,m,p,b,g,y,
g,o,r,m,p,b,o,o,
b,b,o,r,p,o,r,r,
p,p,p,r,r,r,m,m,
m,m,r,r,r,p,p,p,
r,r,o,p,r,o,b,b,
o,o,b,p,m,r,o,g,
y,g,b,p,m,r,o,y
]

load6 = [
g,y,o,r,m,p,b,g,
b,y,o,r,m,p,y,y,
p,p,y,r,m,y,o,o,
m,m,m,r,r,r,r,r,
r,r,r,r,r,m,m,m,
o,o,y,m,r,y,p,p,
y,y,p,m,r,o,y,b,
g,b,p,m,r,o,y,g
]


sense.set_pixels(play)
sleep(1)
sense.set_pixels(pause)
sleep(1)
sense.set_pixels(stop)
sleep(1)
sense.set_pixels(off)
sleep(1)

while True:
	sense.set_pixels(load0)
	sleep(0.1)	
	sense.set_pixels(load1)
	sleep(0.1)
	sense.set_pixels(load2)
	sleep(0.1)
	sense.set_pixels(load3)
	sleep(0.1)
    sense.set_pixels(load4)
    sleep(0.1)
    sense.set_pixels(load5)
    sleep(0.1)
    sense.set_pixels(load6)
