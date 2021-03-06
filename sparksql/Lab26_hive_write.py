from pyspark.sql import SparkSession

#11-Feb-2022

def main():
    
    spark = SparkSession.builder.appName("Lab24-datetime").master("local") \
    .config("hive.metastore.uris","thrift://localhost:9083") \
    .enableHiveSupport().getOrCreate().getOrCreate()
    
    spark.sparkContext.setLogLevel("ERROR")

    #spark.sql("show databases").show()
      
    #df.show()
    df = spark.read.format("csv").option("inferSchema",True).load("file:/home/hduser/hive/data/txns").toDF("txnid","txndate","custid","amount","category","product","city","state","paymenttype")
      
    #default -parquet
    #written the dataframe data into hive table
    df.write.saveAsTable("default.tbltrans")
      
    #create table in hive using hql
    spark.sql("create table default.tblmarks(studid int,mark1 int,mark2 int,mark3 int) row format delimited fields terminated by '~'")
      
    spark.sql("load data local inpath '/home/hduser/sparkdata/mark.csv' into table tblmarks")
      
    print("Table created and data loaded into the hive table")

main()