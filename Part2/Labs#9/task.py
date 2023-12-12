from pyspark.sql import SparkSession, Row

spark = SparkSession.builder.appName("Word Frequency").getOrCreate()

lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

#read from the lines socket
words = lines.selectExpr("explode(split(value, ' ')) as word")

query = words.writeStream.outputMode("complete").format("console").queryName("count_words").start()

query.awaitTermination()

spark.stop()


#print(words)

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

sortedWordCounts = wordCounts.sortBy(lambda x: x[1], ascending=False)

print(sortedWordCounts.collect())

# Stop the SparkContext
spark.stop()