from cassandra.cluster import Cluster

cluster = Cluster(['n1', 'n2'])
session = cluster.connect('easytally')



