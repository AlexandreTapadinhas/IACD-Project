from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, length

# Create a Spark session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Read the input file into a DataFrame
book_df = spark.read.text("Book")

word_df = book_df.select(explode(split(book_df.value, ' ')).alias('word')).filter(length('word') > 0)

# Register the DataFrame as a temporary table
word_df.createOrReplaceTempView("words")

# Perform the word count using Spark SQL
word_count_df = spark.sql("""
    SELECT word, COUNT(*) as count
    FROM words
    GROUP BY word
    ORDER BY count DESC
""")

# Show the result
word_count_df.show()

# Stop the Spark session
spark.stop()
