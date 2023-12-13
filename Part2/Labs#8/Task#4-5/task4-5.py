from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import StructType, StructField, IntegerType, FloatType

spark = SparkSession.builder.appName("Minimum temperature").getOrCreate()

ShoppingStoreSchema = StructType([
    StructField("customerID", IntegerType()),
    StructField("productID", IntegerType()),
    StructField("amount", FloatType())
])

lines = spark.read.format('csv').schema(ShoppingStoreSchema).load("customer-orders.csv")

#lines.show()

lines.createOrReplaceTempView("purchases")

amounts = spark.sql("""
                    SELECT 
                        customerID, 
                        SUM(amount) as sum 
                    FROM purchases 
                    GROUP BY customerID 
                    ORDER BY SUM(amount) DESC LIMIT 10
                    """)

results = amounts.collect()

print("\n\nTop 10 customers:")
for result in results:
    print(" - Customer " + str(result[0]) + " spent " + str(round(float(result[1]), 2)))

print("\n\n")

#amounts.show()

spark.stop()