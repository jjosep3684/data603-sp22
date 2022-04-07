#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 22:18:05 2022

@author: josh
"""


from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import matplotlib.pyplot as plt
import time

spark = (SparkSession 
    .builder 
    .appName("stream iss") 
    .getOrCreate()
    )
    
lines = (
    spark.readStream 
    .format("socket") 
    .option("host", "localhost") 
    .option("port", 22223) 
    .load()
    
)

write_df = lines.selectExpr("CAST(value as STRING) as json")


writer = (
    write_df.writeStream
    .queryName('iss') 
    .format('memory')
    .outputMode('append')
 )
    
streamer = writer.start()
 
for i in range(230):
     total_df = spark.sql("select * from iss")
     total_df.show()
     check_df = spark.sql("""
SELECT 
    get_json_object(json, '$.iss_position.latitude') AS latitude,
    get_json_object(json, '$.iss_position.longitude') AS longitude
    
FROM iss
""").toPandas()

     
     time.sleep(2)
    
check_df.plot.scatter(x='latitude', y = 'longitude', c='DarkBlue')
plt.show()
