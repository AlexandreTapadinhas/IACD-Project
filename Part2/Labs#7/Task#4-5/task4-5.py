from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Total Amount Spent by user")

# Load the input file
lines = sc.textFile("customer-orders.csv")

# format: id, product_id, amount

user_amount_spent = lines.map(lambda line: line.split(",")).map(lambda x: (x[0], float(x[2]))).reduceByKey(lambda x, y: x+y)

sorted_user_amount_spent = user_amount_spent.sortBy(lambda x: x[1], ascending=False)

results = sorted_user_amount_spent.collect()

print("\n\nTop 10 customers:")
for result in results:
    print(" - Customer " + str(result[0]) + " spent " + str(round(float(result[1]), 2)))

print("\n\n")