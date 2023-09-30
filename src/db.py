from cassandra.cluster import Cluster

cluster = Cluster(['node1', 'node2'])
session = cluster.connect('easytally')


