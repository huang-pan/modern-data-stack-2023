# Azure Data / ML Engineer, MLOps, Kubernetes, Terraform, Streamlit

Azure Databricks & Spark For Data Engineers (PySpark / SQL)

- https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/
	- Course completion certificate: https://www.udemy.com/certificate/UC-953b1ee6-3645-4797-8e02-d68b14d0dca2/
- Azure: Data Lake gen 2, Spark clusters, notebooks & dashboards, medallion architecture, incremental loads
- Delta Lake
- Azure Data Factory
- Unity Catalog
- **How to optimize Spark workloads**: https://www.databricks.com/discover/pages/optimize-data-workloads-guide

Azure Databricks and Spark SQL

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
- CI / CD with Databricks
	- Azure Devops solution: standard git -> dev -> test -> prod pipelines
- Data Lake Table formats: https://youtube.com/live/mXitwotQaAU?feature=share
    - Apache Iceberg: most comprehensive format, supports table / catalog versioning that the other formats don't
    - Apache Hudi: event based table format, for events
    - Delta Tables: periodic log checkpoints
- Also see Apache Iceberg: https://www.linkedin.com/posts/sesha-reddy-pattem-543aa311b_apacheiceberg-datamanagementbrilliance-metadatamastery-activity-7100064046502027266-FsDs/
	- Metadata: Metadata in Iceberg comes in three forms — Metadata Files, Manifest Lists, and Manifest Files. Metadata Files store the high-level information about the dataset. Manifest Lists index all the manifest files and keep track of their changes. Manifest Files maintain the actual data files' metadata, enhancing query performance by pruning unnecessary files.
	- 📜 Schema Evolution: Evolving your data schema while keeping your workflow uninterrupted is a breeze with Iceberg. As data structures transform over time, Iceberg's schema evolution supports adding, removing, or modifying columns without breaking downstream applications.
	- 📈 Incremental Read: With Iceberg, reading only the necessary data becomes a reality. Incremental Reads enable you to fetch only the modified data, improving query efficiency and minimizing resource utilization.
	- 🔄- Change Data Capture: Iceberg’s Change Data Capture (CDC) capability empowers you to capture and replicate only the data that changes, facilitating real-time analytics and synchronization across various systems.
	- 🐄 Copy-On-Write (COW), &, Merge-On-Read (MOR): Iceberg offers two storage strategies. COW creates a new snapshot for each write operation, ensuring immutability. MOR, on the other hand, merges new data into existing files during query time, balancing performance and query cost.
	- 🌳 Hidden Partitions: Iceberg introduces hidden partitions, enabling data versioning and management without changing existing data structures. Coupled with branching, this feature facilitates parallel development and experimentation.
	- 🏷️ Tags and Branching: Tags are snapshots of your data, capturing a consistent view at a specific point in time. Alongside branching, this feature aids in managing different development stages and versions of your dataset.
	- 🚀 Migration Made: Transitioning to Iceberg is seamless due to its compatibility with existing data formats. You can incrementally migrate your data and enjoy Iceberg's advanced capabilities without major disruptions.
	- ⏳ Time Travel: Iceberg lets you travel through time! With its time-travel feature, you can access historical versions of your data, empowering forensic analysis, auditing, and debugging.
	- 📆 Snapshot Maintenance: Iceberg’s snapshot expiration feature ensures that old data versions are pruned over time, optimizing storage usage while maintaining historical integrity.


Azure Data Engineer

