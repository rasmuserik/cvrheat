import gzip
import array
import math 

minLng = 8.08350793029
maxLng = 15.1518718625
minLat = 54.568810953
maxLat = 57.7410936803

def findBoundary():
  print "finding boundary"
  for line in gzip.open("companies-sorted-by-registration.gz"):
    field = line.split(" ")
    if field[2] == "":
      continue
    lng = float(field[3])
    lat = float(field[2])
    if lng < minLng:
      minLng = lng
    if lng > maxLng:
      maxLng = lng
    if lat < minLat:
      minLat = lat
    if lat > maxLat:
      maxLat = lat
  print minLng, maxLng, minLat, maxLat

width = 1366
height = 768
width = 300
height = 200
width = 1500
height = 2500
canvas = [0]*width*height
maxLat *= 1.01
maxLng *= 1.01

dLng = maxLng - minLng
dLat = maxLng - minLng
for line in gzip.open("companies-sorted-by-registration.gz"):
    field = line.split(" ")
    if field[2] == "":
      continue
    lng = float(field[3])
    lat = float(field[2])
    x = int((lng - minLng)/dLng*width)
    y = int((1-(lat - minLat)/dLat)*height)
    canvas[x + y * width] += 1
canvas = map(lambda x: math.log (x + 1), canvas)
canvasMax = max(canvas)
canvas = map(lambda x: str(int(math.floor(255.999 * (x / canvasMax)))), canvas)
print "P2"
print width, height
print 255
for i in range(0, width*height, width):
  print " ".join(canvas[i:i+width])


