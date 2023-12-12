from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("Minimum temperature").getOrCreate()

schema_1800 = StructType([
    StructField("stationID", StringType()),
    StructField("date", IntegerType()),
    StructField("type", StringType()),
    StructField("temp", FloatType()),
    StructField("other", StringType()),
    StructField("other1", StringType()),
    StructField("other2", StringType()),
])

lines = spark.read.format('csv').schema(schema_1800).load("1800.csv")

#lines.show()

lines.createOrReplaceTempView("temps")

t_mins = spark.sql("SELECT stationID, MIN(temp) FROM temps WHERE type = 'TMIN' GROUP BY stationID")

results = t_mins.collect()

for result in results:
    print(result[0] + '\t' + str(float(result[1])/10.0))

spark.stop()