from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

spark = SparkSession.builder.appName("HeroAppearanceCount").getOrCreate()

movies_rdd = spark.read.text("Marvel+Graph").rdd.flatMap(lambda x: x)
names_rdd = spark.read.text("Marvel+Names").rdd.flatMap(lambda x: x)
#print(names_rdd.collect())

movies_hero_count_rdd = movies_rdd \
    .flatMap(lambda line: line.split(' ')) \
    .filter(lambda hero_id: hero_id != '') \
    .map(lambda hero_id: (hero_id, 1)) \
    .reduceByKey(lambda x, y: x + y) \
    .sortBy(lambda x: x[1], ascending=False)

names_mapping_rdd = names_rdd \
    .map(lambda line: line.split(' ', 1)) \
    .map(lambda parts: (parts[0], parts[1]))

#print(names_mapping_rdd.collect())

most_appeared_hero_id = movies_hero_count_rdd.first()[0]
most_appeared_hero_count = movies_hero_count_rdd.first()[1]
most_appeared_hero_name = names_mapping_rdd.filter(lambda x: x[0] == most_appeared_hero_id).first()[1]

print(f"\n\nThe hero that appears the most is: {most_appeared_hero_name} with {most_appeared_hero_count} appearances!\n\n")

least_appeared_hero_id = movies_hero_count_rdd.sortBy(lambda x: x[1], ascending=True).first()[0]
least_appeared_hero_count = movies_hero_count_rdd.sortBy(lambda x: x[1], ascending=True).first()[1]
least_appeared_hero_name = names_mapping_rdd.filter(lambda x: x[0] == least_appeared_hero_id).first()[1]

print(f"\n\nThe hero that appears the least is: {least_appeared_hero_name} with {least_appeared_hero_count} appearances!\n\n")

spark.stop()
