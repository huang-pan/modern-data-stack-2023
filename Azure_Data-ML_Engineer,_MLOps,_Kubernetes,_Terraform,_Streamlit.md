# Azure Data / ML Engineer, MLOps, Kubernetes, Terraform, Streamlit

Azure Databricks & Spark For Data Engineers (PySpark / SQL)

- https://www.udemy.com/course/azure-databricks-spark-core-for-data-engineers/
- Azure: Data Lake gen 2, Spark clusters, notebooks & dashboards, medallion architecture, incremental loads
- Delta Lake
- Azure Data Factory
- Unity Catalog

Azure Databricks and Spark SQL

- https://www.udemy.com/course/azure-databricks-and-spark-sql-python/ 
- Medallion Architecture, hive metastore
- Azure Data Lake Storage v2
- Spark Structure Streaming
	- **Can stream directly into a pyspark dataframe or SQL table: a LOT easier than GCP Dataflow, Kinesis Data Analytics**
- Auto Loader
	- stream into one dataframe from all files in one directory
 	- schema inference, schema evolution
- Delta Live Tables
	- Delta tables have checkpoints, including streaming tables
	- Delta Live Expectations: data quality constraints
	- enhanced autoscaling
- CI / CD with Databricks

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
