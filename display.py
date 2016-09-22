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
o1 = [255, 153, 51] #light orange
o2 = [255, 178, 102] #pale orange
o3 = [255, 204, 153] #peach/overwashed orange
ni = [0, 0, 0] #nothing

black = [0,0,0]

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


off = [
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
o2,ni,o1,o,ni,o3,ni,o2,
ni,o2,o1,o,ni,o3,o2,ni,
o3,o3,o2,o,o3,o2,o1,o1,
ni,ni,o3,o,o,o,o,o,
o,o,o,o,o,o3,ni,ni,
o1,o1,o2,o3,o,o2,o3,o3,
ni,o2,o3,ni,o,o1,o2,ni,
o2,ni,o3,ni,o,o1,ni,o2
]


load1 = [
o3,ni,o2,o1,ni,o,ni,o3,
ni,o3,o2,o1,ni,o,o3,ni,
o,o,o3,o2,o,o3,o2,o2,
ni,ni,o,o,o,o1,o1,o1,
o1,o1,o1,o,o,o,ni,ni,
o2,o2,o3,o,o1,o3,o,o,
ni,o3,o,ni,o1,o2,o3,ni,
o3,ni,o,ni,o1,o2,ni,o3
]


load2 = [
o,ni,o3,o2,ni,o1,ni,o,
ni,o,o3,o2,ni,o1,o,ni,
o1,o1,o,o2,o1,o,o3,o3,
ni,ni,o1,o,o,o2,o2,o2,
o2,o2,o2,o,o,o1,ni,ni,
o3,o3,o,o1,o2,o,o1,o1,
ni,o,o1,ni,o2,o3,o,ni,
o,ni,o1,ni,o2,o3,ni,o
]

load3 = [
o1,ni,o,o3,ni,o2,ni,o1,
ni,o1,o,o3,ni,o2,o1,ni,
o2,o2,o1,o,o2,o1,o,o,
ni,ni,o2,o,o,o,o3,o3,
o3,o3,o,o,o,o2,ni,ni,
o,o,o1,o2,o,o1,o2,o2,
ni,o1,o2,ni,o3,o,o1,ni,
o1,ni,o2,ni,o3,o,ni,o1
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
