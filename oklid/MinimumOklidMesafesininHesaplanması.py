import math
points = [(2.2,3.0),(4.0,5.0),(1.1,4.2),(-1.1,0.0)]

def euclideanDistance (point1,point2):
    x1,y1 = point1
    x2,y2 = point2
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

distances = [] #mesafeleri saklayan boş liste
for i in range(len(points)):
    for j in range(i+1,len(points)):
        distance = euclideanDistance(points[i],points[j])
        distances.append(distance)
        #her bir nokta ççiftinin Öklid mesafesi
        print(f"Nokta çifti: {points[i]} ve {points[j]}, Mesafe: {distance}")

min_distance = min(distances)
print("Minimum mesafe:",float(min_distance) )