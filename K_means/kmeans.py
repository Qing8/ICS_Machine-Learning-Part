# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:36:11 2015

@author: zhengzhang
"""

import random
import util
import cluster_student as cluster

def kmeans_iter(samples, clusters, k):
    '''
        implement one iteration of kmeans:
        - each sample finds the closest cluster by computing
          its distance to the centroids of all the clusters
        - then compute every cluster's new centroid
        - the algorithm converges if cluster's centroid does not
          move any more
    '''
    
    #Create a list containing k distinct empty lists
    
    newClusters = []
    for i in range(k):
        newClusters.append([])
    
    #Associate each sample with closest centroid
    for e in samples:
        #Find the centroid closest to e
        smallestDistance = e.distance(clusters[0].getCentroid())
        index = 0
        for i in range(1, k):
            distance = e.distance(clusters[i].getCentroid())
            if distance < smallestDistance:
                smallestDistance = distance
                index = i
        #Add e to the list of samples for the appropriate cluster
        newClusters[index].append(e)
        
    #Update each cluster; check if a centroid has changed
    converged = True
    for i in range(len(clusters)):
        if clusters[i].update(newClusters[i]) > 0.0:
            converged = False
    return converged
    
# Kmeans: take a list of samples and make k clusters
def kmeans(samples, k, verbose):
    """Assumes samples is a list of samples of class Sample,
         k is a positive int, verbose is a Boolean
       Returns a list containing k clusters. """
       
    #Get k randomly chosen initial centroids
    initialCentroids = random.sample(samples, k)
    
    #Create a singleton cluster for each centroid
    clusters = []
    for e in initialCentroids:
        clusters.append(cluster.Cluster([e]))
        
    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        
        numIterations += 1

        # replace the following line by implementing
        # kmeans_iter(samples, clusters, k) in this file
        converged = kmeans_iter(samples, clusters, k)

        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('\n') #add blank line
    return clusters
    
# one run of kmeans, like:
# kmeansTest(4, False)
def kmeansTest(k=2, n=20, verbose=False):
    random.seed(0)
    xMean = 3
    xSD = 1
    yMean = 5
    ySD = 1
    
    d1Samples = util.genDistribution(xMean, xSD, yMean, ySD, n, '1.')
    d2Samples = util.genDistribution(xMean+3, xSD, yMean+1, ySD, n, '2.')
    allSamples = d1Samples + d2Samples
    
    print("before clustering")
    util.plot_cluster([cluster.Cluster(allSamples)])
    
    print("after clustering")
    clusters = kmeans(allSamples, k, verbose)
    util.plot_cluster(clusters, verbose)
    
    print('Final result')
    for c in clusters:
        print('', c)    

if __name__ == "__main__":
    random.seed(0)
    kmeansTest(k=5)