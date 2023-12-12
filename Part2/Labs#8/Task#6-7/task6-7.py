from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

### Read data

# Create a Spark session
spark = SparkSession.builder.appName("HeroAppearanceCount").getOrCreate()

movies_df = spark.read.text("Marvel+Graph")

movies_df = movies_df.select(explode(split(movies_df.value, ' ')).alias('hero_id')).filter(col('hero_id') != '')

names_df = spark.read.text("Marvel+Names")

names_df = names_df.select(split(names_df.value, ' ', 2)[0].alias('hero_id'), split(names_df.value, ' ', 2)[1].alias('name'))

names_df.show()



### Task 6 ###

# Count the occurrences of each hero
hero_count_df = movies_df.groupBy('hero_id').count().orderBy('count', ascending=False)

# Show the result
hero_count_df.show()

# Get the hero with the highest count
most_appeared_hero_id = hero_count_df.first()['hero_id']
most_appeared_hero_row = names_df.filter(col('hero_id') == most_appeared_hero_id).first()

most_appeared_hero_name = most_appeared_hero_row['name']

print(f"\n\nThe hero that appears the most is: {most_appeared_hero_name}\n\n")



### Task 7 ###

hero_count_df_inverted = movies_df.groupBy('hero_id').count().orderBy('count', ascending=True)

# Show the result
hero_count_df_inverted.show()

least_appeared_hero_id = hero_count_df_inverted.first()['hero_id']
least_appeared_hero_row = names_df.filter(col('hero_id') == least_appeared_hero_id).first()

least_appeared_hero_name = least_appeared_hero_row['name']

print(f"\n\nThe hero that appears the least is: {least_appeared_hero_name}\n\n")


# Stop the Spark session
spark.stop()
