from pyspark import SparkContext

sc = SparkContext("local", "Word Frequency")

lines = sc.textFile("Book")

words = lines.flatMap(lambda line: line.split(" ")).filter(lambda x: len(x) > 0)

wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a+b)

sortedWordCounts = wordCounts.sortBy(lambda x: x[1], ascending=False)

res = sortedWordCounts.collect()

print("\n\nTop 10 words:")

for k,v in res[:10]:
    print(k + ' : ' + str(v))

print("\n\n")
sc.stop()
