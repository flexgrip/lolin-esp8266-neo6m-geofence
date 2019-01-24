# lolin-esp8266-neo6m-geofence
The arduino version of my geofence project.

Just pushing up the arduino version of my sketch. This should fire off buzzers when inside the bounding box. Yes, I know its a cheap method of handling bounding boxes in arduino. I'm sure there's a better one. But this ain't 
micropython and I wanted it done quick :)

You'll need software serial. It works ok with hardware serial if you get the baud rates right. But on these Lolin nodemcu chips, they're kinda finicky. This is pretty much based on all of the great work done on TinyGPS++. Speaking 
of that, you'll need that too.
