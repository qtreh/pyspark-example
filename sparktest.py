from pyspark import SparkContext, SparkConf

# Spark initialization
conf = SparkConf().setAppName("appName")
sc = SparkContext(conf=conf)

# Better than wordcount: wordavg
dico = sc.textFile("linuxwords.txt")
mapped = dico.map(lambda s: (len(s),1))
reduced = mapped.reduce(lambda x, y: (x[0] + y[0], x[1] + y[1])) # (total length, nb lines)
avgWordLen = reduced[0] / float(reduced[1])
print "\nAverage length of words in dictionary: {0:.2f}\n".format(avgWordLen)

# Create a RDD, save it on disk, reuse it
rdd = sc.parallelize(range(1, 4)).map(lambda x: (x, "a" * x ))
rddSaved = rdd.saveAsSequenceFile("filefilefile")
collected = sorted(sc.sequenceFile("filefilefile").collect())
print(collected)
