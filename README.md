# Applications-of-K-means-clustering

The first argument, <data_file>, is the path name of a file where the data is stored. The path name can specify any file stored on the local computer.
The second argument, <k>, specifies the number of clusters.
The third argument, <iterations>, specifies the number of iterations of the main loop. The
initialization stage (giving a random assignment of objects to clusters, and computing the means of those random assignments) does not count as an iteration.
  
Commands needed to compile:
python k_means_cluster.py <data_file> <k> <iterations>
Complete output for the following invocations of program: python k_means_cluster.py yeast_test.txt 2 5
Sample output:
After initialization error = 149.5775
After iteration 1: error = 111.6534 
After iteration 2: error = 110.9367
After iteration 3: error = 110.7002 
After iteration 4: error = 110.6002 
After iteration 5: error = 110.4996
  
python k_means_cluster.py yeast_test.txt 3 5 
Sample output:
After initialization error = 136.4980
After iteration 1: error = 109.6018
After iteration 2: error = 107.2850 After iteration 3: error = 106.6220 After iteration 4: error = 106.3141 After iteration 5: error = 106.0039
