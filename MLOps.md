# MLOps

See Feature Store notes https://github.com/huang-pan/modern-data-stack-2023/blob/main/Feature%20Store.md

## General Notes
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
	- https://www.snowflake.com/blog/ml-enhances-mlops-streaming-feature-model-management/
		- ****Snowflake ML has a model registry and feature store****
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
- Eppo
	- https://www.geteppo.com/
	- End to end experimentation platform for A/B testing, integrates with MDS
	- [Building a Modern Experimentation Stack (Eppo).pdf](https://github.com/user-attachments/files/15825712/Building.a.Modern.Experimentation.Stack.Eppo.pdf)

## MLOps for different company stages
- https://www.youtube.com/watch?v=YvjqScBwjPs
![Screenshot_20240705-212701_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c23446e3-20e2-4882-a629-1a5c9a3e8acd)
![Screenshot_20240705-212727_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/eb678c09-af0d-49b9-b43d-f42c17d61f83)
![Screenshot_20240705-213119_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/af03a47b-a12f-48f4-9981-87b8ef37e546)
![Screenshot_20240705-213234_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e64ad30a-b54c-4b62-afa2-5c31e96e8f71)
![Screenshot_20240705-213251_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2dad74ca-8c4f-4e16-9604-ab3e00e6d7b6)
![Screenshot_20240705-213327_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b3b7a76b-59e2-4bd0-b8e6-183b211eb0fc)
![Screenshot_20240705-213340_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/159bddfc-e4a9-4d72-affb-d0f813d81995)
![Screenshot_20240705-213406_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6cfd9813-5f9e-4370-98f4-633bf22ed180)
![Screenshot_20240705-213423_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c758a28a-442a-4dc9-bf3c-3759375b1c31)
![Screenshot_20240706-082059_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e4937de-e641-4703-b547-203d35610ed5)
![Screenshot_20240705-213438_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2ced95b7-561e-4dfe-8df2-01307abddaaf)

## MLOps on Azure Databricks
- https://www.youtube.com/watch?v=qg7rTM8qVoM
![Screenshot_20240703-064957_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6b804fb5-5834-465b-b35c-4050be5e2997)
![Screenshot_20240703-065014_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fd8315ff-4f14-4b00-8460-b4ee486193c7)
![Screenshot_20240703-065047_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e0b181d8-4bb9-45e7-b201-fd0c9e3cb693)
![Screenshot_20240703-065109_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e9e82946-ed3e-4e50-8e62-88bc64ba0fca)
![Screenshot_20240703-065124_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ac106d27-e5de-4911-a626-4d71ea46a643)
![Screenshot_20240703-065218_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/015e7e80-461a-4e5e-a1e0-8383ded1e24e)
![Screenshot_20240703-065221_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ac459b1c-d68f-4a1e-b772-0897b5555f23)
![Screenshot_20240703-065301_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0d90b787-e356-43ac-9f42-d1a6a2590572)
![Screenshot_20240703-065309_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/11243e68-8c97-4a01-8380-52dbc80979d9)
![Screenshot_20240703-065338_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2f1539fc-c7e3-48f7-941e-65957005f414)
![Screenshot_20240703-065426_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/02e8ce51-d7f7-44be-a60b-5c29c2a2ed29)
![Screenshot_20240703-065432_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4d5cb49-d12d-4b03-aa94-612bed929675)

## MLOps in Enterprise (older, cludgy solution)
https://www.youtube.com/watch?v=iENEd59Rrqs
<img width="1792" alt="Screenshot 2024-06-04 at 10 13 40 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/387b29b7-d7cf-445d-b118-52426d40fd6c">
<img width="1792" alt="Screenshot 2024-06-04 at 10 33 56 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e17d910b-1489-4736-9a45-7a00a88dd7bc">
<img width="1792" alt="Screenshot 2024-06-04 at 10 34 25 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a21eff08-60a3-4693-800b-420eab36a3b9">
<img width="1792" alt="Screenshot 2024-06-04 at 10 34 43 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0b248dd1-ae0b-4c11-902b-9f945e13a9d0">
<img width="1792" alt="Screenshot 2024-06-04 at 10 35 10 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bcf405e4-366f-4707-8bbb-0df05232d72a">
<img width="1792" alt="Screenshot 2024-06-04 at 10 41 17 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c90e539c-0e5b-41d1-b6a8-5527838daca6">
<img width="1792" alt="Screenshot 2024-06-04 at 10 43 39 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d66ed08e-185c-4d24-bd3e-167cd72d17d3">
<img width="1792" alt="Screenshot 2024-06-04 at 10 45 09 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4297838-5892-4cde-8d5c-9ce016030eca">
<img width="1792" alt="Screenshot 2024-06-04 at 10 46 34 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b084b994-1b4b-40e7-962a-f92b70f729c4">
<img width="1792" alt="Screenshot 2024-06-04 at 10 47 35 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fe33ee4b-4be7-4ca3-9ba1-2c9edb3e9a62">
<img width="1792" alt="Screenshot 2024-06-04 at 10 49 05 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/17aef8ec-7da2-4538-8eca-7ad137c6ac6e">
<img width="1792" alt="Screenshot 2024-06-04 at 10 49 50 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5f4c4e02-5080-4754-89f2-3162f34562fe">
<img width="1792" alt="Screenshot 2024-06-04 at 10 52 00 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/eab2b738-d40d-4b29-a6e3-b617eae910f7">
<img width="1792" alt="Screenshot 2024-06-04 at 10 52 41 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2c07d392-5abf-4134-9743-66f2c081d4ca">
<img width="1792" alt="Screenshot 2024-06-04 at 10 53 15 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e9e9cd30-5b0a-4cfb-81a9-c3ecdb0be186">
<img width="1792" alt="Screenshot 2024-06-04 at 10 54 05 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e75b48b2-ada3-473a-9888-7f06f93ce12a">
<img width="1792" alt="Screenshot 2024-06-04 at 10 54 35 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e3d5dc5-7971-46dc-9b21-cf414654848d">
<img width="1792" alt="Screenshot 2024-06-04 at 10 54 55 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f1743e27-4c7d-4952-8c7d-701d676ad513">
<img width="1792" alt="Screenshot 2024-06-04 at 10 57 00 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e7245ea5-1850-4501-93ab-eee5929a1d06">
<img width="1792" alt="Screenshot 2024-06-04 at 10 58 09 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2c603e74-7700-4a8a-9cab-7b08cb4dbdb4">
<img width="1792" alt="Screenshot 2024-06-04 at 10 58 19 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a8ce432e-bf77-4aae-8c6b-512c278303e3">
<img width="1792" alt="Screenshot 2024-06-04 at 10 58 25 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/025880be-8a07-4783-a767-6142192c776a">
<img width="1792" alt="Screenshot 2024-06-04 at 10 59 03 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6189ae16-5622-4428-b86e-d68cff509a73">
<img width="1792" alt="Screenshot 2024-06-04 at 10 59 30 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bcda1cb4-a2d7-4ee5-8241-66729ba0274c">
<img width="1792" alt="Screenshot 2024-06-04 at 10 59 56 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f1d32fa6-8369-46de-8842-d3a549361c59">
<img width="1792" alt="Screenshot 2024-06-04 at 11 00 15 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/47998043-759c-4819-ba7f-cc1ee16a650d">
<img width="1792" alt="Screenshot 2024-06-04 at 11 00 30 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ddb8937-aea2-4a16-b75d-22495ab9b0a4">
<img width="1792" alt="Screenshot 2024-06-04 at 11 01 02 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d2fed310-12f7-4240-97f8-388146e697d4">
<img width="1792" alt="Screenshot 2024-06-04 at 11 03 11 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0c8e49e8-fefc-4961-8f30-2f0a6d22a02d">
<img width="1792" alt="Screenshot 2024-06-04 at 11 04 11 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a1430d49-4453-40ba-97ea-dcabc1f0752f">
<img width="1792" alt="Screenshot 2024-06-04 at 11 04 41 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f7f0172f-9fc4-42c9-8c2c-5aac8c254eb2">

https://www.youtube.com/watch?v=AdY7xyj7a28
<img width="1792" alt="Screenshot 2024-06-04 at 11 27 57 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0e5fa005-4f21-45c4-9a96-6f57a8f5b9e1">
<img width="1792" alt="Screenshot 2024-06-04 at 11 28 22 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7aa72e3d-bcd2-46fe-ac16-662c3f6cf5a3">









