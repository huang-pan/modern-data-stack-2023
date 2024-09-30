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
- TurboML: real time ML platform https://turboml.com/
- Inferyx: low code AI dev platform https://www.inferyx.com/
- Runhouse: https://www.run.house/
	- Serverless ML Training in Your Own Cloud
	- A PyTorch Approach to ML Infrastructure https://www.youtube.com/watch?v=jU6ylex9jqE

## MLOps 101
- https://www.youtube.com/watch?v=IYySKhioMTM
![Screenshot_20240618-170606_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e3c5844b-2ab8-406e-9961-fefd7cd0ebfb)
![Screenshot_20240618-170731_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f7d66f7e-d57f-4d7c-81f0-bc5383f465fc)
![Screenshot_20240618-170819_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cbc8b5d5-e8ed-4ba9-9f5e-75d1dbac65c4)
![Screenshot_20240618-170842_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5e2b375c-4a4e-4aa5-8e64-d40bd4240f62)
![Screenshot_20240618-170905_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/013bb6dd-ecee-47ae-92fe-d6274d73b3c9)

## MLOps for different company stages
- https://www.youtube.com/watch?v=YvjqScBwjPs
	- ****Biggest MLOps challenges****: 1. cleaned, versioned data 2. deploying 3. monitoring
![Screenshot_20240705-212727_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/eb678c09-af0d-49b9-b43d-f42c17d61f83)
![Screenshot_20240705-212701_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c23446e3-20e2-4882-a629-1a5c9a3e8acd)
![Screenshot_20240705-213119_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/af03a47b-a12f-48f4-9981-87b8ef37e546)
![Screenshot_20240705-213234_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e64ad30a-b54c-4b62-afa2-5c31e96e8f71)
![Screenshot_20240705-213251_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2dad74ca-8c4f-4e16-9604-ab3e00e6d7b6)
![Screenshot_20240705-213327_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b3b7a76b-59e2-4bd0-b8e6-183b211eb0fc)
![Screenshot_20240705-213340_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/159bddfc-e4a9-4d72-affb-d0f813d81995)
![Screenshot_20240705-213406_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6cfd9813-5f9e-4370-98f4-633bf22ed180)
![Screenshot_20240705-213423_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c758a28a-442a-4dc9-bf3c-3759375b1c31)
![Screenshot_20240706-082059_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e4937de-e641-4703-b547-203d35610ed5)
![Screenshot_20240705-213438_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2ced95b7-561e-4dfe-8df2-01307abddaaf)

