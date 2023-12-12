from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Word Frequency")

# Load the input file
lines = sc.textFile("Book")

words = lines.flatMap(lambda line: line.split(" "))

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

sortedWordCounts = wordCounts.sortBy(lambda x: x[1], ascending=False)

print(sortedWordCounts.collect())

# Stop the SparkContext
sc.stop()
