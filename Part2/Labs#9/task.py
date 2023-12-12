import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("Word Frequency").getOrCreate()

lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

words = lines.select(
    explode(
        split(lines.value, " ")
    ).alias("word")
)

wordCounts = words.groupBy("word").count()

sortedWordCounts = wordCounts.orderBy(col("count").desc())

query = sortedWordCounts.writeStream.outputMode("complete").format("console").start()

query.awaitTermination()

spark.stop()