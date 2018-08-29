"""
A Spark implementation of the PageRank algorithm
"""
import findspark
findspark.init('/Users/darrenmooney/Desktop/learn_spark/spark-2.3.1-bin-hadoop2.7')
import pyspark


def page_rank(use_partitioning=True):
    conf = pyspark.SparkConf()
    conf = conf.setMaster('local[*]')
    sc = pyspark.SparkContext(appName="PageRank", conf=conf)

    # Get url data from text file.
    # Paired RDD of form {0001:[0002, 0003]: 0002: ...}
    if use_partitioning:
        links = sc.textFile('urls_pagerank.txt')\
            .map(lambda x: (x.split('\t')[0], x.split('\t')[1:])).partitionBy(100).persist()
    else:
        links = sc.textFile('urls_pagerank.txt')\
            .map(lambda x: (x.split('\t')[0], x.split('\t')[1:]))

    # Initialise ranks, e.g. {0001: 1.0, 0002: 0.1, ...}
    # mapValues must be used to leave keys untouched and preserve partitioning
    ranks = links.mapValues(lambda x: 1.0)

    for _ in range(100):

        # 1. Creates a single RDD with links and ranks for each url
        # 2. FlatMaps each line to another paired RDD keyed by each link in list of links with their contribution
        # 3. Reduces this by key, summing and weightin contribution
        contributions = links.join(ranks).flatMap(lambda (page_id, (_links, rank)): map(lambda dest: (dest, rank / len(_links)), _links))
        ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda v: 0.15 + 0.85*v)

    sc.stop()

page_rank(False)
