from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, length


spark = SparkSession.builder.appName("WordCount").getOrCreate()


book_df = spark.read.text("Book")

word_df = book_df.select(explode(split(book_df.value, ' ')).alias('word')).filter(length('word') > 0)

word_df.createOrReplaceTempView("words")

word_count_df = spark.sql("""
    SELECT word, COUNT(*) as count
    FROM words
    GROUP BY word
    ORDER BY count DESC
""")

word_count_df.show()

spark.stop()
