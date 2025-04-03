#!/usr/bin/env python3
import sys
import os
import re
import pandas as pd
import pyspark
import json
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from collections import defaultdict
import subprocess


def main():

    # read ndc_product_semaglutide.csv, read product_ndc_9digit as string
    ndc_product_semaglutide = pd.read_csv("../NDC_directory/ndc_product/ndc_product_semaglutide.csv", 
                                         dtype={"product_ndc_9digit": str})
    print("Loaded semaglutide NDC codes")
    # print the number of semaglutide NDC codes
    print(f"Number of semaglutide productNDC codes: {len(ndc_product_semaglutide)}")
    
    print("Starting Spark session...")
    # Kill any running Spark processes
    subprocess.run("ps aux | grep spark | grep -v grep | awk '{print $2}' | xargs -r kill", shell=True)

    # Stop any existing Spark session
    if 'spark' in locals():
        spark.stop()
    # Create a new Spark session
    spark = SparkSession.builder \
        .appName("MDCR D (outpatient prescription)") \
        .config("spark.driver.memory", "128g") \
        .config("spark.executor.memory", "128g") \
        .config("spark.memory.fraction", "0.8") \
        .config("spark.executor.cores", 8) \
        .config("spark.executor.instances", 25) \
        .config("spark.default.parallelism", 448) \
        .config("spark.sql.shuffle.partitions", 448) \
        .config("spark.sql.files.maxPartitionBytes", "128m") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer") \
        .config("spark.sql.inMemoryColumnarStorage.compressed", "true") \
        .config("spark.sql.parquet.filterPushdown", "true") \
        .config("spark.network.timeout", "600s") \
        .config("spark.rdd.compress", "True") \
        .master("local[*]") \
        .getOrCreate()

    


    # read mdcr_data_paths_dict.json
    with open("mdcr_data_paths_dict.json", "r") as f:
        mdcr_data_paths = json.load(f)

    # List of file paths to drug (D)
    mdcr_d_paths = []
    for key in mdcr_data_paths.keys():
        if key.startswith('mdcr_d'):
            for file_path in mdcr_data_paths[key]:
                mdcr_d_paths.append(file_path)

    mdcr_d = spark.read.parquet(*mdcr_d_paths)

    # extract the first 9 digits of NDCNUM and make a new column NDCNUM_9
    mdcr_d = mdcr_d.withColumn("NDCNUM_9", F.substring("NDCNUM", 1, 9))

    num_mdcr = mdcr_d.count()
    print(f"Total number of mdcr_d orders: {num_mdcr}")

    # Filter mdcr_d based on the ndc_product_semaglutide product_ndc_9digit values
    mdcr_d_semaglutide = mdcr_d.filter(F.col("NDCNUM_9").isin(ndc_product_semaglutide["product_ndc_9digit"].tolist()))

    # number of semaglutide orders
    num_mdcr_semaglutide = mdcr_d_semaglutide.count()
    print(f"Total number of semaglutide orders: {num_mdcr_semaglutide}")
    
    # number of unique enrollees
    num_unique_enrollees = mdcr_d_semaglutide.select("ENROLID").distinct().count()
    print(f"Number of unique enrollees that had semaglutide orders: {num_unique_enrollees}")


    # Create output directory if it doesn't exist
    os.makedirs("processed_data", exist_ok=True)
    # Check if the path exists and overwrite if it does
    mdcr_d_semaglutide.write.mode("overwrite").parquet("processed_data/mdcr_d_semaglutide.parquet")
    print("Successfully wrote data to processed_data/mdcr_d_semaglutide.parquet")

    spark.stop()
    print("Spark session stopped")



if __name__ == "__main__":
    main()