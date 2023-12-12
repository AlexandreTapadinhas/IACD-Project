from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Minimum Temperature")

# Load the input file
lines = sc.textFile("1800.csv")

tmin_lines = lines.filter(lambda line: line.split(",")[2] == "TMIN")

# Parse the lines to extract station and temperature
station_temps = tmin_lines.map(lambda line: line.split(",")).map(lambda x: (x[0], int(x[3])))

# Find the minimum temperature for each station
min_temps = station_temps.reduceByKey(lambda x, y: min(x, y))

# Print the result
print(min_temps.collect())

# Stop the SparkContext
sc.stop()
