import random
import math
import csv
import random
lst = []
with open('studyhoursdb.csv','r') as f:
    reader = csv.reader(f,delimiter = ' ')
    for row in reader:
        lst.append([int(row[0]),int(row[1])])
    f.close()
compr_h = [0,0]
compr_l = [1000,1000]
lowest = 0
highest = 0
print lst
for index in range(0,len(lst)):
    x,y = lst[index][0],lst[index][1]
    if x >= compr_h[0] and y >= compr_h[1]:
        compr_h,highest = [x,y],index
    elif compr_l[0]>=x and  compr_l[1]>= y:
        compr_l[0],compr_l[1],lowest = x,y,index
NUM_CLUSTERS = 4
TOTAL_DATA = len(lst)
LOWEST_SAMPLE_POINT = lowest#element 0 of SAMPLES.
HIGHEST_SAMPLE_POINT = highest #element 3 of SAMPLES.
BIG_NUMBER = math.pow(20, 10)

HIGH_MID_SAMPLE_POINT = random.randint(0,len(lst)-1)
LOW_MID_SAMPLE_POINT = random.randint(0,len(lst)-1)
print HIGHEST_SAMPLE_POINT

SAMPLES = lst
data = []
centroids = []

class DataPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_x(self, x):
        self.x = x
    def get_x(self):
        return self.x
    def set_y(self, y):
        self.y = y
    def get_y(self):
        return self.y
    def set_cluster(self, clusterNumber):
        self.clusterNumber = clusterNumber
    def get_cluster(self):
        return self.clusterNumber

class Centroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_x(self, x):
        self.x = x
    def get_x(self):
        return self.x
    def set_y(self, y):
        self.y = y
    def get_y(self):
        return self.y

def initialize_centroids():
    # Set the centoid coordinates to match the data points furthest from each other.
    # In this example, (1.0, 1.0) and (5.0, 7.0)
    centroids.append(Centroid(SAMPLES[LOWEST_SAMPLE_POINT][0], SAMPLES[LOWEST_SAMPLE_POINT][1]))
    centroids.append(Centroid(SAMPLES[LOW_MID_SAMPLE_POINT][0], SAMPLES[LOW_MID_SAMPLE_POINT][1]))
    centroids.append(Centroid(SAMPLES[HIGH_MID_SAMPLE_POINT][0], SAMPLES[HIGH_MID_SAMPLE_POINT][1]))
    centroids.append(Centroid(SAMPLES[HIGHEST_SAMPLE_POINT][0], SAMPLES[HIGHEST_SAMPLE_POINT][1]))
    print "Centroids initialized at:"
    print "(", centroids[0].get_x(), ", ", centroids[0].get_y(), ")",'\n'
    print "(", centroids[1].get_x(), ", ", centroids[1].get_y(), ")","\n"
    print "(", centroids[2].get_x(), ", ", centroids[2].get_y(), ")","\n"
    print "(", centroids[3].get_x(), ", ", centroids[3].get_y(), ")","\n"
    return

def initialize_datapoints():
    # DataPoint objects' x and y values are taken from the SAMPLE array.
    # The DataPoints associated with LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT are initially
    # assigned to the clusters matching the LOWEST_SAMPLE_POINT and HIGHEST_SAMPLE_POINT centroids.
    for i in range(TOTAL_DATA):
        newPoint = DataPoint(SAMPLES[i][0], SAMPLES[i][1])
        
        if(i == LOWEST_SAMPLE_POINT):
            newPoint.set_cluster(0)
        elif(i == LOW_MID_SAMPLE_POINT):
            newPoint.set_cluster(1)
        elif(i == HIGH_MID_SAMPLE_POINT):
            newPoint.set_cluster(2)
        elif(i == HIGHEST_SAMPLE_POINT):
            newPoint.set_cluster(3)
        else:
            newPoint.set_cluster(None)
        data.append(newPoint)
    return

def get_distance(dataPointX, dataPointY, centroidX, centroidY):
    # Calculate Euclidean distance.
    return math.sqrt(math.pow((centroidY - dataPointY), 2) + math.pow((centroidX - dataPointX), 2))

def recalculate_centroids():
    totalX = 0
    totalY = 0
    totalInCluster = 0
    for j in range(NUM_CLUSTERS):
        for k in range(len(data)):
            if(data[k].get_cluster() == j):
                totalX += data[k].get_x()
                totalY += data[k].get_y()
                totalInCluster += 1
        if(totalInCluster > 0):
            centroids[j].set_x(totalX / totalInCluster)
            centroids[j].set_y(totalY / totalInCluster)
    return

def update_clusters():
    isStillMoving = 0
    for i in range(TOTAL_DATA):
        bestMinimum = BIG_NUMBER
        currentCluster = 0
        for j in range(NUM_CLUSTERS):
            distance = get_distance(data[i].get_x(), data[i].get_y(), centroids[j].get_x(), centroids[j].get_y())
            if(distance < bestMinimum):
                bestMinimum = distance
                currentCluster = j
        data[i].set_cluster(currentCluster)
        if(data[i].get_cluster() is None or data[i].get_cluster() != currentCluster):
            data[i].set_cluster(currentCluster)
            isStillMoving = 1
    
    return isStillMoving

def perform_kmeans():
    isStillMoving = 1
    initialize_centroids()
    initialize_datapoints()
    while(isStillMoving):
        recalculate_centroids()
        isStillMoving = update_clusters()   
    return

def print_results():
    for i in range(NUM_CLUSTERS):
        print "Cluster ",i, " includes:"
        for j in range(TOTAL_DATA):
            if(data[j].get_cluster() == i):
                print "(", data[j].get_x(), ", ", data[j].get_y(), ")"
        print()
    return
perform_kmeans()
print_results()