## The State of Production ML
- 2024 https://www.youtube.com/live/AtA2XXo_b5s
- 2023 https://www.youtube.com/watch?v=iMiFA_rITHI
![Screenshot_20240729-100531_YouTube](https://github.com/user-attachments/assets/8b250cc7-6f1e-420f-932f-5426a3638071)
![Screenshot_20240729-100534_YouTube](https://github.com/user-attachments/assets/70c49ef4-ee41-46d4-9e44-c037d0a7b889)
![Screenshot_20240729-100542_YouTube](https://github.com/user-attachments/assets/b07fed00-8702-4270-80ca-1748f623cc9e)
![Screenshot_20240729-100552_YouTube](https://github.com/user-attachments/assets/763a672d-e063-4e26-a85c-207bda854812)
![Screenshot_20240729-100557_YouTube](https://github.com/user-attachments/assets/8df5ac04-7b2a-4f86-a8f4-c58554daadce)
![Screenshot_20240729-100650_YouTube](https://github.com/user-attachments/assets/87085802-8ce7-4ffc-a505-fbe9e91a6ff3)
![Screenshot_20240729-100730_YouTube](https://github.com/user-attachments/assets/0c337788-d84d-41ab-bb46-61ebd5f0a4b1)
![Screenshot_20240729-100749_YouTube](https://github.com/user-attachments/assets/3f6f5f41-5faa-4b9d-b2df-938d5ca3815f)
![Screenshot_20240729-100756_YouTube](https://github.com/user-attachments/assets/9060f36e-4dc4-4d36-addd-049f782481cd)
![Screenshot_20240729-100813_YouTube](https://github.com/user-attachments/assets/7aaf84b2-11c1-4e8d-8511-42150c5d4d0f)
![Screenshot_20240729-100820_YouTube](https://github.com/user-attachments/assets/cb0a1700-7a47-47c9-ab20-37b6efda7b5c)
![Screenshot_20240729-100824_YouTube](https://github.com/user-attachments/assets/c3ec3f25-d27a-4d22-be79-a6755166aa9b)
![Screenshot_20240729-100828_YouTube](https://github.com/user-attachments/assets/f81d8a5b-f341-498d-a4cd-29af1b3b9cd7)
![Screenshot_20240729-100833_YouTube](https://github.com/user-attachments/assets/742d70a2-6b67-438c-84b2-4195c3fd8118)
![Screenshot_20240729-100847_YouTube](https://github.com/user-attachments/assets/90c5d8ef-950c-4842-ae44-8a61a68eb708)
![Screenshot_20240729-100850_YouTube](https://github.com/user-attachments/assets/1a3d3813-490e-4378-8ac6-1c8366d91a2a)
![Screenshot_20240729-100855_YouTube](https://github.com/user-attachments/assets/5059ce0e-bbd5-4703-92fd-9881b411443e)
![Screenshot_20240729-100904_YouTube](https://github.com/user-attachments/assets/8d62f257-0184-4f73-afd5-83d6c06c25c8)
![Screenshot_20240729-100909_YouTube](https://github.com/user-attachments/assets/239f8895-8ad5-4462-bb4b-3a021b924628)
![Screenshot_20240729-100914_YouTube](https://github.com/user-attachments/assets/39bfda73-9a89-4b11-a0cd-ace290c949a5)
![Screenshot_20240729-100918_YouTube](https://github.com/user-attachments/assets/d03d9b5a-dfbf-4c26-88cb-c5d0672b5ba4)
![Screenshot_20240729-100924_YouTube](https://github.com/user-attachments/assets/b27907f0-bf3b-4d7b-bb67-0f3d670be774)
- https://www.youtube.com/live/sTI3kdytymY MLOps in FinTech
![Screenshot_20240713-171810_YouTube](https://github.com/user-attachments/assets/3a6ee5df-d881-47ee-8165-7e91741665c6)
![Screenshot_20240713-171817_YouTube](https://github.com/user-attachments/assets/228d5e46-f870-4bb5-ae61-c48daf222019)

## Kubeflow
- https://www.youtube.com/watch?v=OpH5wM4WGTY
![Screenshot_20240713-163504_YouTube](https://github.com/user-attachments/assets/1bb20fb9-8b47-4b1f-b0e3-40180a71ad42)
![Screenshot_20240713-163627_YouTube](https://github.com/user-attachments/assets/46287d8a-374d-4d75-8b9a-6d46ad771c55)
![Screenshot_20240713-163633_YouTube](https://github.com/user-attachments/assets/c5935788-4f48-475c-8de6-2f136c587e9c)
![Screenshot_20240713-163713_YouTube](https://github.com/user-attachments/assets/2c3eeebb-aa7e-4b71-baff-0454c99e351a)
![Screenshot_20240713-163719_YouTube](https://github.com/user-attachments/assets/70cfa138-b333-414f-b7c4-15160e8ae889)
![Screenshot_20240713-163732_YouTube](https://github.com/user-attachments/assets/c155a623-6587-4109-babc-e8037362c236)
![Screenshot_20240713-163739_YouTube](https://github.com/user-attachments/assets/d8b2238b-5998-4c52-91f1-87e530a7f536)
- https://www.youtube.com/watch?v=bddiQ21qrKY
![Screenshot_20240713-163121_YouTube](https://github.com/user-attachments/assets/7571e400-7194-4b89-933d-f349f0cefa1a)
![Screenshot_20240713-163138_YouTube](https://github.com/user-attachments/assets/7dc42e48-afd2-4198-8aaa-fa66b6b96359)
![Screenshot_20240713-163240_YouTube](https://github.com/user-attachments/assets/96791475-420b-4c6e-84d0-016c19924626)

## Weights and Biases
- https://www.youtube.com/watch?v=YYGRBbf3bWI
![Screenshot_20240712-064047_YouTube](https://github.com/user-attachments/assets/86fe28fa-5568-46ef-82ce-c601a37db0d9)
- https://www.youtube.com/watch?v=tHAFujRhZLA
![Screenshot_20240801-101245_YouTube](https://github.com/user-attachments/assets/cf923837-ed5b-4777-a937-c00229ab13fe)
- https://www.youtube.com/watch?v=ZWMRIkAhcRw
![Screenshot_20240801-100837_YouTube](https://github.com/user-attachments/assets/327dcd05-6d34-4857-a89f-91cd502c18d6)
![Screenshot_20240801-101032_YouTube](https://github.com/user-attachments/assets/3db8b470-ce9f-49d5-98fa-c92b84deed86)
- https://www.youtube.com/watch?v=RGLh4IdaOT4  demo of W&B
![Screenshot_20240801-133146_YouTube](https://github.com/user-attachments/assets/d198f8ab-c4a3-4a57-8848-86e059eb4f38)
![Screenshot_20240801-133155_YouTube](https://github.com/user-attachments/assets/a9470cff-6050-4d87-bba3-e9a93a651204)
![Screenshot_20240801-133200_YouTube](https://github.com/user-attachments/assets/b3be2613-0339-4708-89e6-d58f741cd0d2)
![Screenshot_20240801-133209_YouTube](https://github.com/user-attachments/assets/719b5854-99ac-4f11-9d2e-7a7d0050dfe1)
![Screenshot_20240801-133210_YouTube](https://github.com/user-attachments/assets/06a5624e-2e73-48be-872d-a6a54c75a68e)
![Screenshot_20240801-133346_YouTube](https://github.com/user-attachments/assets/0910a3aa-2d2a-404f-8b9d-9d9dc1d31c99)
![Screenshot_20240801-133501_YouTube](https://github.com/user-attachments/assets/ac94c64e-4e5c-4444-a2ad-ff0aa262927b)
![Screenshot_20240801-133509_YouTube](https://github.com/user-attachments/assets/7fadbadf-7b23-46af-a982-4969d0053cc9)
![Screenshot_20240801-133524_YouTube](https://github.com/user-attachments/assets/f5c27c95-25d2-4f8c-9f0a-653fdfa01176)
![Screenshot_20240801-133542_YouTube](https://github.com/user-attachments/assets/7a327c40-19e2-4749-b8fb-ece8f821d78b)
![Screenshot_20240801-133548_YouTube](https://github.com/user-attachments/assets/21e3fec2-33b2-464d-8eb9-6f15d1c2549d)
![Screenshot_20240801-133556_YouTube](https://github.com/user-attachments/assets/d3c33016-acdc-4a48-ba1a-2df9631d3cd6)
![Screenshot_20240801-133600_YouTube](https://github.com/user-attachments/assets/b418091e-4c46-4d3f-a6fa-05dd3298f871)
![Screenshot_20240801-133610_YouTube](https://github.com/user-attachments/assets/f20813d2-e476-41f9-8d27-0b2d22303b30)
![Screenshot_20240801-133622_YouTube](https://github.com/user-attachments/assets/c6648a1c-9aa5-47b5-8e3d-f1287d291a3b)
![Screenshot_20240801-133712_YouTube](https://github.com/user-attachments/assets/886195f3-6306-4c13-8ee5-4258bbbee0f5)
- https://www.youtube.com/watch?v=QMQPnAkZFOE CD from W&B model registry
![Screenshot_20240801-134628_YouTube](https://github.com/user-attachments/assets/e9289fc2-27b3-4129-a784-72dcfa5f5ffc)
![Screenshot_20240801-134638_YouTube](https://github.com/user-attachments/assets/02061553-a2dc-4a5d-b445-6936ac5de32f)
![Screenshot_20240801-134709_YouTube](https://github.com/user-attachments/assets/0dd591c3-20d8-4638-8787-2ceaefa8a629)
![Screenshot_20240801-134729_YouTube](https://github.com/user-attachments/assets/e144586d-3df9-480f-8eca-d3551f058e74)

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

## ArangoML
- https://www.youtube.com/watch?v=5xW8u1RF29U
![Screenshot_20240709-073847_YouTube](https://github.com/user-attachments/assets/beb63373-58d2-4a8f-b5d5-4c6b95efb7b4)
![Screenshot_20240709-074017_YouTube](https://github.com/user-attachments/assets/11742dac-a586-4e8f-b5ec-45f9e41c90d2)
![Screenshot_20240709-074040_YouTube](https://github.com/user-attachments/assets/5911f69b-de98-4a56-b7f6-ddf9a7d16c63)
![Screenshot_20240709-074342_YouTube](https://github.com/user-attachments/assets/76cc21ca-5c83-418b-89e9-d6841d79d775)
![Screenshot_20240709-074355_YouTube](https://github.com/user-attachments/assets/3c84160c-c360-45ea-9295-e5920f8167e2)
![Screenshot_20240709-074413_YouTube](https://github.com/user-attachments/assets/5f6e1fa3-11e9-4f70-b2b8-305db02fe5ad)
![Screenshot_20240709-074559_YouTube](https://github.com/user-attachments/assets/eb9394be-8e17-490e-bfc9-c6c74291a5b4)
![Screenshot_20240709-074635_YouTube](https://github.com/user-attachments/assets/2ca097f8-b1f6-4c1d-aa96-c691a2fb2241)
![Screenshot_20240709-074648_YouTube](https://github.com/user-attachments/assets/225f43ac-ae2e-4dac-9baa-8885d1bd9614)
![Screenshot_20240709-074705_YouTube](https://github.com/user-attachments/assets/7fb1824d-a06c-4f3c-b773-43e3c7d6bb3f)
![Screenshot_20240709-074720_YouTube](https://github.com/user-attachments/assets/952bfff5-1084-4e7e-9940-3571a2163a32)
![Screenshot_20240709-074753_YouTube](https://github.com/user-attachments/assets/a511bb9d-3834-4214-ba81-7585891bf2fb)

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

## MLOps with Hopsworks Feature Store
- https://www.youtube.com/watch?v=vADvw4-XOlU
![Screenshot_20240711-185030_YouTube](https://github.com/user-attachments/assets/e5d5a177-8fc2-4759-8266-b34d84c8984e)
![Screenshot_20240711-185100_YouTube](https://github.com/user-attachments/assets/82f0f2f0-4f62-4843-8b4c-f031602e5225)
![Screenshot_20240711-185119_YouTube](https://github.com/user-attachments/assets/ba8c3bbf-7261-4103-94bd-2759248a2225)
![Screenshot_20240711-185133_YouTube](https://github.com/user-attachments/assets/985c9f00-8fbd-4600-80f5-59e38bb2a6bc)
![Screenshot_20240711-185145_YouTube](https://github.com/user-attachments/assets/b8da9cda-cbea-464d-b606-fdd5ef3f07f2)
![Screenshot_20240711-185225_YouTube](https://github.com/user-attachments/assets/208c490f-61f7-487b-a137-369d815ebbc8)
![Screenshot_20240711-185235_YouTube](https://github.com/user-attachments/assets/1400b1c0-a751-49a1-a73c-df328b775b42)
![Screenshot_20240711-185245_YouTube](https://github.com/user-attachments/assets/213c0eda-296b-4ede-82c2-7a7ad24cb36e)
![Screenshot_20240711-185256_YouTube](https://github.com/user-attachments/assets/1728c568-d52c-4824-8cd8-788f574c4b87)
![Screenshot_20240711-185305_YouTube](https://github.com/user-attachments/assets/a7af78af-54f6-4a3a-a269-8bc735d8bc63)
![Screenshot_20240711-185320_YouTube](https://github.com/user-attachments/assets/bee7b096-2bb0-4bad-bb17-b226c520a072)
![Screenshot_20240711-185335_YouTube](https://github.com/user-attachments/assets/5ca71e67-6e7c-47d9-9bc4-053f3737c60f)
![Screenshot_20240711-185349_YouTube](https://github.com/user-attachments/assets/8d724234-4c9b-4b2a-b421-ae4e83b81a9b)
![Screenshot_20240711-185353_YouTube](https://github.com/user-attachments/assets/7bfc91b3-2b7c-454e-b99c-992fcaf27241)
![Screenshot_20240711-185402_YouTube](https://github.com/user-attachments/assets/65658d16-292b-46a7-b3a6-b2ab03d6aa7c)
![Screenshot_20240711-185416_YouTube](https://github.com/user-attachments/assets/2cd8b781-cd05-491d-b7fd-b4565bbb982c)
![Screenshot_20240711-185422_YouTube](https://github.com/user-attachments/assets/36e0a9cf-313d-4d53-9a72-380890efe19d)
![Screenshot_20240711-185427_YouTube](https://github.com/user-attachments/assets/f88249dc-9678-4600-9379-cb461c866678)
![Screenshot_20240711-185432_YouTube](https://github.com/user-attachments/assets/4b4c0eeb-559d-4982-937d-d2ca098bdea7)
![Screenshot_20240711-185436_YouTube](https://github.com/user-attachments/assets/7686633b-9ede-4929-88bb-09b2eb1c5582)
![Screenshot_20240711-185450_YouTube](https://github.com/user-attachments/assets/162aedaf-53b7-42a1-a272-98fe350bdcc2)
![Screenshot_20240711-185453_YouTube](https://github.com/user-attachments/assets/7d35d5bb-9082-40c1-a97d-f070f2041156)
![Screenshot_20240711-185503_YouTube](https://github.com/user-attachments/assets/732228f4-c7fc-4aa3-b08d-f56837766211)
![Screenshot_20240711-185509_YouTube](https://github.com/user-attachments/assets/9197b4f2-cc12-438d-a78a-4c34b46274ce)
![Screenshot_20240711-185512_YouTube](https://github.com/user-attachments/assets/fa673893-0a15-4a54-a068-ed148aa2821e)
![Screenshot_20240711-185517_YouTube](https://github.com/user-attachments/assets/3625c04e-18f8-4581-8422-d4e01b1cb83b)
![Screenshot_20240711-185521_YouTube](https://github.com/user-attachments/assets/71a4db57-bfa2-4224-a75c-f6c167b1c596)
![Screenshot_20240711-185524_YouTube](https://github.com/user-attachments/assets/5a05711e-733c-4a24-89e5-6aff9179fa90)
![Screenshot_20240711-185529_YouTube](https://github.com/user-attachments/assets/81ec0b94-32dd-4488-91d0-cac7bdebc88c)
![Screenshot_20240711-185537_YouTube](https://github.com/user-attachments/assets/be04e928-08e5-481f-87c2-6559fa3566ad)
![Screenshot_20240711-185544_YouTube](https://github.com/user-attachments/assets/08f05ad9-b2e7-4fc6-ac4a-c8a697ec3b30)

## MLOps CICD
- https://www.youtube.com/live/jZOOvtX_T5Q
![Screenshot_20240713-165850_YouTube](https://github.com/user-attachments/assets/a528453a-dcf8-44c4-8c11-f5626f946797)
![Screenshot_20240713-170010_YouTube](https://github.com/user-attachments/assets/0f85f43e-0492-460e-abe6-e06143be08d4)
![Screenshot_20240713-170117_YouTube](https://github.com/user-attachments/assets/924e88d4-e1aa-43a4-b072-d52c2c0fffd3)
![Screenshot_20240713-170216_YouTube](https://github.com/user-attachments/assets/8e03b2ef-6268-4970-b4fe-3c4ddd2e5e0f)
![Screenshot_20240713-170230_YouTube](https://github.com/user-attachments/assets/ad19c52d-37b1-4b51-923c-b3ead7750141)
![Screenshot_20240713-170245_YouTube](https://github.com/user-attachments/assets/4bc3d66d-2be2-4c24-a086-ab05510e4f82)

## MLOps testing, monitoring
- https://www.youtube.com/watch?v=j4wZmywPs1E
![Screenshot_20240713-180849_YouTube](https://github.com/user-attachments/assets/9a63cc5e-5fbb-4390-87a8-d654a665595f)
![Screenshot_20240713-180902_YouTube](https://github.com/user-attachments/assets/692d71ef-8204-4923-86a1-4a2e10010fb6)
![Screenshot_20240713-180934_YouTube](https://github.com/user-attachments/assets/c2e0c834-9e35-4209-9bc0-2984443f224f)
![Screenshot_20240713-180943_YouTube](https://github.com/user-attachments/assets/e509a250-04c4-447e-9069-79fc3573557f)
![Screenshot_20240713-180953_YouTube](https://github.com/user-attachments/assets/fc2fe37d-5dd5-4edf-99a3-9fa43cb2b00f)
![Screenshot_20240713-180959_YouTube](https://github.com/user-attachments/assets/a1a9b4a4-ac93-4924-aaee-3e12e68fac7f)
![Screenshot_20240713-181007_YouTube](https://github.com/user-attachments/assets/bc4d1b77-3087-43ef-8736-2aa36074ab82)
![Screenshot_20240713-181024_YouTube](https://github.com/user-attachments/assets/a1e09a0f-de2d-40ab-8129-4f0a45d2e9a6)
![Screenshot_20240713-181027_YouTube](https://github.com/user-attachments/assets/b2182809-beca-42f6-b71c-ddb39601a296)
![Screenshot_20240713-181055_YouTube](https://github.com/user-attachments/assets/aaf3d793-5471-4d5a-98d3-7c08b6f08276)
![Screenshot_20240713-181105_YouTube](https://github.com/user-attachments/assets/599dfe0e-f91f-4983-9087-b3bd244acdb1)
![Screenshot_20240713-181113_YouTube](https://github.com/user-attachments/assets/69ea1dcd-20e9-4e84-b4f1-004733c32c5a)
![Screenshot_20240713-181116_YouTube](https://github.com/user-attachments/assets/7d96303f-d1ed-4967-a3dd-7d8bee65efed)
![Screenshot_20240713-181126_YouTube](https://github.com/user-attachments/assets/aa1655d8-1d83-4906-8b27-d7b33d18e7d6)
![Screenshot_20240713-181134_YouTube](https://github.com/user-attachments/assets/b83f654a-a273-4307-a2f5-dc06abe98f2d)
![Screenshot_20240713-181140_YouTube](https://github.com/user-attachments/assets/afe36421-01a0-469b-bdce-4214ef116536)
![Screenshot_20240713-181149_YouTube](https://github.com/user-attachments/assets/4f69bb9a-ce36-49c4-9409-10eecee764be)
![Screenshot_20240713-181158_YouTube](https://github.com/user-attachments/assets/88a89e8c-2d58-4ad9-b379-b1ded20bc5cf)
![Screenshot_20240713-181219_YouTube](https://github.com/user-attachments/assets/ea03341a-3fda-4431-bab7-7ac35ea47d5f)
![Screenshot_20240713-181231_YouTube](https://github.com/user-attachments/assets/0e39b554-9a4f-41d8-907d-939f903ce212)
![Screenshot_20240713-181237_YouTube](https://github.com/user-attachments/assets/9d002385-9cf8-4d1f-ac93-9b90e8c7b685)
![Screenshot_20240713-181244_YouTube](https://github.com/user-attachments/assets/88fb4255-60f9-4e99-bb17-584f22de46c4)
![Screenshot_20240713-181249_YouTube](https://github.com/user-attachments/assets/187a72f4-0d83-44f7-a459-df9a60ac298a)
![Screenshot_20240713-181255_YouTube](https://github.com/user-attachments/assets/2309d142-c355-46bc-8df8-6211de457c00)
![Screenshot_20240713-181304_YouTube](https://github.com/user-attachments/assets/89e1deb4-f04c-4248-8b6c-65574e061c6f)
![Screenshot_20240713-181311_YouTube](https://github.com/user-attachments/assets/074d6e1d-7f99-414c-94da-36c84433575c)
![Screenshot_20240713-181320_YouTube](https://github.com/user-attachments/assets/e1f0aed4-19bc-40d1-ba36-618dc1eefaac)
![Screenshot_20240713-181335_YouTube](https://github.com/user-attachments/assets/d80b4919-3975-4d42-9adf-a972eb6f82f8)
![Screenshot_20240713-181339_YouTube](https://github.com/user-attachments/assets/dd40357d-0aa1-44f1-a5db-b6d88721fc99)
![Screenshot_20240713-181404_YouTube](https://github.com/user-attachments/assets/29a498f8-34ed-4320-b821-cc88d33d286d)
![Screenshot_20240713-181416_YouTube](https://github.com/user-attachments/assets/c2842861-93d9-43b2-b499-adfffe15aba4)
![Screenshot_20240713-181425_YouTube](https://github.com/user-attachments/assets/f1f3b64d-c5b6-42c0-963f-d32e5d649740)
![Screenshot_20240713-181430_YouTube](https://github.com/user-attachments/assets/b2e8e0eb-7341-4601-8e69-b98ecb5c87bb)
