#!/usr/bin/python
import math

locations = []

lineCount = 0
for line in open("locations.txt", "r"):
  if lineCount == 0:
    lineCount += 1
    continue
  vals = line.split("\t")

  locations.append(vals)

  lineCount += 1

print locations


distances = []
vectors = {}

for l1Count, l1 in enumerate(locations):
  for l2Count, l2 in enumerate(locations):
    if l1Count < l2Count:
      diffLat = float(l1[1]) - float(l2[1])
      diffLong = float(l1[2]) - float(l2[2])
      distance = math.sqrt(diffLat ** 2 + diffLong ** 2)
      vectors[1000 * l1Count + l2Count] = distance
      distances.append([distance, l1[0], l2[0]])

#print vectors
distances.sort()
print distances[0: 20]

