# Databricks, Udemy Spark

****NOTE****: 
- ****Guide for developing on Databricks****: https://blog.det.life/a-practitioners-guide-to-developing-data-engineering-solutions-with-databricks-1db5134ad831
- For Databricks on Azure: https://github.com/huang-pan/modern-data-stack-2023/blob/main/Azure%20Data%2C%20ML%20Engineer.md
- Also see MLOps on Azure Databricks section: https://github.com/huang-pan/modern-data-stack-2023/blob/main/MLOps.md
- Similarities and differences of Spark, Dask, and Ray https://www.youtube.com/watch?v=YpFACw3g0AY
![Screenshot_20240802-152116_YouTube](https://github.com/user-attachments/assets/115a9a69-7bda-467a-afed-b20eaf63e791)

## Udemy Spark
- [https://www.udemy.com/course/taming\-big\-data\-with\-apache\-spark\-hands\-on/](https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/)
- Course completion certificate: [https://www.udemy.com/certificate/UC\-c069b4b8\-3a68\-46e9\-a591\-f8c1c5a72b50/](https://www.udemy.com/certificate/UC-c069b4b8-3a68-46e9-a591-f8c1c5a72b50/) 
- Summary:
    - This is a refresher course on Spark for me and added to my existing knowledge of Spark. 
    - This course is a super basic introduction to Spark. 
        - It starts with the use of RDDs and then expands to using dataframes and SQL. 
        - You can implement algorithms in pyspark using RDDs, map, reduce, filter, etc. 
        - The course did some examples using both local Spark and Spark on AWS EMR. 
        - It touched on Machine Learning in Spark, and Spark Structured Streaming, GraphX, what's new in Spark 3.0.
    - Data engineering work using Spark is usually limited to data loading, cleaning, and transforms using pyspark dataframes or Spark SQL. RDDs usually too low level.
        - This course is better for data engineers \(Delta Lake, Unity Catalog\): [https://www.udemy.com/course/azure\-databricks\-spark\-core\-for\-data\-engineers/](https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/) 
        - Spark is becoming an older technology nowadays. If you're limited to purely data engineering work and batch processing, it's much faster to develop on Snowflake using SQL or python in Snowpark. You can extend existing data science / machine learning work with Dask clusters instead of using the more complex Spark. Spark has a higher learning curve and the applications are Spark are harder to tune / optimize and maintain.
    - I already did work on Spark 2\+ \- see: [https://github.com/huang\-pan/shift](https://github.com/huang-pan/shift) 
    - Exploratory Data Analysis nowadays can be sped up using ChatGPT, etc. \- see: [https://www.youtube.com/watch?v=C75TROiiEa0](https://www.youtube.com/watch?v=C75TROiiEa0) 
    - After this course, to dig into pyspark more: [https://github.com/cartershanklin/pyspark\-cheatsheet](https://github.com/cartershanklin/pyspark-cheatsheet) 
        - Supplementary video, great overview of Spark: [https://www.youtube.com/watch?v=S2MUhGA3lEw](https://www.youtube.com/watch?v=S2MUhGA3lEw) 
- Github repos for course:
    - PySpark cheat sheet: 
        - [https://www.globalsqa.com/pyspark\-cheat\-sheet/](https://www.globalsqa.com/pyspark-cheat-sheet/)
        - [https://sparkbyexamples.com/pyspark\-tutorial/](https://sparkbyexamples.com/pyspark-tutorial/) 
        - [https://intellipaat.com/blog/tutorial/spark\-tutorial/spark\-and\-rdd\-cheat\-sheet/?US](https://intellipaat.com/blog/tutorial/spark-tutorial/spark-and-rdd-cheat-sheet/?US)
    - ***How to optimize Spark workloads***
		- https://www.linkedin.com/posts/arslanali434343_bigdata-apachespark-dataengineering-activity-7209195256255242243-UHJW/ 
		- https://www.databricks.com/discover/pages/optimize-data-workloads-guide 
			- Z-order on high cardinality columns (e.g. uuid) - physically sorts or co-locates data
			- partition on low cardinality columns (e.g. year, month) - 
			- above common techniques for index clustering, e.g. like w/Azure SQL DB at Roofstock
			- use Photon to speed up queries
			- Spark UI Query execution plan or spark profiler to dig into queries
			- data skew
				- look at query plan, ID skew
					- redo query: filter out skewed values
					- break up tables into smaller ones, redo query
					- redo partition, z order
				- spark 3+: Adaptive Query Execution: monitors ANALYZE TABLE statistics, changes query plan during runtime
				- add salt to skewed columns
    					- https://www.youtube.com/watch?v=ufaQGQGeK3k
					- https://www.youtube.com/watch?v=zRtJ7dZ5eP4
![Screenshot_20240701-174055_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8363f8eb-6eaf-4ee7-ab6f-7db1cb424fad)
![Screenshot_20240701-174104_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bf43172d-9004-4bce-b6bc-e6c5e0f3f264)
![Screenshot_20240701-174113_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b9e8b88b-fd35-4751-926d-08cc3631113c)
![Screenshot_20240701-174128_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d084efa7-b558-41e1-835f-36b5205e9d6b)
![Screenshot_20240701-174149_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9fc9fdb0-580f-4813-b32f-7cc1ba03a54e)
![Screenshot_20240701-174222_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b76954ba-a4b6-433c-9b47-1ba350295f6a)
			- cluster instance types:
				- memory: for lots of shuffles during execution
				- compute: structured streaming
				- storage: delta caching
				- GPU: ML / Deep Learning
				- General purpose
			- right sizing number of workers guide
		-  Spark performance optimizations
			- https://youtube.com/watch?v=NvziNVQSlqk&si=Yl5G2PolHOBbbtU3
    			- https://youtube.com/watch?v=boGuRnyFL-I&si=x5DSjEDIH4_Z5Ef5
			- code
    			- file format (parquet)
       			- spark optimizations
          		- configuration, garbage collection
  ![shuffle](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d675d4c0-ae88-4a65-a288-195782659a1c)
![sparkui](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/726db2a8-460b-4a4e-a740-325cb76de992)
![partitioning](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9b915abf-816d-4eda-88f2-7b30ce5eec3e)
![gc](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/aad5569b-56c2-4d39-90ac-4f67b3409f26)
![expensive](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5bc2e53b-5d70-4f57-b68c-99d2a659033d)
![diskspill](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/54b815d6-0b34-4bec-a941-087fa8fffadd)
![dynamicallocation](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e43e25b6-6c08-4aab-9651-ab8b9b29ad62)
![serialize](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1721a154-193c-42bc-9169-1f05e737c1ae)

	- Delta Lake 3.0: Liquid clustering better than static partitioning and zorder https://medium.com/closer-consulting/liquid-clustering-first-impressions-113e2517b251   
    	- https://www.linkedin.com/posts/bigdatabysumit_bigdata-career-dataengineering-activity-7093867870463397888-Et4V/
     	- https://youtube.com/watch?v=5EkYtX9CuC4&feature=share
      		- start with general sizing, then monitor RAM, CPU, I/O usage
        	- spark usually needs high memory VMs
		- https://www.newsletter.swirlai.com/p/a-guide-to-optimising-your-spark
		- https://www.newsletter.swirlai.com/p/a-guide-to-optimising-your-spark-841 
			- If the main use case for Spark is OLAP - use ****Parquet**** or ORC.
			- If the main use case is about frequently writing data (OLTP) - use ****Avro****.
    	- partitioning: https://medium.com/@tagnev.vengat/essential-tips-for-optimizing-apache-spark-queries-part-1-data-partitioning-unleashed-e4c3f1eae8b
	- partitioning vs bucketing
   		- https://youtu.be/fp0PN9Y9QiY?si=agFuiRaT3sxcuYkC
	 		- partition using low cardinality columns; bucket on high cardinality columns
   			- can have bucketed and non-bucketed tables: Databricks workspace: Data section (table), DBFS section (actualy parquet files)
      			- can read in bucketed / non-bucketed tables into dataframes
         			- df1.join(df2, 'PK').explain(): bucketed to bucketed df join: ****no shuffle**** at both sides, just a ****sort merge join****
         			- non-bucketed to non-bucketed df join: ****shuffle**** at both sides, an expensive ****shuffle hash join****
         			- bucketed to non-bucketed df join: shuffle on one side, then sort merge join
 		- partition first: if get a lot of small files, then use bucketing to group small files together
   		- https://medium.com/@ghoshsiddharth25/partitioning-vs-bucketing-in-apache-spark-a37b342082e4
     		- https://www.youtube.com/watch?v=Kr_AAkzGZsI
- Set up Spark from the JDK: in reality, I would use a managed service like Spark on EMR or GCP DataProc
    - course starts with installing and running Spark locally
        - spark\-submit pyspark\_script.py
    - Please see related coursework I completed on GCP:
        - [https://www.cloudskillsboost.google/journeys/16](https://www.cloudskillsboost.google/journeys/16)
        - [https://www.cloudskillsboost.google/journeys/17](https://www.cloudskillsboost.google/journeys/17) 
- The course starts by using RDDs; most of the work in Spark nowadays is done using Spark dataframes
- **Spark 3.\+**
    - python 3
    - new dataframe based ML library, spark graph library, Delta Lake
    - better performance
    - integration with deep learning libraries like Tensorflow, GPU support
    - Kubernetes integration
- Architecture of Spark
    - driver program: spark context
    - cluster manager: Spark, YARN
    - Executors: cache, tasks
    - python is translated to Scala which runs on the JVM
- spark initialization
    - conf = SparkConf\(\).setMaster\("local"\).setAppName\("MinTemperatures"\)
    - sc = SparkContext\(conf = conf\)
- spark sessions
    - spark = SparkSession.builder.appName\("MinTemperatures"\).getOrCreate\(\)
    - lines = spark.sparkContext.textFile\("fakefriends.csv"\)
    - ...
    - spark.stop\(\)
- Resilient Distributed Dataset
    - RDD **transforms**: map, flatmap, filter, distinct, sample, union, intersection, subtract, cartesian
        - transform takes RDD as an input, outputs another RDD
        - map: one to one transform
        - flatmap: one to many transform, e.g. split sentence into individual words
    - many RDD methods accept a function as a parameter
    - RDD **actions**: collect, count, countByValue, take, top, reduce
        - action take RDD as an input, outputs a value
        - lazy execution, e.g. collect forces Spark to do all the preceding transforms
    - filtering RDDs: filter
- key value manipulations: reduceByKey, groupByKey, sortByKey
- pyspark dataframes
    - I'm paying more attention to the dataframe solutions than the RDD solutions
    - dataframe manipulations \(select, group by, etc.\) can also be done in \(Spark\) SQL
    - don't worry about Spark DataSets, they are only used in Scala
    - data manipulations for course taught using RDDs, but there is also corresponding code that does the same manipulations using dataframes
    - dataframe schema
        - schema = **StructType**\(\[ \\
        -                StructField\("stationID", StringType\(\), True\), \\
        -                      StructField\("date", IntegerType\(\), True\), \\
        -                      StructField\("measure\_type", StringType\(\), True\), \\
        -                      StructField\("temperature", FloatType\(\), True\)\]\)
        - schema can also be inferred after reading in csv / parquet, etc. file
            - people = spark.read.option\("header", "true"\).option\("inferSchema", "true"\).csv\("file:///SparkCourse/fakefriends\-header.csv"\)
- **broadcast variable**
    - small variable \(e.g. dictionary\) broadcast to each executor
    - def loadMovieNames\(\):
    - spark = SparkSession.builder.appName\("PopularMovies"\).getOrCreate\(\)
    - nameDict = spark.sparkContext.broadcast\(loadMovieNames\(\)\)
    - \# Create a user\-defined function to look up movie names from our broadcasted dictionary
    - def lookupName\(movieID\):
        - return nameDict.value\[movieID\]
    - lookupNameUDF = func.udf\(lookupName\)
    - \# Add a movieTitle column using our new udf
    - moviesWithNames = movieCounts.withColumn\("movieTitle", lookupNameUDF\(func.col\("movieID"\)\)\)
- Spark SQL
    - Spark SQL performs better than Hive on Hadoop
    - works with structured and semistructured data
    - can use User Defined Functions UDFs
    - dataframe API
    - spark **dataframes are RDDs with schemas schemaRDD**
        - to be more specific, a dataframe is a Domain Specific Language \(DSL\) e.g. SQL / python, that uses datasets with schemas
            - a dataset is a distributed collection of data
        - dataframe is like a table in a relational database
- Breadth First Search
    - can implement more complicated algorithms in pyspark, but this is an RDD implementation
        - not super useful for data engineering which uses pyspark dataframes or spark SQL
    - preprocess graph
    - map function
        - create new nodes for each connection of gray nodes, with a distance incremented by one, color gray, and no connections
        - colors the gray node we just processed black
        - copies the node itself into the results
    - reduce function
        - combines together all nodes for the same hero ID
        - preserves the shortest distance, and the darkest color found
        - preserves the list of connections from the original node
    - **accumulator**: allows many executors to increment a **shared variable**
- item based collaborative filtering: movie recommendations
    - out of the purvue of data engineering, more data science oriented
        - uses dataframes
        - first version runs on local Spark, single machine
    - compute cosine similarity function
    - Pyspark **cache**\(\) method is used to cache the intermediate results of the transformation so that other transformation runs on top of cached will perform faster. Caching the result of the transformation is one of the optimization tricks to improve the performance of the long\-running PySpark applications/jobs.
    - **persist**\(\) optionally lets you cache dataframe to disk instead of just memory in case a node fails
- Spark local \-\-\> cluster \(uses AWS EMR\)
    - example of setting up Spark cluster on EMR
    - version of movie recommendations that works on a Spark cluster
- **Spark history server: Spark UI**
    - has list of spark jobs that has been run, can click on each job and see how stages / tasks have been broken down
        - has list of executors, etc.
- cluster performance optimization
    - partitioning: use .partitionBy\(\) on an RDD before running a large operation that benefits from partitioning
        - operations that benefit from partitioning: join\(\), cogroup\(\), groupwith\(\), join\(\), leftouterjoin\(\), rightouterjoin\(\), groupbykey\(\), reducebykey\(\), combinebykey\(\), lookup\(\)
    - now we start getting into Spark cluster configuration
        - default executor memory budget: 1 GB
        - https://www.linkedin.com/blog/engineering/infrastructure/right-sizing-spark-executor-memory
        - upload pyspark\_[script.py](http://script.py) to AWS S3 bucket
        - SSH into Spark cluster master node and 
            - spark\-submit \-\-executor\-memory 1g pyspark\_[script.py](http://script.py)
            - look at log output to see if there are any errors, e.g. executor out of memory error
            - also can debug from Spark UI \(hard to connect from outside AWS EMR, so course showed Spark UI on local machine\)
            - Spark local mode: logs in web UI
            - Spark YARN cluster: logs distributed, can be found in each executor
                - compile logs using: yarn logs \-\-applicationID \<app ID\>
- Spark Machine Learning ML
    - standard suite of ML algos
    - example using prebuilt Spark ML Alternating Least Squares algorithm for movie recommendations
    - example of linear regression in Spark
    - example of decision tree regression in Spark
    - train model and then use for prediction
- Spark Streaming
    - **dstream** Discretized Stream object: breaks stream into distinct RDDs
        - divided data stream into batches of input data as RDDs
        - RDD @ time 1, time 2, etc.: apply regular Spark transforms
        - streams have checkpoints
    - has window operations, pretty standard among all streaming technologies \(sliding, hop, session\)
    - word count example
    - can use in **conjunction with Spark ML**
        - train models with live data
    - can use **in conjunction with Spark SQL** / Dataframes
        - interactively query live streams with SQL
    - Spark streaming example https://sparkbyexamples.com/spark/spark-streaming-with-kafka/
    	- use spark stream to read from Kafka topic into dataframe, <100 ms latency
       		- can query dataframe using Spark SQL
        - newer way to do it: kafka topic --> Kafka connector -> dump into data lakehouse --> auto load into Delta Live Table --> Spark SQL query Delta Live Table
    - Spark streaming trigger available now, trigger on size 100mb, multi hop streaming
    	- ****streaming analytics solution**** with Kafka, Spark streaming, delta tables in data lakehouse
     	- oltp -> kafka topic -> spark stream -> bronze landing delta table (append) -> spark stream trigger available now on size 100mb -> silver (star schema fact / dim tables) -> batch spark -> gold (aggregate metrics)
      		- oltp -> kafka topic -> data lake json file -> bronze landing delta live table (append) -> delta live table silver (star schema fact / dim tables) -> materialized view gold (aggregate metrics)
      		- oltp ->  kinesis firehose -> S3 json / parquet / iceberg file -> snowpipe streaming -> snowflake dynamic table -> silver dynamic tables (star schema fact / dim tables) -> gold dynamic table
      	-  https://youtube.com/watch?v=JfDGYKvRfWw&si=rRwRpMn1i2-dtiT6
- Structured Streaming
    - ever expanding dataframes \(unbounded input table\)
    - streaming code looks like batch code, can use Spark ML on structured streaming
    - useful for real time data engineering
    - example of streaming log file count application that uses dataframe
- Spark GraphX
- After this course, to dig into pyspark more: [https://github.com/cartershanklin/pyspark\-cheatsheet](https://github.com/cartershanklin/pyspark-cheatsheet) 

## Udemy Spark 3 beyond the basics
[https://www.udemy.com/course/apache\-spark\-3\-beyond\-basics/](https://www.udemy.com/course/apache-spark-3-beyond-basics/)

- Course completion certificate: [https://www.udemy.com/certificate/UC\-230f3948\-d2f2\-405a\-9f55\-3c0f151db965/](https://www.udemy.com/certificate/UC-230f3948-d2f2-405a-9f55-3c0f151db965/) 
- Summary:
    - I felt the Spark introductory course was a bit lacking, so I also enrolled in this course.
    - The spark architecture part of this course was useful. The Performance and Applied Understanding section was a little too detailed \- only useful if you really want to tune your app or the cluster. More modern data technologies like Snowflake abstract away all the tuning \- it's much faster to develop on Snowflake.
    - Other useful Spark courses:
        - [https://www.udemy.com/course/azure\-databricks\-spark\-core\-for\-data\-engineers/](https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/) 
        - [https://www.udemy.com/course/apache\-spark\-programming\-in\-python\-for\-beginners/](https://www.udemy.com/course/apache-spark-programming-in-python-for-beginners/) 
- Spark Architecture
    - master node has Spark driver which contains the SparkContext
        - spark applications run as independent sets of processes on a cluster
        - driver program and spark context takes care of the job execution within the cluster
    - cluster managers: Hadoop YARN, Kubernetes, Apache Mesos, Spark Standalone \(local mode\)
        - cluster has cluster manager
        - worker node has node manager
            - within a worker, the executor take care of running a task and returns the results back to the Spark context
    - worker node has x (3?) number of executors
    - cluster capacity: sum of all worker nodes
        - worker node: 16 CPU cores, 64 GB ram
- **spark\-submit**
    - submit spark application / script \(.py or .jar file\) to master node \(YARN Resource Manager\) of cluster
    - \-\-driver\-cores, driver\-memory, num\-executors, executor\-cores, executor\-memory
    - client mode: spark driver on client, almost never use in production
    - cluster mode: spark driver on cluster \(YARN RM\)
- spark interactive mode
    - run spark through CLI
        - spark\-shell \(scala\)
        - sparkR
        - **pyspark**
        - **spark\-sql**
    - run spark through a notebook
- Spark Data Frame API \(runs on Dataset API \- Scala only\)
    - transformations
        - **narrow** dependency
            - performed in **parallel** on data partitions
            - select, filter, withcolumn, drop
        - **wide** dependency
            - performed **after grouping** data from multiple partitions
            - groupby, join, cube, rollup, agg
    - actions
        - used to trigger Job, lazy execution
        - read, write, collect, take, count
    - **logical plan**: step by step break down of pyspark statement
        - one spark **application** \-\-\> multiple spark jobs
        - one spark **job**: friendsByAge.groupBy\("age"\).agg\(func.round\(func.avg\("friends"\), 2\)\).sort\("age"\).show\(\)
            - RDD split into partitions \(default 2\): each partition executed on different node / executor
                - RDD split across various nodes
        - broken down into **stages**
            - stages separated by **wide** dependencies
            - narrow dependencies done in each stage
                - each group of narrow dependencies that can be run in **parallel** a stage is called a **task**
            - each stage outputs an exchange buffer which is then **shuffled** / sorted \(repartitioned\) before being read by next stage
        - job \-\-\> broken down into stages \-\> shuffle / sort \-\-\> task \(smallest unit of work in spark job\)
        - each executor / worker node has X number of **slots** - 1 slot = 1 core
            - **tasks** run in each slot in **parallel** across all executors
            - driver has to balance task execution across all executor slots
            - data is split into **partitions of varying size** that is accessed by tasks in executor slots
        - **job / stages / tasks can be seen in Spark UI**
- https://www.linkedin.com/posts/bigdatabysumit_bigdata-career-dataengineering-activity-7093867870463397888-Et4V/
	- Internal working of Apache Spark - One of the most liked writeup
	Lets say you have a 20 node spark cluster
	Each node is of size - 16 cpu cores / 64 gb RAM
	Let's say each node has 3 executors,
	with each executor of size - 5 cpu cores / 21 GB RAM
	
	=> 1. What's the total capacity of cluster?
	We will have 20 * 3 = 60 executors
	Total CPU capacity: 60 * 5 = 300 cpu Cores
	Total Memory capacity: 60 * 21 = 1260 GB RAM
	
	=> 2. How many parallel tasks can run on this cluster?
	We have 300 CPU cores, we can run 300 parallel tasks on this cluster.
	
	=> 3. Let's say you requested for 4 executors then how many parallel tasks can run?
	so the capacity we got is 20 cpu cores
	84 GB RAM
	so a total of 20 parallel tasks can run.
	
	=> 4. Let's say we read a csv file of 10.1 GB stored in datalake and have to do some filtering of data, how many tasks will run?
	if we create a dataframe out of 10.1 GB file we will get 81 partitions in our dataframe. (will cover in my next post on how many partitions are created)
	so we have 81 partitions each of size 128 mb, the last partition will be a bit smaller.
	so our job will have 81 total tasks.
	but we have 20 cpu cores
	lets say each task takes around 10 second to process 128 mb data.
	so first 20 tasks run in parallel,
	once these 20 tasks are done the other 20 tasks are executed and so on...
	so totally 5 cycles, if we think the most ideal scenario.
	10 sec + 10 sec + 10 sec + 10 sec + 8 sec
	first 4 cycles is to process 80 tasks all of 128 mb,
	last 8 sec is to process just one task of around 100 mb, so it takes little lesser but 19 cpu cores were free during this time.
	
	=> 5. is there a possibility of, out of memory error in the above scenario?
	Each executor has 5 cpu cores and 21 gb ram.
	This 21 gb RAM is divided in various parts -
	300 mb reserved memory,
	40% user memory to store user defined variables/data. example hashmap
	60% spark memory - this is divided 50:50 between storage memory and execution memory.
	so basically we are looking at execution memory and it will be around 28% roughly of the total memory allotted.
	so consider around 6 GB of 21 GB memory is meant for execution memory.
	per cpu core we have (6 GB / 5 cores) = 1.2 GB execution memory.
	That means our task can roughly handle around 1.2 GB of data.
	however, we are handling 128 mb so we are well under this range.
- Spark Memory https://www.linkedin.com/posts/aurimas-griciunas_mlops-machinelearning-dataengineering-activity-7103325115748110336-xqcm/
  ![sparkmemory](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/abfe03b4-4aed-4512-a23c-f1b27f07ad42)


	- https://youtu.be/RPGCJXmTGWw?si=EZ-BdK-t9Q2wsAnt
![memory](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5ceb2b03-117a-4f1c-adcc-42b245b8dcbf)

- Spark SQL
    - one SQL expression = one Spark **job**
    - SQL expression or pyspark line \-\-\> unresolved logical plan \-\-\> Spark SQL engine
    - Spark execution plan [https://sparkbyexamples.com/spark/spark\-execution\-plan/?expand\_article=1](https://sparkbyexamples.com/spark/spark-execution-plan/?expand_article=1) 
        - unresolved logical plan \-\-\> logical plan \-\-\> optimized logical plan \-\-\> physical plans \-\-\> cost model \-\-\> selected physical plan \-\-\> RDDs
- https://youtube.com/watch?v=BVsKJ6xQxsQ&feature=share 
	- how spark works under the hood: logical, physical plan optimizations
	- logical, physical operators
- ***Databricks / Spark optimizations***
	- https://www.databricks.com/discover/pages/optimize-data-workloads-guide
- Shuffle hash joins (expensive, major source of slowing down Spark jobs) vs Broadcast joins (cheaper)
	- https://youtube.com/watch?v=vswrfVkP10Y&si=nnYWCIo1GjuD5P3o 
	- stage: read in 2 DFs, each with 3 partitions -> map partitions to new partitions based on join keys -> shuffle partitions (take longest time, disk / network IO) --> stage: reduce phase, join data
- Sort Merge Join (default join)
	- https://youtube.com/watch?v=isOuTH_49pY&si=dLhxHm7PN5r1gSZ2
 	- shuffle / repartition (map) -> sort data within partition -> merge / join (reduce)
- Other Joins (not commonly used): https://youtube.com/watch?v=fp53QhSfQcI&si=ocvSMtdW4B1i_-pZ
- Memory Allocation / Management
    - driver, executor memory
    - overhead, heap, off heap, pyspark
- ***Adaptive Query Execution***
    - dynamically coalescing shuffle partitions, switching join strategies, optimizing skew joins
    - Spark 3+, details of AQE https://blog.cloudera.com/how-does-apache-spark-3-0-increase-the-performance-of-your-sql-workloads/
    - https://youtube.com/watch?v=elCPrsqBaME&si=mA98M8yZw0OzBQoi
- Data Skew
	- https://towardsdatascience.com/data-skew-in-pyspark-783d529a9dd7
 	- https://statusneo.com/solving-data-skewness-in-apache-spark-techniques-and-best-practices/
  	- https://medium.com/@suffyan.asad1/handling-data-skew-in-apache-spark-techniques-tips-and-tricks-to-improve-performance-e2934b00b021
- Partitioning
	- https://www.youtube.com/watch?v=KcflbFv5saY 
	- Input Partitioning
		- RDDs immutable, input partitioning set at beginning of Spark job
		- spark.sql.files.maxPartitionBytes: max number of bytes per partition
		- getNumPartitions()
	- Output Partitioning
		- sets number of output files to write
	- Shuffle Partitioning
		- spark.sql.shuffle.partitions
		- default is 200 shuffle partitions
- Dynamic Partition Pruning
	- https://youtube.com/watch?v=W9yo0bnf0ss&si=asF1j-A3rg0iFXsz
	- Dynamic Partition Pruning vs. Static Partition Pruning: predicate pushdown during query, DPP only uses the partitions that contain info for the query
- Data Caching: cache, persist
- Repartition, Coalesce
    - repartition by hash, range of values; repartition evenly distributes the data: serialize data, move, deserialize
    - coalesce consolidates data across partitions and reduces the number of partitions; coalesce does not evenly distribute the data, is faster than repartition
- Broadcast Variables
    - broadcast join
- Accumulators
- Speculative Execution
- Dynamic Resource Allocation
    - scheduling across applications
        - static vs dynamic allocation
            - two spark jobs submitted at the same time to cluster, YARN must allocate resources to each job
    - scheduling within an application
        - can trigger 2 spark jobs within an application to run in parallel
- Unit Testing
- Debug Spark
	- https://youtu.be/6z53q66cqHY?si=-ORxZFBO6Q8EjGSC
 	- Note: trade off for increasing number of partitions: increase number of partitions uses less memory per executor, but more executors - more tasks are spread across more executors
![1sparknostart](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/81dc7549-341f-48e9-abbb-164e48f5d56c)
![2slowtasks](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/70560958-74af-45cd-9b97-95e5de92a59f)
![3slowagg](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/56a62b57-f1f5-4589-8fd9-5ac6d5ccdd12)
![4slowjoin](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/97ebd583-2af7-42e6-8f96-376891093b18)
![5driveroom](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9f9d256b-3c5c-49a5-b93f-11a25ae71f45)
![6execoom](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5cd0f30b-a638-47d6-9f13-6607e69bc515)


MLFlow AI Gateway: https://www.databricks.com/blog/announcing-mlflow-ai-gateway 

## Databricks Data and AI Summit 2023
- take this Databricks class: https://www.udemy.com/course/azure-databricks-and-spark-sql-python/ 
- Lakehouse AI https://youtube.com/watch?v=bQOEIeUx9pU&feature=share 
	- Databricks state of the art unified data engineering and ML development platform
	- By breaking down the silos between the data stack, ML stack and DevOps stack, Databricks offers a simplified, faster, and better-governed way to do ML, including integrated feature engineering and governance tooling, end-to-end tracking and lineage of models and data, automatic monitoring, and root cause analysis.
- Lakehouse IQ https://youtube.com/watch?v=QgLLaUuApzQ&feature=share 
	- Use natural language to query everything in Databricks ecosystem
- Spark 3.4 https://youtube.com/watch?v=jmwK_zIFPTM&feature=share 
	- Spark Connect
		- connect to Spark from IDE, etc. thin API layer connecting client to spark server
		- https://youtube.com/watch?v=p9IRFSjuLBE&feature=share
	- support for pytorch
	- pyspark.ai
		- https://youtube.com/watch?v=ZunjkL3L62o&feature=share 
		- ingest data from the web
		- english to SQL / pyspark
		- transcribe audio
		- create plots, analyses, etc.
		- explain code
		- predict, etc.
		- uses langchain
		- https://youtube.com/watch?v=ndL3TlWlA1o&feature=share 
	- Photon next gen Spark, compatible with Spark, accelerates SQL queries: https://www.databricks.com/product/photon
 		- 2x performance https://medium.com/sync-computing/are-databricks-clusters-with-photon-and-graviton-instances-worth-it-845641d464f2	
	- https://youtube.com/watch?v=BVsKJ6xQxsQ&feature=share 
		- how spark works under the hood: logical, physical plan optimizations
		- logical, physical operators
- Delta Live Tables https://youtube.com/watch?v=PIFL7W3DmaY&feature=share 
	- Delta tables: parquet + metadata, https://youtu.be/ouecrLhjPBM?si=W3hm3c6WRC7vzZjz
 		- ***table partitioning***
   			- https://stackoverflow.com/questions/70881505/databricks-z-order-vs-partitionby#:~:text=Partitioning%20physically%20splits%20the%20data,possible%20values%20for%20given%20column.
      			- https://community.databricks.com/t5/data-engineering/what-s-the-difference-between-z-ordering-and-partitioning/td-p/26656
         		- https://docs.databricks.com/en/tables/partitions.html
		           - https://docs.databricks.com/en/tables/partitions.html#ingestion-time-clustering
           		- Partitioning physically splits the data into different files/directories having only one specific value, while ZOrder provides clustering of related data inside the files that may contain multiple possible values for given column.
Partitioning is useful when you have a low cardinality column - when there are not so many different possible values - for example, you can easily partition by year & month (maybe by day), but if you partition in addition by hour, then you'll have too many partitions with too many files, and it will lead to big performance problems.   Amount of data in each partition should meet a minimum threshold
ZOrder allows to create bigger files that are more efficient to read compared to many small files. This works somewhat like secondary indexes in terms of improving query read performance. 
But you can combine both partitioning with ZOrder - for example partition by year/month, and ZOrder by day - that will allow to collocate data of the same day close to each other, and you can access them faster (because you read fewer files). 
Besides ZOrder, you can also use data skipping to efficiently filter out files that doesn't contain data you need for your query.

	- unified batch and streaming tables, declarative tables
		- streaming tables (ingest): to bronze
		- materialized views (transforms): to silver
		- autoscaling, retries
  			- https://synccomputing.com/is-databrickss-autoscaling-cost-efficient/
	- expectations: testing
		- auto shunt bad data to error tables
	- multi hop streaming from bronze to silver table
	- many new techniques for automating declarative streaming tables and materialized views
	- DLT Serverless https://docs.databricks.com/serverless-compute/index.html
		- Photon underneath - fast https://www.databricks.com/product/photon
  		- Databricks medium SQL serverless warehouses best bang for your buck: https://towardsdatascience.com/5-lessons-learned-from-testing-databricks-sql-serverless-dbt-1d85bc861358
		- Databricks serverless not that good (not linear cost/performance with compute size), not as good as Snowflake warehouses
  			- https://medium.com/sync-computing/top-9-lessons-learned-about-databricks-jobs-serverless-41a43e99ded5
	- ST ingest into Bronze --> materialized view in Silver
	- DLT pipelines: code, target, configuration; auto manage lifecycle, dependency, isolation (dev/stg/prod) - for CI / CD
		- create dynamic pipelines in python
		- uses Databricks Pipelines API
	- Use Github Actions / DAB for CI/CD, integrated with Github PRs
 	- Data Lake Table formats: https://youtube.com/live/mXitwotQaAU?feature=share
  		- Apache Iceberg: most comprehensive format, supports table / catalog versioning that the other formats don't
    		- Apache Hudi: event based table format, for events
      		- Delta Tables: periodic log checkpoints
- AutoLoader
	- https://www.linkedin.com/posts/vishalwaghmode_whatsthedata-dataengineering-databricks-activity-7215006513365454848-A1qv/
		- Don't use COPY INTO, use Databricks AutoLoader (or Delta Live Tables?)
	- https://youtube.com/watch?v=2F6mBvLoavs&feature=share
		- auto detect and add files in S3 directory, auto infer schemas, auto error processing
	- https://youtube.com/watch?v=VUt4sKBelPo&feature=share
		- declarative pipelines create entire new set of problems: Dangers of schema inference, declarative pipelines 
		- Streaming merge schema
		- Autoloader schema explosion
		- Schema drift, need dashboards to monitor 
- Configurable metadata pipelines in Databricks
	- https://youtube.com/watch?v=WYv5haxLlfA&feature=share
- Databricks Asset Bundles
	- CI / CD processes for DE / ML: dev -> stg -> prod
	- https://youtube.com/watch?v=9HOgYVo-WTM&feature=share
- Databricks Workflows (orchestration, imperative, but can orchestrate declarative data pipelines)
	- https://youtube.com/watch?v=SKJibVvB2hQ&feature=share 
	- https://www.databricks.com/blog/2022/05/10/introducing-databricks-workflows.html 
- Unified Batch and Streaming
	- https://youtube.com/watch?v=Jv_SCwNndMc&feature=share 
		- Kinesis -> Delta Live Table --> Workflows triggers and real time alerts -> RT dashboard
	- https://youtube.com/watch?v=vTbVBlHhecQ&feature=share
		- general overview of delta lake streaming
		- what to watch out for: OOM Out of Memory errors (millions of keys in memory)
			- use RocksDb instead to store streaming state on HDD
	- https://youtube.com/watch?v=khhzniCyfP4&feature=share
		- detailed analysis of how to create robust streaming applications
- LLMs 
	- https://www.youtube.com/watch?v=-ijwLeXgPB4
		- Foundation Models in the MDS
		- Self service ad hoc queries for business people 
		- Prompt engineering for data cleaning and entity resolution 
		- RAG: Retrieval Augmented Generation
			- input your own data into the LLM
		- Create a RAG based Chatbot with Databricks https://www.youtube.com/watch?v=p4qpIgj5Zjg
![Screenshot_20240619-160019_YouTube](https://github.com/user-attachments/assets/18eea031-7ba4-4082-83d4-bf06d5325823)

	- Use LLMs to generate natural language interfaces / chatbots, etc. add to medium article
		- deploy internal LLMs so no public data exposure
- LLMOps: MLFlow 2.5 https://www.databricks.com/dataaisummit/session/llmops-everything-you-need-know-manage-llms/
	- has all the features for MLOps
	- plus LLMOps AI Gateway add to MLOps section in medium (also LangSmith)
		- Vector search: index domain documents, auto index queries and responses for further training
		- Mlflow evaluation: compare models
		- GPU serving for LLMs
	- Lakehouse monitoring: auto generated dashboard, PII detection
- LLMApp https://youtu.be/Bu3UZpHy0r0
	- ![LLMapp](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e7b9727f-ad82-4bfb-86da-13cb7515b191)
- Unity Catalog
	- Predictive Optimization, Lakehouse Monitoring (data quality alerts, PII automasking, model performance / drift monitoring)
		- https://youtube.com/watch?v=8WppyVldn1o&feature=share 
	- Data search, RBAC down to column level
		- https://youtube.com/watch?v=CXAFpTo8_WQ&feature=share 
	- federated access to all data stores (postgres, Snowflake, etc.)
		- https://youtube.com/watch?v=vGyXpHTYgrQ&feature=share 
	- Data lineage: easy to track down dirty data origin and all downstream data / models it affected
		- https://youtube.com/watch?v=bZXswjZ0avA&feature=share 
- Monte Carlo + Unity Catalog
	- https://youtube.com/watch?v=09sTDFaOuw4&feature=share 
	- Data Reliability / Observability
	- Freshness, Volume, Quality, Schema, Lineage
	- Detect: ML anomaly detection
	- Resolve: 
	- Prevent:
- Delta Sharing
	- https://youtube.com/watch?v=imSi6dYBXSg&feature=share 
	- https://www.databricks.com/product/delta-sharing
	- Delta sharing, clean rooms: share data, models, notebooks, etc.
- Databricks Dashboards
	- integrated across all features, some auto generated
- Databricks and MS Power BI
	- Power BI MS Copilot integration
	- https://youtube.com/watch?v=uadUz6jRb8g&feature=share
- Databricks Feature Store: https://github.com/huang-pan/modern-data-stack-2023/blob/main/Feature%20Store.md#databricks-feature-store

## Example streaming data architecture using Databricks Delta Live Streaming Tables / Delta Live Tables & Views; or Spark Structured Streaming
- AWS services such as S3, Lambda, DMS, Athena, SNS, Kinesis, EMR etc.
- kafka JSON payloads
	- SMS messages, Design and build multi-tenant systems capable of loading and transforming large volumes of structured and semi-structured fast moving data
	- Kafka / Kinesis throughput sizing, latency
		- https://github.com/huang-pan/modern-data-stack-2023/blob/main/Udemy_Kafka.md 
- structured streaming
	- can stream into bronze_df from Kafka topic, etc.
	- can also use kinesis data firehose to stream into S3 bucket directory and then create streaming table from that directory
		- https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/transform 
		- https://docs.databricks.com/en/delta-live-tables/tutorial-sql.html 
	- batch: can also autoload into bronze_df from S3 bucket directory
- delta live table: autoscaling if use spark cluster, or use serverless compute
	- https://www.databricks.com/blog/2022/06/29/delta-live-tables-announces-new-capabilities-and-performance-optimizations.html
		- DLT employs an enhanced auto-scaling algorithm purpose-built for streaming. scales up for streaming ETL / analytics.
		- DLTs Enhanced Autoscaling optimizes cluster utilization while ensuring that overall end-to-end latency is minimized. 
		- It does this by detecting fluctuations of streaming workloads, including data waiting to be ingested, and provisioning the right amount of resources needed (up to a user-specified limit). In addition, Enhanced Autoscaling will gracefully shut down clusters whenever utilization is low while guaranteeing the evacuation of all tasks to avoid impacting the pipeline.
	- cluster autoscaling?
		- same as DLT enhanced autoscaling https://docs.databricks.com/en/delta-live-tables/auto-scaling.html 
		- ****Spark cluster autoscaling not worth it****: too much time spent changing size of cluster, but you have to try it / tune it to see if it works for your workload
			- https://synccomputing.com/is-databrickss-autoscaling-cost-efficient/
	- https://www.youtube.com/watch?v=vTbVBlHhecQ
		- delta lake streaming: be prepared to break streams
			- stream to stream joins
			- stream to static table joins
		- bounds: cpu, ram, disk, network I/O
			- Out of Memory Error OOM: too many key / value pairs in memory
			- find approximate bounds from delta tables: size cluster correctly (or use autoscale, serverless compute)
			- calculate how fast table is growing: average bytes per day
		- rate limiting
			- limit the volume of data per trigger
			- limit the microbatch frequency
		- avoid real time schema evolution
	- https://www.youtube.com/watch?v=khhzniCyfP4
		- streaming application mistakes
		- streaming transforms
			- window aggregation
			- pattern detection
			- enrichment
			- routing
		- kafka best practices
			- size kafka cluster (topics / partitions) correctly for consumption
				- rate limiting
			- kafka errors topic
		- size delta table correctly for volatile data
			- rate limiting: see above
			- size spark cluster correctly for time of day volume spikes
		- checkpoints so don't have to restart stream from scratch
		- stateful store management (watch size of stateful store growing --> OOM)
			- streaming aggregation
			- drop duplicates
			- stream to stream joins
			- use watermark to filter outdated data, periodically clean
			- use RocksDB for stateful store: low latency, stores state to disk to avoid OOM
- databricks SQL serverless compute https://docs.databricks.com/en/serverless-compute/index.html 
	- serverless warehouses now an option vs regular spark clusters
		- for DB SQL, ML Model Serving, workflows, DLT, notebooks; NOT FOR PYSPARK (general compute)
	- https://www.youtube.com/watch?v=Jv_SCwNndMc
		- example serverless compute for real time pipeline
		- kinesis -> Delta Live Table Table pipeline
			- -> spark structured streaming data analytics
			- -> databricks notebooks display streaming visualization
			- -> databricks SQL dashboard
		- can see Delta Live Table pipeline in Databricks UI
			- example notebook: spark readstream format delta into delta live table group by window, etc
			- configure stream: format kinesis, streamname, region, aws access key, aws secret key
		- Data lineage in Databricks UI
  	- Databricks ****medium SQL serverless warehouses**** best bang for your buck: https://towardsdatascience.com/5-lessons-learned-from-testing-databricks-sql-serverless-dbt-1d85bc861358
	- Databricks serverless not that good (not linear cost/performance with compute size), not as good as Snowflake warehouses
		- https://medium.com/sync-computing/top-9-lessons-learned-about-databricks-jobs-serverless-41a43e99ded5
- photon: next gen spark, accelerates SQL queries 2x
- databricks optimizations
	- https://www.databricks.com/discover/pages/optimize-data-workloads-guide
	- Liquid clustering better than static partitioning and zorder https://medium.com/closer-consulting/liquid-clustering-first-impressions-113e2517b251
- Databricks workflows for orchestration over entire lakehouse
	- https://www.databricks.com/blog/2022/05/10/introducing-databricks-workflows.html
		- orchestrate databricks notebooks, Delta Live Table pipeline, dbt, spark submit jobs
		- supports both data engineering and ML
	- https://www.youtube.com/watch?v=SKJibVvB2hQ
		- schedule and monitor structured streaming and delta live tables
		- lots of connectors to MDS
		- can use serverless compute
	- integrates with Databricks Asset Bundles and Github Actions CI / CD
- Azure devops CI / CD
	- https://www.udemy.com/course/azure-databricks-and-spark-sql-python/learn/lecture/38369238#overview
		- PR -> main branch -> build pipeline -> build artifact (notebooks) -> deploy to test / prod environment
		- CI: create build pipeline in Azure DevOps: runs build job -> create artifact
		- CD: create release pipeline: artifact -> deploy to test / prod environment run by Databricks workflows
		- test / prod environment
			- databricks workspace with dev / test / prod folders with notebooks that can be called by databricks workflows
			- can also use Databricks Asset Bundles
	- Databricks Asset Bundles 
		- https://www.youtube.com/watch?v=9HOgYVo-WTM 
			- yaml file that specifies artifacts, resources, configurations of a databricks project
				- databricks workspace, cluster size
				- dev / stg / prod environments
			- example DLT pipeline
				- stream into df from DLT, do cleaning, 
				- stream into another df from cleaned df, do aggregation (groupby)
		- https://www.youtube.com/watch?v=uG0dTF5mmvc 
	- can also use Github Actions
- databricks namespaces? 
	- You reference all data in Unity Catalog using a three-level namespace: catalog.schema.table.
	- workspaces: 
		- one for each region (north america, canada, central america)
			- dev / stg / prod folders in each workspace
		- can have one workspace each for dev / stg / prod
	- Unity Catalog oversees all workspaces
		- https://docs.databricks.com/en/data-governance/unity-catalog/index.html 
		- You reference all data in Unity Catalog using a three-level namespace: catalog.schema.table. 
		- data lineage in all workspaces
			- federated data from AWS, etc.
	- Evolving Data Governance With Unity Catalog https://www.youtube.com/watch?v=lZbmBAxa3O4
![Screenshot_20240619-163642_YouTube](https://github.com/user-attachments/assets/7866b798-eccf-4b5a-98ec-7d39ee43bc3d)
![Screenshot_20240619-163827_YouTube](https://github.com/user-attachments/assets/2d472f4d-57ea-4763-b4b0-86c3c36d5f2b)
![Screenshot_20240619-163936_YouTube](https://github.com/user-attachments/assets/d4b438ca-bf48-41ae-957f-60498b803e5a)

## Spark + high Velocity of data
- 3V's: Volume, Variety, Velocity
	- https://www.youtube.com/watch?v=svYMMRnZzQM&feature=share 
- https://blog.dataengineer.io/p/how-to-optimize-100-tb-data-pipelines
- How to process extremely large (> 100TBs) data sets without burning millions
	- I first worked with >100 TB pipelines when I joined the Core Growth team at Facebook in 2016 back when it was the best place to work. The first three months were filled with ice cream, bike rides, and lots of fun!
	- Then suddenly my dream paradise turned intense when my boss, Jitender told me, I was to own the push, email, and SMS notification data for all of Facebook.
- I was excited about this challenge when I learned:
	- Facebook sends 50 BILLION NOTIFICATIONS every single day
	- Facebook has five channels they send notifications through
	- Jewel, Push, Email, SMS, and Logged Out Push
	- We need low latency for optimal machine learning
	- The notification filtering machine learning degraded significantly if it was delayed > 1 day.
	- It’s a complex space that balances between spammy and engaging!
- 
- I was tasked with creating a much more efficient version of “notif_delivery_deduped” which was a deduplicated log of all notification events each day.
- The old pipeline was just a big GROUP BY query that fired at the end of the day. Except this query took NINE HOURS to run and oftentimes would fail and delay the notifications ML training algorithms downstream!
- 
- Deduping tens of billions of records in micro-batch
	- Initially, my manager suggested I create a streaming job in Flink that dedupes the data in real-time from Scribe (scribe was Facebook’s version of Kafka).
	- I tried to make that streaming job work. The issue was the dedupe required tens of TBs of RAM in order to run since it needed to hold onto each record in memory to dedupe. Facebook’s infrastructure at the time couldn’t address this without some crazy customizations.
- The next idea was to dedupe every hour in batch and then merge those hours together.
- I initially tried a pipeline that was
	- Dedupe hour 1 → Dedupe hour 2 → merge hours 1 and 2 → Dedupe hour 3 → merge hours 1,2 and 3, etc until all 24 hours were deduped
	- The problem with this approach was it required a TON of IO of the data and it barely improved the landing time. 9 hours to 6 hours!
- After working with more of the engineers, we figured doing it like a tree would greatly improve the landing time of the data!
- 
- This design worked the best! Here’s a code repo with the pattern detailed
	- This pattern worked! It allowed almost all the deduping to happen throughout the day and minimized the IO-heavy operations! Now the notification datasets would land one hour after midnight instead of nine hours!
	- This pattern involves a lot of FULL OUTER JOIN and GROUP BY which involves a great deal of shuffling! So how do you minimize shuffling?
	- Make sure the merge tables and final table are sorted and bucketed on the unique identifier. This means the only time you actually pay the shuffle cost is during the GROUP BY and all the FULL OUTER JOINs happen without shuffle at all! Bucket joins are one of the most powerful things you can do when managing extremely large data!
- Feeding the deduped events into machine learning training
	- After we optimized the flow of notifications events, I set my sights downstream. There was an inefficient join between the notification machine learning features table and the deduped events table. This table also had its own dedupe step.
- Right around this time, Facebook started adopting Spark in places. I became one of the first data engineers at Facebook to try Spark in the warehouse!
- So, I did two things here:
	- Made the generation of the features table sorted and bucketed on the same keys as the events table
	- I migrated the GROUP BY to Spark so the dedupe, sort, and bucket were 10 times more efficient. (Spark vs Hive performance difference is most profound in the case of high cardinality GROUP BY and JOIN)
	- This allowed the notifications team to generate and evaluate their machine-learning features much more reliably and on time! We cut notification compute usage by 30% too!
- 
- The dos and don’ts of extremely large data
- Please do the following when working with very large data
	- Use Apache Spark or Apache Flink to process the data.
	- Use Scala Spark or ****SparkSQL**** not PySpark because you’ll feel the small performance differences at this huge scale.
	- ****Partition your data both by day and by hour**** (intervals smaller than this seem to be counter-productive because of Spark’s slow startup time)
	- Consider subpartitioning your data
		- At Facebook, we partitioned on day, hour, and “channel” where channel was the method we used to send the notification
		- ****Ideal candidates for subpartitions are low-cardinality (< 15 values)****
	- Sample if you can and just don’t work with big data
	- Track your costs
		- Costs are in the following areas:
			- Computation cost from Spark
			- IO cost from S3 (or whatever cloud provider you’re using)
			- Storage cost from S3 (or whatever cloud provider you’re using)
		- ****Generally speaking, the biggest point of cost is going to be the ingress and egress of data from S3****
		- Short retention since we don’t want to pay for such a large cloud storage
			- Make sure to store long-term aggregates though so you don’t miss anything when the data falls out of retention
	- Check your disk spill. Increase partitioning or memory if it’s high!
	- Log data ahead of time using things like sidecar proxies to minimize the number of joins needed to solve the problem
	- Try to have your joins fit into memory and leverage broadcast join
- Please never do the following when working with very large data:
	- Long retention = burning tons of money
	- Try to tackle the problem with Trino/Presto, ****Snowflake, or any other technology that doesn’t spill to disk well!****
	- Do joins that aren’t bucketed or broadcastable
	- ****Remember that shuffle caused by JOIN is much more expensive than shuffle caused by GROUP BY****
	- ****Using SparkSQL ORDER BY and not sortWithinPartitions, a global ordering of your data is a pipe dream when it is this big!****
- Please rarely do the following (as they seem like they could help but don’t):
	- Rarely change any other Spark setting except ****spark.executor.memory, spark.sql.shuffle.partitions, spark.driver.memory, spark.default.parallelism, spark.sql.adaptive.enabled, spark.sql.autoBroadcastJoinThreshold****
	- ****Rarely increase the broadcast join threshold beyond 8 GBs, it doesn’t work and causes reliability issues****
	- Rarely change compression types like lz4 vs snappy. I’ve always found this to be an unfruitful endeavor

## The Big Book of Data Engineering with Databricks 2nd edition
[big-book-of-data-engineering-2nd-edition-final.pdf](https://github.com/huang-pan/modern-data-stack-2023/files/13065105/big-book-of-data-engineering-2nd-edition-final.pdf)
- Use larger clusters (memory / CPU, etc. optimized): workloads run faster
- Use Delta Cache
- Lazy Evaluation faster than without it
- pyspark profilers
	- cProfile
	- driver profiling
	- worker profiling
		- UDF profiler: Spark 3.3+
- DLT
	- Spark Structured Streaming: has check pointing; Delta Live Streaming Tables automatically takes care of checkpointing and triggers
		- streaming trigger: how often stream will look for new data
			- SLA > 10 minutes, use trigger.once -> batch processing
		- lower streaming latency by
			- using shorter trigger interval
			- increasing resources available: adding more workers, use compute / memory optimized instances
			- having fewer streams per cluster
			- check for data skew in each Spark job
			- stateful queries (aggregations, etc) need to have watermark set
		- stateful streaming
			- streaming aggregations / drop duplicates / stream - stream joins, etc.
			- use RocksDB to store streaming state to avoid worker node Out Of Memory errors
				- adds latency to streaming pipeline, but alleviates OOM pressure
			- higher watermark threshold -> more streaming data in memory
	- either SQL or python, SQL preferred for dbt
	- lower latency when reading directly from message bus
		- Needs schema mapping when reading data from Kafka
	- OR stream into S3, use databricks autoloader
		- COPY INTO command with mergeSchema schema inference
			- schema changes tracked by Unity Catalog
			- use COPY into when source directly has small number of files
		- Autoloader
			- use for larger number of files
			- for both streaming and batch
		- recommended to use autoloader with DLT pipelines
			- schema inference / evolution
			- auto error handling, quality control, data lineage, setting expectations
	- DLT streaming uses spark structured streaming under the hood
	- DLT pipelines vs Databricks Workflows
- Databricks Workflows
	- an alternative to DLT pipelines
	- Spark jobs that run on Spark clusters (autoscale)
		- spark structured streaming
	- photon
	- serverless SQL warehouse
	- Unity Catalog
	- Delta Lake Storage
- production
	- unit tests for all spark steps
	- can use the same batch unit tests for streaming
	- can have multiple streams per Spark cluster
- Geospatial
	- grid index systems: KD trees, ball trees, quad trees
	- storage: geoparquet
- ****Example solutions architecture notebooks in pdf above****
- A lot of companies are using DLT pipelines for streaming IoT
	- case studies: Rivian, Akamai, Grammarly, Honeywell, Wood Mackenzie, AT&T
- https://blog.dataengineer.io/p/how-to-save-millions-by-optimizing  **no shuffles** group by join bucketing

## Medallion architecture best practices
- see: https://github.com/huang-pan/modern-data-stack-2023/blob/main/Data%20Warehouse%2C%20DBT.md#dbt--spark
- https://youtube.com/live/QimxOUwHdgo?si=r00ucK2VSTE93QMC 
	- Scd type 2 merges not optimal in delta lake; data vault append / insert only architecture better for delta lake 
	- DLT insert only incremental tables best for iot
	- Meshdallion arch: DLT for bronze silver, dbt for gold
	- Can explode nest json into silver layer but costs a lot of storage, data analyst like
	- Can also keep nested json in gold, data scientist like, and have separate layer for unnested json for analysts 
- https://www.databricks.com/blog/2023/04/14/how-we-performed-etl-one-billion-records-under-1-delta-live-tables.html
	- How We Performed ETL on One Billion Records For Under $1 With Delta Live Tables
	- TPC-DI benchmark

## Databricks & Apache Spark Performance Tuning
- https://www.youtube.com/watch?v=hLOpfxpgc70
- ![Screenshot_20240611-215434_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/48052837-60da-47be-b060-567d3a38d11d)
- ![Screenshot_20240611-215149_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/723b5d2f-0b5c-4565-b0e4-e4e8a357aecb)
- ![Screenshot_20240611-214932_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/57813c01-cd03-4185-8629-9e27c8662763)
- ![Screenshot_20240611-214802_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/15522cf1-0ac7-4d44-9377-fd061667908e)
- ![Screenshot_20240611-214626_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/64ec829e-c1d9-4e53-af54-4a08f86b0c86)

## Databricks Summit 2024
- https://seattledataguy.substack.com/p/developing-production-databricks
	- Developing Production Databricks Pipelines
- https://www.youtube.com/watch?v=HHzvWh9sJuE 
- truly serverless compute
-
- LLM dev integration in Databrick dev env
- LLM search on data: Databricks Genie: https://www.youtube.com/watch?v=uKLscjh__Yc
- ![Screenshot_20240613-115139_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75c6ac9b-295d-46a2-80b9-25e823ea9651)
- Spark 4.0 https://www.databricks.com/dataaisummit/session/whats-next-upcoming-apache-spark-40

- Gigasheet for Databricks, like Sigma Computing for Databricks
	- https://gigasheet.com/databricks
- Summit recap https://www.youtube.com/watch?v=63BRE2vry44
![Screenshot_20240618-163642_YouTube](https://github.com/user-attachments/assets/b5ff16be-37de-4413-85c1-7eafc85e8c13)
![Screenshot_20240618-163716_YouTube](https://github.com/user-attachments/assets/4e439543-6fb2-4dba-825b-b2244bbe6c6d)
![Screenshot_20240618-163822_YouTube](https://github.com/user-attachments/assets/b56b4659-a6fa-439f-9060-cf72388f4f10)
![Screenshot_20240618-164059_YouTube](https://github.com/user-attachments/assets/31865300-b360-42d8-87c3-10620367cbae)
![Screenshot_20240618-164107_YouTube](https://github.com/user-attachments/assets/29627f16-6858-4184-b081-b726dbba82af)
![Screenshot_20240618-164112_YouTube](https://github.com/user-attachments/assets/5f72791b-a388-4530-93fa-a5c00af46b33)
![Screenshot_20240618-164516_YouTube](https://github.com/user-attachments/assets/3a1dd100-91c2-4f19-8e9f-6cfe1d80fe3d)
![Screenshot_20240618-164734_YouTube](https://github.com/user-attachments/assets/ffba9268-1968-43c5-9005-406b46ffb068)
![Screenshot_20240618-164855_YouTube](https://github.com/user-attachments/assets/37ee4218-0787-4d5f-bff1-072414f07f7f)

- The Best Data Warehouse is a Lakehouse https://www.youtube.com/watch?v=UcdFPRT_sG8
![Screenshot_20240619-153917_YouTube](https://github.com/user-attachments/assets/b0b81d9b-68a3-419f-b351-1c06d376bc04)
![Screenshot_20240619-153945_YouTube](https://github.com/user-attachments/assets/bf4758da-1b6c-4d9e-a786-6bacb9ecbdb1)
![Screenshot_20240619-153959_YouTube](https://github.com/user-attachments/assets/64b4da98-3593-4105-8839-b159cf60d3c6)
![Screenshot_20240619-154249_YouTube](https://github.com/user-attachments/assets/c6724dd7-b4ff-45e6-b1c4-e0a21dfa4f06)
![Screenshot_20240619-154301_YouTube](https://github.com/user-attachments/assets/b528ba8a-1b08-435d-bbc7-00bddce14f83)
![Screenshot_20240619-154312_YouTube](https://github.com/user-attachments/assets/669a76e3-1c73-4dd5-85b9-695e7f6f83e1)
![Screenshot_20240619-154401_YouTube](https://github.com/user-attachments/assets/bf27daf0-53cd-4281-a008-07616a024986)
![Screenshot_20240619-154411_YouTube](https://github.com/user-attachments/assets/b375224b-ebbc-47cb-8063-a330136565a6)
![Screenshot_20240619-154425_YouTube](https://github.com/user-attachments/assets/8d1e82b4-540b-4c6b-8fb9-5bffc4dbc262)
![Screenshot_20240619-154554_YouTube](https://github.com/user-attachments/assets/8cf3e547-e7ec-42bc-8727-1a36c835fdb0)
![Screenshot_20240619-154724_YouTube](https://github.com/user-attachments/assets/23c28ade-08e1-47d6-96de-5b369b0f423c)

- Announcing Delta Lake 4.0 with Liquid Clustering https://www.youtube.com/watch?v=joy4jdYJg3c
![Screenshot_20240617-121204_YouTube](https://github.com/user-attachments/assets/cf02ac87-39ba-44c7-8b5c-dcaef7caa85a)
![Screenshot_20240617-121317_YouTube](https://github.com/user-attachments/assets/a8350e76-1da9-49f3-a992-fb586fdfeade)
![Screenshot_20240617-121457_YouTube](https://github.com/user-attachments/assets/d0c046ac-25e5-4665-a241-35f902fffcc6)
![Screenshot_20240617-121542_YouTube](https://github.com/user-attachments/assets/443d6c0a-a2a8-4d79-9632-d742c2bbb8d2)

- Databricks LakeFlow: A Unified, Intelligent Solution for Data Engineering https://www.youtube.com/watch?v=6rzQ6xjkYko
	- LakeFlow Connect: auto ETL ingest tool to Databricks https://www.databricks.com/product/data-ingestion
![Screenshot_20240619-151659_YouTube](https://github.com/user-attachments/assets/d95caefc-8cf1-4568-814d-b36593a7f104)
![Screenshot_20240619-152031_YouTube](https://github.com/user-attachments/assets/008e9864-a496-4caa-ab3c-84efc849d265)
![Screenshot_20240619-152242_YouTube](https://github.com/user-attachments/assets/bff9ecc5-f2c5-476f-80ac-47759052de7d)
![Screenshot_20240619-152409_YouTube](https://github.com/user-attachments/assets/c3b0c291-ff02-44f5-be97-8344e0694eb2)
![Screenshot_20240619-152429_YouTube](https://github.com/user-attachments/assets/048489cd-e47e-464b-b67c-23f2e4021d32)
![Screenshot_20240619-152533_YouTube](https://github.com/user-attachments/assets/b1be7a0b-5e3a-4626-b9b6-fc93ec70ef2d)
![Screenshot_20240619-152651_YouTube](https://github.com/user-attachments/assets/5f906f99-e96a-4f4e-adc8-3520da6a4f3f)
![Screenshot_20240619-152731_YouTube](https://github.com/user-attachments/assets/ef7356d1-4d2f-4c06-85db-9cdb8f8b495d)
![Screenshot_20240619-152816_YouTube](https://github.com/user-attachments/assets/9fc846d9-c378-4884-b787-0f57d28b85a3)
![Screenshot_20240619-152846_YouTube](https://github.com/user-attachments/assets/9b7b886d-29ea-4953-929b-a654826ca210)
![Screenshot_20240619-152855_YouTube](https://github.com/user-attachments/assets/3e6157d3-13c5-4252-9c0f-2d628f8fe3f8)

- DBRX Databricks LLM https://www.youtube.com/watch?v=Sf7r2XcLNEk
![Screenshot_20240619-115124_YouTube](https://github.com/user-attachments/assets/a0c72fde-3a55-4396-82b5-1c9e4f3dc368)
![Screenshot_20240619-115138_YouTube](https://github.com/user-attachments/assets/6868e679-810b-4147-b01e-6cdaedf482e3)
![Screenshot_20240619-115206_YouTube](https://github.com/user-attachments/assets/db125ba7-642f-4650-8fb3-bc5bffd94f34)
![Screenshot_20240619-115253_YouTube](https://github.com/user-attachments/assets/018b3d9b-6215-4352-9abc-cce4edb3cfd2)

## Databricks Photon
- next gen Spark engines https://www.linkedin.com/posts/jorritsandbrink_dataengineering-softwareengineering-activity-7211134200320565249-vxZO/
	- Open source:
		- Apache DataFusion Comet ➜ Rust (language) + Arrow (data format)
		- Apache Gluten (Incubating) + Velox ➜ C++ (language) + Arrow (data format)
	- Proprietary:
		- Databricks Photon ➜ C++ (language) + proprietary Arrow-like (data format)
		- Microsoft Fabric ➜ uses Gluten + Velox
- Photon next gen Spark SQL compute engine completely rewritten in C++ https://www.youtube.com/watch?v=PwnUf6_0H0k
![Screenshot_20240703-183012_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7e1aa915-0830-46fb-8d81-f584af7d67b9)
![Screenshot_20240703-183022_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a36fd9de-274d-487a-9bdd-6f8730d7a411)
![Screenshot_20240703-183039_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cbe37f27-9ec8-458b-bb9f-4835077fd55d)
![Screenshot_20240703-183042_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/24fbf352-761e-4fc6-a51f-6b3fba7cf9dc)
![Screenshot_20240703-183124_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/11a56a83-ce77-417b-b52d-7e53b69b4701)
![Screenshot_20240703-183131_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ebac7bce-fee7-4d0d-8345-99d9017afd78)
![Screenshot_20240703-183144_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/32b3bc4a-07ce-42ee-841e-79bf49a70fc9)
![Screenshot_20240703-183151_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c6a157f2-0cfd-412a-9c98-099f7ab8275f)
![Screenshot_20240703-183208_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b46d07a4-6de6-4880-93bf-9c338bd9c864)
![Screenshot_20240703-183212_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b34f75e2-fcb6-48f5-95b2-11457f1431e9)
![Screenshot_20240703-183216_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3652f61b-58d0-4334-b034-7630e73ba763)
![Screenshot_20240703-183237_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c9024a9b-ec32-45b0-9002-66e321e1e039)
![Screenshot_20240703-183247_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/10a9c2a0-e2b5-4e5a-a2b4-58c87bfa6fc1)
![Screenshot_20240703-183252_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0654e9d7-706e-427e-afce-ee40a9d35563)
![Screenshot_20240703-183318_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3e09f1d7-08eb-48a6-a529-a0f4c1fcaf49)
![Screenshot_20240703-183328_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a2415eb5-d39e-42af-aa72-7c0728202a33)

## Databricks Cost Savings
- Great video on cost savings in Databricks https://www.youtube.com/watch?v=Qp7QOrI8T5A
- Ray is more efficient than Spark for large amounts of data
	- https://aws.amazon.com/blogs/opensource/amazons-exabyte-scale-migration-from-apache-spark-to-ray-on-amazon-ec2/

## Databricks Summit 2025
- Lakeflow Designer auto-ETL pipeline creator
	- https://www.linkedin.com/posts/daniel-klein-72703731_this-product-demo-at-our-data-and-ai-summit-activity-7344009121190342660-8NNE/
	- https://www.youtube.com/watch?v=0pys27kA67U&t=4472s
