# Modern Data Stack 2023

Huang Pan's data architecture and engineering learning path for 2023.

I updated / refreshed my data engineering skill set in 2023. This consisted of two parts:

1. Research all the up to date tools in the [Modern Data Stack in 2023](https://medium.com/@huangpan/modern-data-stack-2023-ab3364b9281d)
![Unified Data Infrastructure](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/547c12f5-e40f-4d44-81bf-aaa2100a03c4)

2. Take courses to refresh / update my data engineering skills:
	- [DBT / Data Warehousing](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Data%20Warehouse%2C%20DBT.md)
	- [Spark](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Databricks%2C%20Spark.md) / [Databricks Data and AI Summit 2023](https://www.youtube.com/watch?v=PIFL7W3DmaY&list=PLTPXxbhUt-YW6v14Vs3sTx6cyK5URKKgO)
	- [Kafka / KSQL](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Kafka%2C%20KSQL.md)
	- [FastAPI](https://github.com/huang-pan/modern-data-stack-2023/blob/main/FastAPI.md)
	- [AWS Data Engineer](https://github.com/huang-pan/modern-data-stack-2023/blob/main/AWS%20Data%20Engineer.md)
	- [AWS Machine Learning Engineer](https://github.com/huang-pan/modern-data-stack-2023/blob/main/AWS%20ML%20Engineer.md)
	- [GCP Data Engineer](https://github.com/huang-pan/modern-data-stack-2023/blob/main/GCP%20Data%20Engineer.md)
	- [GCP Machine Learning Engineer](https://github.com/huang-pan/modern-data-stack-2023/blob/main/GCP%20Machine%20Learning%20Engineer.md)
	- [Azure Databricks Data / ML Engineer](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Azure%20Data%2C%20ML%20Engineer.md)
	- [Generative AI](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Generative%20AI.md)

The courses above are all up to date for 2023. I took the courses above just to fill in any gaps in my background knowledge and refresh my skill set. I would say that generally, the courses are like tutorial / introductory courses. They have given me enough background knowledge on where to start for any of my future projects. I will go into more depth and really understand the technologies when I work on the actual projects. This is not a problem for me as I'm an experienced data engineer. I've already worked with many tools of the Modern Data Stack already and have learned how to use many technologies on the job in the past. Picking up and applying new technologies is one of my main strengths.

For future research on the latest data tooling:
- see CMU Advanced Database Systems https://www.youtube.com/@CMUDatabaseGroup/playlists
- https://github.com/andresvourakis/data-scientist-handbook
- [Data 2025Q1.pdf](https://github.com/user-attachments/files/20613787/Data.2025Q1.pdf)


## DBT / Data Warehousing
#### Courses taken
- [Udemy Data Build Tool](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/)
#### Summary
- This is a refresher course on data modeling in the data warehouse with the DBT framework.
	- Some notes on: query optimization framework
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Data%20Warehouse%2C%20DBT.md)
- Github repo: https://github.com/huang-pan/complete-dbt-bootcamp-zero-to-hero
#### Certificates of Completion
- Udemy DBT completed [May 20, 2023](https://www.udemy.com/certificate/UC-de00a2d0-a8a1-4319-8101-bbea3cb3cc5b/)

## Spark / Databricks
#### Courses taken
- [Udemy PySpark](https://www.udemy.com/course/taming-big-data-with-apache-spark-hands-on/)
- [Udemy Advanced Spark 3+](https://www.udemy.com/course/apache-spark-3-beyond-basics/)
- [Databricks Data and AI Summit 2023](https://www.youtube.com/watch?v=PIFL7W3DmaY&list=PLTPXxbhUt-YW6v14Vs3sTx6cyK5URKKgO)
#### Summary
- The Udemy PySpark course is a refresher course on PySpark.
- I learned how Spark works under the hood and how to optimize Spark jobs with the Advanced Spark 3+ course.
- The [Databricks Data and AI Summit 2023 videos](https://www.youtube.com/watch?v=PIFL7W3DmaY&list=PLTPXxbhUt-YW6v14Vs3sTx6cyK5URKKgO) of the conference was a great introduction to the modern Databricks platform and integrated development environment. The Databricks platform is currently state of the art. It is a comprehensive platform that unifies data engineering and machine learning development. Features include unified batch and stream processing on Delta Live Tables, declarative pipelines with infrastructure autoscaling, [pyspark.ai](http://pyspark.ai/), Databricks Workflows, LLM model serving / LLMOps, Unity Catalog for data / ML governance, Photon, etc.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Databricks%2C%20Spark.md)
#### Certificates of Completion
- Udemy PySpark completed [May 20, 2023](https://www.udemy.com/certificate/UC-c069b4b8-3a68-46e9-a591-f8c1c5a72b50/)
- Udemy Advanced Spark 3+ completed [May 25, 2023](https://www.udemy.com/certificate/UC-230f3948-d2f2-405a-9f55-3c0f151db965/)

## Kafka / KSQL
#### Courses taken
- [Udemy Kafka](https://www.udemy.com/course/apache-kafka/)
- [Udemy KSQL](https://www.udemy.com/course/kafka-ksql/)
#### Summary
- I learned how Kafka works and how to build streaming analytics solutions with Kafka and KSQL.
- After you learn Kafka, all the streaming analytics technologies on AWS (Kinesis), Azure (Event Hubs / Stream Analytics), and GCP (Pub/Sub / Dataflow) are similar.
- I also do a comparison of streaming technologies (Kafka, Flink, Spark Streaming, etc.)
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Kafka%2C%20KSQL.md)
#### Certificates of Completion
- Udemy Kafka completed [May 26, 2023](https://www.udemy.com/certificate/UC-82d2aa28-046b-4b71-afe2-8f6e593d490a/)
- Udemy KSQL completed [May 26, 2023](https://www.udemy.com/certificate/UC-510b1e24-cc7f-40a8-bb30-a96b6acf8d31/)

## FastAPI
#### Courses taken
- [Udemy FastAPI](https://www.udemy.com/course/completefastapi/)
#### Summary
- This course is useful if I need to build a basic REST API with Python to serve up data. I learned about the basics of API development using FastAPI: CRUD operations, routes, models, schemas, database connections, etc.
- I focused on the back end related portions of this course and skipped all the front end sections.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/FastAPI.md)
#### Certificates of Completion
- Udemy FastAPI completed [May 20, 2023](https://www.udemy.com/certificate/UC-f91bde24-2803-4e24-beba-7e2f3963c9d6/)

## AWS Data Engineer
#### Courses taken
- [Udemy Amazon Web Services Data Engineer](https://www.udemy.com/course/aws-data-analytics)
#### Summary
This course is a top level overview of all the AWS services related to data engineering. This course was mainly review for me as I have worked with many AWS services before in production. Services covered include:
- S3
- Redshift / Athena
- Kinesis
- EMR (Managed Spark, etc.)
- DynamoDB
- Glue
- Lambda
- Quicksight
- MWAA (Managed Workflows for Apache Airflow)
- EKS (Elastic Kubernetes Service)
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/AWS%20Data%20Engineer.md)
#### Certificates of Completion
- Udemy AWS Data Engineer completed [June 1, 2023](https://www.udemy.com/certificate/UC-634381db-3681-4d2e-8525-98205f7ac624/)

## AWS Machine Learning Engineer
#### Courses taken
- [Udemy Amazon Web Services ML Engineer](https://www.udemy.com/course/aws-machine-learning)
#### Summary
- This course is a top level overview of all the AWS services related to machine learning. I mainly focused on the AWS Sagemaker Studio (ML development environment) sections of this course - the parts relevant to MLOps. Honestly, the machine learning development environments of AWS (Sagemaker), Azure (Machine Learning), and GCP (Vertex AI) are all similar.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/AWS%20ML%20Engineer.md)
#### Certificates of Completion
- Udemy AWS ML Engineer completed [June 3, 2023](https://www.udemy.com/certificate/UC-9115613e-cdc4-4ef8-836b-3198f5765b5f/)

## GCP Data Engineer
#### Courses taken
- [Google Cloud Data Engineer Learning Path](https://www.cloudskillsboost.google/paths/16)
#### Summary
The GCP Data Engineer learning path consists of lectures, quizzes, and labs working with all GCP services related to data engineering. I used following GCP services in the labs:
- BigQuery
- Dataflow (both batch and streaming ETL / analytics)
- Pub/Sub
- Cloud Storage
- Cloud Dataproc (Managed Spark, etc.)
- Bigtable
- Cloud Composer (Managed Airflow)
- Cloud Build (CI/CD for data pipelines)
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/GCP%20Data%20Engineer.md)
#### Certificates of Completion
- Preparing for the Google Cloud Professional Data Engineer Exam completed [June 28, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4161331)
- Google Cloud Big Data and Machine Learning Fundamentals completed [June 29, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4171969)
- Modernizing Data Lakes and Data Warehouses with Google Cloud completed [June 29, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4172371)
- Building Batch Data Pipelines on Google Cloud completed [July 1, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4182084)
- Building Resilient Streaming Analytics Systems on Google Cloud completed [July 2, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4187773)
- Smart Analytics, Machine Learning, and AI on Google Cloud completed [July 2, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4191832)
- Serverless Data Processing with Dataflow: Foundations completed [July 2, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4191948)
- Serverless Data Processing with Dataflow: Develop Pipelines completed [July 2, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4193692)
- Serverless Data Processing with Dataflow: Operations completed [July 4, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4204812)

## GCP Machine Learning Engineer
#### Courses taken
- [Google Cloud Machine Learning Engineer Learning Path](https://www.cloudskillsboost.google/paths/17)
#### Summary
- The GCP ML Engineer learning path consists of lectures, quizzes, and labs working with all GCP services related to machine learning. I mainly focused on the Vertex AI (ML development environment) and Cloud Build (CI / CD / CT for ML) sections of this course - the parts relevant to MLOps. I also learned how to build neural networks with Tensorflow / Keras from this course - good background knowledge to have.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/GCP%20Machine%20Learning%20Engineer.md)
#### Certificates of Completion
- How Google Does Machine Learning completed [July 5, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4222516)
- Launching into Machine Learning completed [July 5, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4223005)
- TensorFlow on Google Cloud completed [July 6, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4232587)
- Feature Engineering completed [July 6, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4233166)
- Machine Learning in the Enterprise completed [July 10, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4259057)
- Production Machine Learning Systems completed [July 6, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4233637)
- Machine Learning Operations (MLOps): Getting Started completed [July 8, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4243516)
- ML Pipelines on Google Cloud completed [July 11, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4271248)

## Azure Databricks Data Engineer, MlOps, Terraform, Kubernetes, etc.
#### Courses taken
- [Azure Databricks & Spark For Data Engineers (PySpark / SQL)](https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/)
- [Azure Databricks and Spark SQL](https://www.udemy.com/course/azure-databricks-and-spark-sql-python/ )

Just basic tutorial / background knowledge on the below topics:
- Terraform
- Kubernetes
- MlOps
- Streamlit
- Airflow vs. Dagster vs. Prefect; Snowflake

#### Summary
- The Udemy Azure and Databricks courses were very helpful for understanding the latest Databricks offerings on Azure. Services of note are:
 	- Databricks Delta Lake / Delta Live Tables
  		- Delta Lake vs Iceberg vs Hudi
	- Databricks Unity Catalog
  	- Azure Data Factory / Data Lake
  	- Azure Devops, Databricks CI/CD
- Azure data engineering / ML related services are similar to AWS and GCP services. I've used some Azure services in production before.
	- Azure Data Lake gen 2
	- Azure SQL (cloud MS SQL Server)
	- Azure Cosmos DB (like Mongo DB, Dynamo DB, Bigtable)
	- Azure Synapse Analytics
	- Azure Data Factory
	- Azure Stream Analytics
 	- Azure Databricks
	- Azure HDInsight (Hadoop, Spark, Kafka)
- I also updated my knowledge on Airflow 2+, Dagster, Prefect, Kubernetes, Terraform, Streamlit, etc.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Azure%20Data%2C%20ML%20Engineer.md)
#### Certificates of Completion
- Azure Databricks & Spark For Data Engineers (PySpark / SQL) [August 16, 2023](https://www.udemy.com/certificate/UC-953b1ee6-3645-4797-8e02-d68b14d0dca2/)
- Azure Databricks and Spark SQL [August 17, 2023](https://www.udemy.com/certificate/UC-f9306a42-9538-4dd1-9ee6-7633cb069371/)

## Generative AI
#### Courses taken
- [Google Cloud Generative AI learning path](https://www.cloudskillsboost.google/journeys/118)
- [Stanford Professor Andrew Ng Generative AI Short Courses](https://www.deeplearning.ai/short-courses/)
#### Summary
- The courses on Generative AI was just good background knowlege to have, in case I ever need to build any applications using prompting with language chains on Large Language Models (LLMs), etc.
- [Course Notes](https://github.com/huang-pan/modern-data-stack-2023/blob/main/Generative%20AI.md)
#### Certificates of Completion
- Introduction to Generative AI completed [May 23, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3737950)
- Introduction to Large Language Models completed [May 23, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3738003)
- Introduction to Responsible AI completed [June 4, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3815915)
- Generative AI Fundamentals completed [June 6, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3861709 )
- Introduction to Image Generation: diffusion models completed [May 30, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787142)
- Encoder-Decoder Architecture: translation, text summarization, Q&A completed [May 30, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787392)
- Attention Mechanism completed [May 28, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3766502 )
- Transformer Models and BERT Model completed [May 30, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787108)
- Create Image Captioning Models completed [May 30, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787318)
- Introduction to Generative AI Studio completed [June 27, 2023](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4150368)
- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Langchain for LLM Application Development](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)
- [Langchain Chat with Your Data](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