- [https://www.youtube.com/playlist?list=PL7ZG6NdDdT8NRHDU5shVgGjlua297bm\-H](https://www.youtube.com/playlist?list=PL7ZG6NdDdT8NRHDU5shVgGjlua297bm-H)
- Azure has a similar set of data engineering services to GCP and AWS. I went through the above lectures quickly because of this.
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

Azure ML Engineer

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

MLOps

- Building ML Platform [https://neptune.ai/blog/ml\-platform\-guide](https://neptune.ai/blog/ml-platform-guide) 
    - [https://neptune.ai/blog/mlops\-architecture\-guide](https://neptune.ai/blog/mlops-architecture-guide) 
        - event based training architecture \(push based\)
            - can be implemented in Dagster, etc. \(sensors\)
        - orchestration pull based training architecture
            - can be implemented in Dagster, etc. \(orchestration\)
        - message based training architecture
    - [https://neptune.ai/blog/mlops\-tools\-platforms\-landscape](https://neptune.ai/blog/mlops-tools-platforms-landscape) 
    - [https://neptune.ai/blog/mlops\-at\-reasonable\-scale](https://neptune.ai/blog/mlops-at-reasonable-scale) 
- Types of ML model serving
    - [https://www.linkedin.com/posts/damienbenveniste\_machinelearning\-datascience\-artificialintelligence\-activity\-7082742497596112896\-VA9N/](https://www.linkedin.com/posts/damienbenveniste_machinelearning-datascience-artificialintelligence-activity-7082742497596112896-VA9N/) 
    - [https://www.linkedin.com/feed/update/urn:li:activity:7080450427355291648/](https://www.linkedin.com/feed/update/urn:li:activity:7080450427355291648/) 
- MLOps tools
    - MLOps
        - a collaborative notebook model development environment
        - code versioning in git
        - data versioning
        - experiment tracking
        - model training \(hyperparameter tuning\) / evaluation / test pipelines
        - a feature store
        - a model registry
        - a model metadata & artifact repository
        - model serving \(online / streaming / batch / embedded inference\)
        - model monitoring
        - CI / CD / CT
    - [https://wandb.ai/site](https://wandb.ai/site)
        - [https://www.linkedin.com/company/wandb/people/](https://www.linkedin.com/company/wandb/people/) 250 people
        - a collaborative notebook model development environment
        - experiment tracking
        - model training \(hyperparameter tuning\) / evaluation / test pipelines
        - data versioning
        - a model registry
        - model monitoring
        - LLMOps \(additional\)
        - Build Apps \(additional\)
    - [https://www.comet.com/site/](https://www.comet.com/site/)
        - [https://www.linkedin.com/company/comet\-ml/people/](https://www.linkedin.com/company/comet-ml/people/) 109 people
        - experiment tracking
        - a model metadata & artifact repository
        - a model registry
        - model monitoring
        - LLMOps \(additional\)
    - [https://abacus.ai/](https://abacus.ai/)
        - [https://www.linkedin.com/company/abacusai/people/](https://www.linkedin.com/company/abacusai/people/) 102 people
        - a model registry
        - model monitoring
        - a feature store
    - [https://neptune.ai/](https://neptune.ai/)
        - [https://www.linkedin.com/company/neptuneai/people/](https://www.linkedin.com/company/neptuneai/people/) 54 people
        - experiment tracking
        - a model registry
        - a model metadata & artifact repository
    - [https://clear.ml/](https://clear.ml/)
        - open source
        - a collaborative notebook model development environment
        - data versioning
        - experiment tracking
        - model training \(hyperparameter tuning\) / evaluation / test pipelines
        - a model registry
        - model serving \(online / streaming / batch / embedded inference\)
        - model monitoring
    - MLFlow
        - experiment tracking
        - a model registry
        - model training \(hyperparameter tuning\) / evaluation / test pipelines
- ***MLOps testing***
    - https://madewithml.com/courses/mlops/testing/  
	- model testing, use pytest
 		- test fixture: common test elements shared among different tests
    - test types
	- Unit tests: tests on individual components that each have a single responsibility (ex. function that filters a list).
          - models and unit tests on cleaning data between raw and staging
        - Integration tests: tests on the combined functionality of individual components (ex. data processing).
          - not yet, need to create tests on combined / aggregated data
        - System tests: tests on the design of a system for expected outputs given inputs (ex. training, inference, etc.).
          - not yet, this is more of a MLOps thing
        - Acceptance tests: tests to verify that requirements have been met, usually referred to as User Acceptance Testing (UAT).
          - biz stakeholder feedback?        
        - Regression tests: tests based on errors we've seen before to ensure new changes don't reintroduce them.
          - should be part of feedback loop from analytics, data science, MLOps        
    - Juvo used pytest, see test fixture code
    - https://ssmertin.com/articles/strategies-for-data-quality-with-apache-spark/
    	- test for: completeness (check for missing data), consistency (data within range), uniqueness, timeliness, relevance, accuracy, validity
- Data pipeline testing https://dataqualityguru.substack.com/p/the-essential-role-of-automated-tests
	- Unit tests: Validate each logical unit or functions that are part of the ETL process. If the pipeline consists of a group of transformations, those can be tested separately using a set of input values and expected output.
	- Contract tests: Applicable for assets consumed in downstream processes. I already presented some concepts in my previous post, but the idea is to test the items from the contract: schema, semantics, references, distribution, and freshness (SLAs).
	- Data quality tests: Audit the data stored in a data asset to check for accuracy, consistency, completeness, uniqueness, and timeliness.
	- Integration tests: The flow between different data assets is correct, and there are no communication, interaction, or compatibility problems.
	- Performance tests: Assesses the resource utilization and scalability of the pipeline. This is crucial for high-volume data pipelines to meet the required SLAs.
	- End-to-end tests: Test the data pipeline as a whole, from the source to the target or output. This could be categorized as “black box” testing because there is no need to know the internal structure of the pipeline, but only the expected output given the input.
 	- pytest (mock tests, fixtures), just like at Juvo

Kubernetes tutorial

- Refresher lecture, just the basics
- [https://www.youtube.com/watch?v=X48VuDVv0do](https://www.youtube.com/watch?v=X48VuDVv0do)
- https://youtu.be/s_o8dwzRlu4
	- more concise summary of k8s architecture
	- State full sets hard to manage, easier to use db services outside k8s
- Volumes, volume mounts, persistent volume claim
	- https://www.kubermatic.com/blog/keeping-the-state-of-apps-1-introduction-to-volume-and-volumemounts/
	- https://bluexp.netapp.com/blog/cvo-blg-kubernetes-persistent-volume-claims-explained
- stateful set
	- https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/
 	- Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling. 
![k8s](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f932b21f-e33f-45d3-811a-0df5e3d610bb)



Terraform

- Refresher lecture, just the basics
- [https://www.youtube.com/watch?v=7xngnjfIlK4](https://www.youtube.com/watch?v=7xngnjfIlK4) 

Streamlit

- create data / ML web apps using python scripts
    - seems pretty straightforward
- [https://youtu.be/R2nr1uZ8ffc](https://youtu.be/R2nr1uZ8ffc)
- [https://www.youtube.com/live/YzvMpvXyUfs?feature=share](https://www.youtube.com/live/YzvMpvXyUfs?feature=share) 
- [https://youtu.be/\_wq1NbDCkL8](https://youtu.be/_wq1NbDCkL8)

Notebooks

- Hex
    - [https://www.linkedin.com/company/hex\-technologies/people/](https://www.linkedin.com/company/hex-technologies/people/) 91 people
- Deepnote
    - [https://www.linkedin.com/company/deepnote/people/](https://www.linkedin.com/company/deepnote/people/) 36 people
- Noteable
    - [https://www.linkedin.com/company/noteable\-io/people/](https://www.linkedin.com/company/noteable-io/people/) 27 people

Latest Data Tools

- Cool channel doing demos of the latest data tools: [https://www.youtube.com/@demohub/videos](https://www.youtube.com/@demohub/videos)
- Jupyter AI https://www.marktechpost.com/2023/08/06/meet-jupyter-ai-a-new-open-source-project-that-brings-generative-artificial-intelligence-to-jupyter-notebooks-with-magic-commands-and-a-chat-interface/
- ***Data Tooling cost analysis***, etc.: https://medium.com/@hugolu87

Data Product
- Understand business requirements for upcoming data ingestion work (Securities data, Master data, Positions data etc.)
	- What’s the timeline to implement the pipeline?
	- What level of testing is required e.g., Source-to-Target reconciliation, Basic Data Quality vs Functional Testing)
	- What volume of data are we dealing with?
	- How will the data be consumed once it has been hosted in the Cloud Data Lake (AWS S3) and Warehouse (Snowflake)?
- Create a data pipeline spec that covers quality checks, assumptions, business metrics, and allows stakeholders to give feedback BEFORE you start coding
   	- stakeholders / end users / areas impacted
	- data
		- upstream / source
			- data contracts?
		- downstream
			- internal tools
			- external tools
			- KPIs / metrics
			- data science / ML
		- frequency
	- level of testing
	- implementation timeline
- Build data quality checks into your pipelines using data contracts such as write-audit-publish and write unit and integration tests to catch quality errors before they enter production
- Discover the power of data lake technologies Apache Iceberg. Proper schema evolution, partitioning, and parquet file format compression!
- Level up your SQL skills by having a four-hour crash course on GROUPING SETS, window functions, and cumulative table design

KPIs
- 1st level metrics, 2nd level metrics
	- https://www.kalungi.com/blog/10-marketing-kpis-every-b2b-saas-company-should-track
	- https://userpilot.com/blog/b2b-saas-metrics/
	- https://www.chargebee.com/blog/saas-kpis/ 
- Customer Lifetime Value = Average Revenue Per Customer / Churn Rate, Customer Acquisition Cost,
	- The CLV is the amount the customer spends every month (average revenue per customer, or ARPC for short) times the expected number of months they use our platform for. A clearer way of defining CLV is by dividing the ARPC by the churn rate (the percentage of users that stop using our platform each month)
 	- https://www.interviewquery.com/questions/marketing-channel-metrics
  	- 
![kpi](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b150e889-1832-41c3-a07b-05b40fbb0dc4)



Data Contracts

In its simplest form Data Contract is an agreement between Data Producers and Data Consumers on what the Data being produced should look like, what SLAs it should meet and the semantics of it.
Data Contract should hold the following non-exhaustive list of metadata:
- Schema of the Data being Produced.
- Schema Version - Data Sources evolve, Producers have to ensure that it is possible to detect and react to schema changes. Consumers should be able to process Data with the old Schema.
- SLA metadata - Quality: is it meant for Production use? How late can the data arrive? How many missing values could be expected for certain fields in a given time period?
- Semantics - what entity does a given Data Point represent. Semantics, similar to schema, can evolve over time.
- Lineage - Data Owners, Intended Consumers.

Some Purposes of Data Contracts:
- Ensure Quality of Data in the Downstream Systems.
- Prevent Data Processing Pipelines from unexpected outages.
- Enforce Ownership of produced data closer to where it was generated.
- Improve scalability of your Data Systems.
- Reduce intermediate Data Handover Layer.

![data_contract](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee07a579-af1a-48e2-a9f8-d192fe031848)

1. Schema changes are implemented in a git repository, once approved - they are pushed to the Applications generating the Data and a central Schema Registry.
2. Applications push generated Data to Kafka Topics. Separate Raw Data Topics for CDC streams and Direct emission.
3. A Flink Application(s) consumes Data from Raw Data streams and validates it against schemas in the Schema Registry.
4. Data that does not meet the contract is pushed to Dead Letter Topic.
5. Data that meets the contract is pushed to Validated Data Topic.
6. Applications that need Real Time Data consume it directly from Validated Data Topic or its derivatives.
7. Data from the Validated Data Topic is pushed to object storage for additional Validation.
8. On a schedule Data in the Object Storage is validated against additional SLAs and is pushed to the Data Warehouse to be Transformed and Modeled for Analytical purposes.
9. Consumers and Producers are alerted to any SLA breaches.
10. Data that was Invalidated in Real Time is consumed by Flink Applications that alert on invalid schemas. There could be a recovery Flink App with logic on how to fix invalidated Data.


10 categories of tech debt:
In order of prevalence…
1. Outstanding migrations
2. Missing or incomplete documentation
3. Poor test quality or coverage
4. Poorly designed code
5. Dead or unused code
6. Code that's not aligned to current standards
7. Lack of needed expertise on a team, resulting in code that's difficult to maintain
8. Problematic dependencies
9. Incomplete migrations or upgrades
10. Out-of-date release process
