# Azure Data / ML Engineer

****NOTE****: for more on Databricks / Spark: https://github.com/huang-pan/modern-data-stack-2023/blob/main/Databricks%2C%20Spark.md

## Azure Databricks & Spark For Data Engineers (PySpark / SQL)

- https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/
	- Course completion certificate: https://www.udemy.com/certificate/UC-953b1ee6-3645-4797-8e02-d68b14d0dca2/
- Azure: Data Lake gen 2, Spark clusters, notebooks & dashboards, medallion architecture, incremental loads
- Delta Lake: process image, video, audio files in Spark
	- https://blog.devgenius.io/handling-media-files-in-pyspark-image-audio-video-files-8e3bcd7a5c4e
	- https://godatadriven.com/blog/real-distributed-image-processing-with-apache-spark/
 	- https://community.databricks.com/t5/data-engineering/how-to-process-images-and-video-through-structured-streaming/td-p/18738
- Azure Data Factory
- Unity Catalog
- **How to optimize Spark workloads**: https://www.databricks.com/discover/pages/optimize-data-workloads-guide
	- Liquid clustering better than static partitioning and zorder https://medium.com/closer-consulting/liquid-clustering-first-impressions-113e2517b251 

## Azure Databricks and Spark SQL

- https://www.udemy.com/course/azure-databricks-and-spark-sql-python/
	- Course completion certificate: https://www.udemy.com/certificate/UC-f9306a42-9538-4dd1-9ee6-7633cb069371/ 
- Medallion Architecture, hive metastore
- Azure Data Lake Storage v2
- Spark Structured Streaming
	- **Can stream directly into a pyspark dataframe or SQL table: a LOT easier than GCP Dataflow, Kinesis Data Analytics**
- Auto Loader
	- stream into one dataframe from all files in one directory
 	- schema inference, schema evolution
- Delta Live Tables https://docs.databricks.com/en/delta-live-tables/tutorial-sql.html 
	- Delta Live streaming tables, delta live tables (batch, aggregation)
	- Delta tables have checkpoints, including streaming tables
	- Delta Live Expectations: data quality constraints
	- enhanced autoscaling: primarily for streaming data
 	- https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/transform
  		- DLT (bronze, raw, incremental, streaming) -> DLT (silver, cleaned) -> Materialized View (Gold, aggregates)
    	- https://stephenallwright.com/materialize  Materialized View vs Table
     		- If you need to store data long term and use it as part of a data model then you should create a table, however if you want to join multiple tables and query this infrequently, as part of an analysis for example, then a materialized view would be the better choice.
- CI / CD with Databricks
	- Azure Devops solution: standard git -> dev -> test -> prod pipelines
- Polars is a pandas replacement: https://www.confessionsofadataguy.com/replacing-pandas-with-polars-a-practical-guide/

## Azure Data Engineer

- [https://www.youtube.com/playlist?list=PL7ZG6NdDdT8NRHDU5shVgGjlua297bm\-H](https://www.youtube.com/playlist?list=PL7ZG6NdDdT8NRHDU5shVgGjlua297bm-H)
	- Azure has a similar set of data engineering services to GCP and AWS. I went through the above lectures quickly because of this.
		- Azure Data Lake gen 2
		- Azure SQL (cloud MS SQL Server)
		- Azure Cosmos DB (like Mongo DB, Dynamo DB, Bigtable)
		- Azure Synapse Analytics
		- Azure Data Factory
		- Azure Stream Analytics
		- Azure Databricks
		- Azure HDInsight (Hadoop, Spark, Kafka)
	- If your company is Windows / .NET focused, you should start here. 
- Microsoft has recently [introduced](https://venturebeat.com/data-infrastructure/how-microsoft-fabric-aims-to-beat-amazon-and-google-in-the-cloud-war/) a new data integration environment called [Fabric](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview). Its goal is to break down all data silos and be a one stop shop for all your data needs. All your data is located in a data lakehouse, Fabric can access data in AWS & GCP data lakes, and AI prompting through Microsoft [Copilot](https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/) will be integrated with it. They hope to [leapfrog](https://venturebeat.com/data-infrastructure/how-microsoft-fabric-aims-to-beat-amazon-and-google-in-the-cloud-war/) AWS & GCP with this technology.
    - **Real Time Analytics in Fabric**: [https://learn.microsoft.com/en\-us/fabric/real\-time\-analytics/overview](https://learn.microsoft.com/en-us/fabric/real-time-analytics/overview) 
        - KQL database: real time database, use KQL to query real time data and push to Power BI
        - [https://learn.microsoft.com/en\-us/fabric/real\-time\-analytics/tutorial\-introduction](https://learn.microsoft.com/en-us/fabric/real-time-analytics/tutorial-introduction) 
        - **Seems to be an easier / more up to date solution than GCP Dataflow or AWS Kinesis Data Analytics**
- Azure Stream Analytics
    - [https://youtu.be/NbGmyjgY0pU](https://youtu.be/NbGmyjgY0pU) 
    - Looks pretty similar to other streaming solutions; SQL based windows etc.
- Azure Synapse Analytics
    - [https://learn.microsoft.com/en\-us/training/paths/realize\-integrated\-analytical\-solutions\-with\-azure\-synapse\-analytics/](https://learn.microsoft.com/en-us/training/paths/realize-integrated-analytical-solutions-with-azure-synapse-analytics/) 
        - [https://www.youtube.com/watch?v=1UHCiletocg&list=PLcwrIWK7WBcSB5O3GgbmAm0pxw0RBJrtK](https://www.youtube.com/watch?v=1UHCiletocg&list=PLcwrIWK7WBcSB5O3GgbmAm0pxw0RBJrtK)
        - [https://www.youtube.com/watch?v=Qoatg\-SPpe4&list=PLMWaZteqtEaIZxPCw\_0AO1GsqESq3hZc6](https://www.youtube.com/watch?v=Qoatg-SPpe4&list=PLMWaZteqtEaIZxPCw_0AO1GsqESq3hZc6)
    - Azure Synapse Analytics is an upgrade from Azure SQL Data Warehouse \(looked at in 2017 for Roofstock\)
        - built heavily on Spark / Delta Lake
            - Still don't like it \- prefer Snowflake
        - Azure Data Factory
            - Data Pipeline \(orchestration\)
            - Dataflow \(transforms\)
            - For Azure services
            - still don't like it \- clunky UI interfaces \(git integration? CI / CD?\) \- prefer Dagster

## Azure ML Engineer

- [https://www.youtube.com/watch?v=OwZHNH8EfSU](https://www.youtube.com/watch?v=OwZHNH8EfSU)
- Azure has a similar set of machine learning services to GCP and AWS. I went through the above lectures quickly because of this.
- I'm not focusing on Azure ML because I already have some experience with Azure, plus I'm doing the GCP ML course [https://www.cloudskillsboost.google/journeys/17](https://www.cloudskillsboost.google/journeys/17) which has plenty of labs. \(I haven't used GCP in production before\)
- Azure Machine Learning Studio
    - Seems pretty standard, like AWS & GCP solutions [https://youtu.be/kBz6zCzcPBQ](https://youtu.be/kBz6zCzcPBQ) 
        - Notebooks
        - AutoML
        - Designer: drag and drop models
        - Data
        - Jobs
        - Components
        - Pipelines
        - Environments
        - Models
        - Endpoints
        - Compute
        - Datastores
        - Linked Services
        - Data Labeling
- Azure MLOps
    - [https://opendatascience.com/machine\-learning\-operations\-mlops\-with\-azure\-machine\-learning/](https://opendatascience.com/machine-learning-operations-mlops-with-azure-machine-learning/) 