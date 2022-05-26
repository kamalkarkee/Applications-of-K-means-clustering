#kamal karkidholi
#1001514809

import numpy as np
import random
import sys

def main():
    fileName = sys.argv[1]
    k = int(sys.argv[2])
    iteration = int(sys.argv[3])

    # read the given txt file
    lines = open(fileName, 'r')
    attributes = []
    classLabels = []
    # seperates attributes and class_label
    try:
        for line in lines:
            line = line.rstrip('\n')
            line = line.rstrip('\r')
            tokens = line.split()
            attribute = []
            for column in range(len(tokens)):
                if column is len(tokens) - 1:
                    classLabels.append(float(tokens[column]))
                else:
                    attribute.append(float(tokens[column]))
            attributes.append(attribute)
    finally:
        lines.close()
    # pick k centroids randomly
    As = np.array(attributes)
    centroid = []
    for i in range(k):
        randomSample = random.randint(0, len(As))
        centroid.append(As[randomSample])
    centroid = np.array(centroid)
    # create empty cluster
    cluster = {i:[] for i in range(k)}
    # fill cluster
    for i in range(len(As)):
        minimumDistance = float('inf')
        minimumCenter = 0
        for j in range(len(centroid)):
            euclideanDistance = np.linalg.norm(As[i] - centroid[j])
            if euclideanDistance <= minimumDistance:
                minimumDistance = euclideanDistance
                minimumCenter = j
        cluster[minimumCenter].append(As[i])
    # initialization error
    iError = 0
    for i in cluster.keys():
        for j in cluster[i]:
            iError += np.linalg.norm(j - centroid[i])
    print("After initialization error = %.4f" % (iError))
    # k-means clustering
    for i in range(iteration):
        # find mean centroid
        meanCentroid = [np.mean(cluster[j], axis=0) for j in cluster.keys()]
        # measure error
        error = 0
        for j in cluster.keys():
            for k in cluster[j]:
                error += np.linalg.norm(k - meanCentroid[j])
        # print error in defined format
        print("After iteration %d: error = %.4f" % (i+1, error))
        # recluster dataset
        newCluster = {j:[] for j in range(len(meanCentroid))}
        for j in range(len(attributes)):
            minimumDistance = float('inf')
            minimumCenter = 0
            for k in range(len(meanCentroid)):
                euclideanDistance = np.linalg.norm(attributes[j] - meanCentroid[k])
                if euclideanDistance <= minimumDistance:
                    minimumDistance = euclideanDistance
                    minimumCenter = k
            newCluster[minimumCenter].append(attributes[j])
        cluster = newCluster


if __name__ == "__main__":
    main()
