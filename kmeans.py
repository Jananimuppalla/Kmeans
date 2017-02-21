from __future__ import division
import random
import math
import csv
import sys

# All Work herein is solely mine

cluster1={}
global centroid_list
centroid_list =[]
distance_list=list()
new_centroid=list()
new_sum=list()
prev_centroid=list()


#distance between two points (euclidean)
def euclidean_dist(centroid_1,alist):
    final_dist = 0.0
    dist=0
    for j in range(1,len(alist)):
        dist=dist+math.pow((centroid_1[j]-alist[j]),2)
        final_dist=math.sqrt(dist)
    return final_dist

#K means implementation
def kmeans(nc,Patient_list,t):
    global centroid_list
    while True:
        if not centroid_list:
            for i in range(0,nc):
                centroid_list.append(random.choice(Patient_list))
        for i in range(0,len(Patient_list)-1):
            distance_list=[]
            for j in range(0,len(centroid_list)):
                dist=euclidean_dist(centroid_list[j],Patient_list[i])
                distance_list.append(dist)
            min_ind=distance_list.index(min(distance_list))
            if min_ind in cluster1.keys():
                cluster1[min_ind].append(Patient_list[i])
            else:
                cluster1[min_ind]= [Patient_list[i]]
        # Recomputing centroids
        new_centroid = []
        for k in range(0,nc):
            sum1 = list(map(sum,zip(*cluster1[k])))
            new_centroid.append([x /len(cluster1[k]) for x in sum1])
        #print new_centroid
        # comparison of old centroid with new centroid
        d1=0
        for i in range(0,len(new_centroid)):
            d1=d1+euclidean_dist(new_centroid[i],centroid_list[i])
        #print d1

        centroid_list=list(new_centroid)
        if d1<t:
            print('Kmeans is completed')
            break
        else:
            cluster1.clear()


def caluculateError():
    totalError = 0
    for i in range(0,nc):
        benignCount = 0
        malignCount = 0
        for eachRecord in cluster1[i]:
            if eachRecord[-1] == 2:
                benignCount = benignCount +1
            else:
                malignCount = malignCount + 1
        if benignCount > malignCount:
            totalError = totalError + malignCount/(malignCount + benignCount)
        else:
            totalError = totalError + benignCount/(malignCount + benignCount)
    print "total Error Rate :" , totalError




if __name__ == "__main__":
    with open('clean2.csv', 'rb') as BreastCancer:
        reader = csv.reader(BreastCancer,)
        Patient_list = list(reader)
        Patient_list=[ [int(y) for y in x] for x in Patient_list]
        #Patient_list = Patient_list[:30]
        print len(Patient_list)
    print("Enter the number of clusters")
    nc=int(input())
    print("Enter the treshold")
    t=float(input())
    kmeans(nc,Patient_list,t)
    caluculateError()



















