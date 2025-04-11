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
        .appName("medicaid D (outpatient prescription)") \
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

    


    # read medicaid_data_paths_dict.json
    with open("medicaid_data_paths_dict.json", "r") as f:
        medicaid_data_paths = json.load(f)

    # List of file paths to drug (D)
    medicaid_d_paths = []
    for key in medicaid_data_paths.keys():
        if key.startswith('medicaid_d'):
            for file_path in medicaid_data_paths[key]:
                medicaid_d_paths.append(file_path)

    medicaid_d = spark.read.parquet(*medicaid_d_paths)

    # extract the first 9 digits of NDCNUM and make a new column NDCNUM_9
    medicaid_d = medicaid_d.withColumn("NDCNUM_9", F.substring("NDCNUM", 1, 9))

    num_medicaid = medicaid_d.count()
    print(f"Total number of medicaid_d orders: {num_medicaid}")

    # Filter medicaid_d based on the ndc_product_semaglutide product_ndc_9digit values
    medicaid_d_semaglutide = medicaid_d.filter(F.col("NDCNUM_9").isin(ndc_product_semaglutide["product_ndc_9digit"].tolist()))

    # number of semaglutide orders
    num_medicaid_semaglutide = medicaid_d_semaglutide.count()
    print(f"Total number of semaglutide orders: {num_medicaid_semaglutide}")
    
    # number of unique enrollees
    num_unique_enrollees = medicaid_d_semaglutide.select("ENROLID").distinct().count()
    print(f"Number of unique enrollees that had semaglutide orders: {num_unique_enrollees}")


    # Create output directory if it doesn't exist
    os.makedirs("processed_data", exist_ok=True)
    # Check if the path exists and overwrite if it does
    medicaid_d_semaglutide.write.mode("overwrite").parquet("processed_data/medicaid_d_semaglutide.parquet")
    print("Successfully wrote data to processed_data/medicaid_d_semaglutide.parquet")

    spark.stop()
    print("Spark session stopped")


if __name__ == "__main__":
    main()