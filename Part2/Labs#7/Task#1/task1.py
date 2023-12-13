from pyspark import SparkContext

sc = SparkContext("local", "Minimum Temperature")

lines = sc.textFile("1800.csv")

tmin_lines = lines.filter(lambda line: line.split(",")[2] == "TMIN")

station_temps = tmin_lines.map(lambda line: line.split(",")).map(lambda x: (x[0], int(x[3])))

min_temps = station_temps.reduceByKey(lambda x, y: min(x, y))

res = min_temps.collect()
print("\n\n")
for i in res:
    print(i[0] + "\t{:.2f}C".format(i[1] / 10))

print("\n\n")

sc.stop()
