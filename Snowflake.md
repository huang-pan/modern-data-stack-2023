# Snowflake

## Snowflake
- https://medium.com/@noah.goodrich/snowflake-vs-databricks-revisited-edd8201b5799
	- Snowflake cheaper for orgs than Databricks https://squadrondata.com/databricks-vs-snowflake-org-impact-analysis/
	- https://www.fujitsu.com/au/imagesgig5/A%20Practitioners%20Guide%20to%20Databricks%20vs%20Snowflake.pdf
	- Snowfake a lot easier to use than Databricks, but hard to control costs at larger scale
 	- Databricks may require a lot of time maintaining / optimizing. But it may work well for extremely large data, see: https://blog.dataengineer.io/p/how-to-optimize-100-tb-data-pipelines
	- Try both and see what works the best for your business requirements
- https://www.linkedin.com/posts/nick-akincilar-3417945_benchmarking-snowflake-vs-spark-to-optimize-activity-7130908981018943489-_8ei/
	- Snowflake 2x faster than Spark for the same ETL process given the same compute size
- https://docs.snowflake.com/en/guides-overview 
- features
	- https://docs.snowflake.com/en/user-guide/tables-external-intro
	- https://docs.snowflake.com/en/user-guide/object-clone 
	- schema evolution
		- https://docs.snowflake.com/en/user-guide/data-load-schema-evolution
  		- This feature is limited to COPY INTO <table> statements and Snowpipe data loads. INSERT operations cannot evolve the target table schema automatically.
    		- Snowpipe Streaming data loads are not supported with schema evolution.
	- snowpipe, snowpipe streaming
	- tasks
		- https://docs.snowflake.com/en/user-guide/tasks-intro
		- A task can execute any one of the following types of SQL code:
			- Single SQL statement
			- Call to a stored procedure
			- Procedural logic using Snowflake Scripting
		- Pipelines: Tasks can be combined with table streams for continuous ELT workflows to process recently changed table rows. Streams ensure exactly once semantics for new or changed data in a table.
  		- https://julielovesdata.medium.com/value-passing-in-snowflake-tasks-3a19e10a30a4
	- Dynamic tables
		- https://docs.snowflake.com/en/user-guide/dynamic-tables-about
			- https://youtu.be/4O2_I25izIs?si=Mt_dBHBr6kM9puL2 
			- streams and tasks: imperative way of creating pipelines
				- SQL can be optimized more than dynamic tables
				- can use serverless tasks
			- dynamic tables: declarative way of creating pipelines
				- figures out merge / insert / delete statement
				- best for incremental refresh tables, not suitable for very large tables
				- no serverless option
			- auto pipeline, replaces streams and tasks
			- no schema evolution
		- https://docs.snowflake.com/en/user-guide/dynamic-tables-comparison
  		- https://coalesce.io/product-technology/slowly-changing-dimensions-with-dynamic-tables-and-coalesce/
	- https://coalesce.io/ dbt for Snowflake
 	- Snowflake can read Iceberg in external storage space
  		- https://youtube.com/watch?v=Ix2BZV1AjxA&si=th1tfQ9KDZWFsDaG
    		- Need separate AWS Glue Catalog in conjunction with Snowflake Catalog
- performance
	- warehouse structure
		- 1 extra small snowflake warehouse for Airflow jobs
			- fewest number of queries
			- query planner to see if long running queries are more efficient
				- break down queries, add intermediate tables
			- periodic COPY INTO cheaper than Snowpipe
		- 1 small / medium for analysts, data scientists
		- 1 small / medium for Sigma Computing
	- warehouse auto-scaling
	- multicluster warehouses
	- caching
	- query acceleration service
		- https://docs.snowflake.com/en/user-guide/query-acceleration-service
	- search optimization service
		- https://docs.snowflake.com/en/user-guide/search-optimization-service
- optimization
	- https://docs.snowflake.com/en/user-guide/tables-clustering-micropartitions
		- tables are closed source column store format, micro-partitioned
	- set table clustering keys (expensive compute to recluster)
		- https://docs.snowflake.com/en/user-guide/tables-clustering-keys
		- https://docs.snowflake.com/en/user-guide/tables-auto-reclustering
	- query profiling
		- https://docs.snowflake.com/en/user-guide/ui-query-profile
		- https://docs.snowflake.com/en/user-guide/performance-query-exploring
		- https://docs.snowflake.com/en/user-guide/performance-query-warehouse
	- https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics
		- split tables, use materialized views
		- optimize queries
			- OBT, but only select needed columns in queries
				- use LIMIT in queries
		- https://articles.analytics.today/boost-your-snowflake-query-performance-with-these-10-tips
		- https://articles.analytics.today/snowflake-cluster-keys-and-micro-partition-elimination-best-practices
		- https://articles.analytics.today/best-practices-for-reducing-snowflake-costs-top-10-strategies 
	- https://medium.com/@gupta.sahil.201191/snowflake-performance-optimization-techniques-9d135e07ef37
 	- dbt runs use up a lot of snowflake compute; consider SQLmesh instead
- RBAC
	- https://hevodata.com/learn/snowflake-roles/#3
		- orgadmin, accountadmin, securityadmin, sysadmin, etc.
	- Row Access Policies https://docs.snowflake.com/en/user-guide/security-row-intro 
	- Dynamic Data Masking down to column level https://docs.snowflake.com/en/user-guide/security-column-ddm-intro
 	- ***Permifrost*** https://medium.com/yousign-engineering-product/snowflake-rbac-implementation-with-permifrost-3d30652825ad
- Warehouse load monitoring, cost controls
	- https://docs.snowflake.com/en/user-guide/warehouses-load-monitoring
	- https://docs.snowflake.com/en/guides-overview-cost 
		- https://docs.snowflake.com/en/user-guide/cost-controlling 
	- Sigma has Snowflake Cost Monitoring Dashboard
		- https://www.sigmacomputing.com/interactive-demos/snowflake-cost-monitoring-template
	- https://sonra.io/snowflake/7-guardrails-against-common-mistakes-that-inflate-snowflake-credit-usage/
   	- Understand, Control, And Optimize Spend In Snowflake More Effectively
		- https://youtube.com/watch?v=Dwf11NxNqbw&si=9QTlHnx6ZEkAE-Wr
   	- Reduce Costs With Snowpipe Streaming And Dynamic Tables
		- https://youtube.com/watch?v=y67bH9ss07Y&si=RYzbsnPGqtWt2mAU
   	- Snowflake AI cost usage
   		- https://www.linkedin.com/posts/ian-whitestone_i-was-just-asking-our-snowflake-sales-engineer-activity-7220172262249746435-_hDq/
	- SurveyMonkey Increases Snowflake Workloads By 475% With Only A 27% Increase In Credit Use https://www.youtube.com/watch?v=4aCj0wk33kg
 ![Screenshot_20240729-192527_YouTube](https://github.com/user-attachments/assets/46382304-2ee7-49be-af3c-c534e3bd66a0)

	- ***Sundeck*** Snowflake warehouse usage cost optimization https://www.youtube.com/watch?v=jlCEeHHE_G8
- Data Lineage
	- https://www.phdata.io/blog/ultimate-guide-to-data-lineage-directly-in-snowflake/
 	- https://www.metaplane.dev/blog/the-definitive-guide-to-snowflake-data-lineage
  	- https://community.snowflake.com/s/question/0D53r0000BZbxJgCQJ/how-do-you-address-data-lineage
  		- coalesce, dbt, atlan, databand.ai, etc.
- Dynamic Data pipelines with SQL Macros (like dbt macros)
	- https://youtu.be/4O2_I25izIs?si=Mt_dBHBr6kM9puL2
![dynamicpipeline](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ce7db7eb-d24e-47a1-aaef-daf2c5f881e7)
![sqlmacro](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/57df1e49-9081-4cc6-a16f-3f9d53863d55)
![dynamicsql](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d629c549-b7a9-46c5-8906-68027caf125c)
- Level Up Your Spark Pipelines With Hex And Snowpark
	- https://youtube.com/watch?v=8IGP72KxTBw&si=Sw0hl_YUFY9hawra
 	- pyspark to snowpark
		- https://youtube.com/watch?v=M7uAWoPKMsg&si=-wqneWvcng5MY4Cn
		- snowpark not as advanced as spark (which is open source and Databricks bread and butter) https://www.youtube.com/watch?v=5dwYg2kuZ0A
	- https://www.youtube.com/watch?v=WinsWvLyEO0
![Screenshot_20240701-104713_YouTube](https://github.com/user-attachments/assets/32c2cd4a-426d-416a-b596-21387d69e9cf)
![Screenshot_20240701-104730_YouTube](https://github.com/user-attachments/assets/eb370645-5f14-4c4e-bdc8-69ff62a2a9d2)

- Building a Comprehensive Data Science Platform on Snowflake at Regions Bank
	- https://youtube.com/watch?v=z2zdIzfuNQo&si=Bnq4gAlJw-YqgRmb
- Fast, Easy, And Secure AI/ML Development And Deployment In Snowflake
	- https://youtube.com/watch?v=3WqDHoBGzPM&si=JyrCl3AQ7uIoSHs2
 ![snowflake ml](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d30f2d29-7b8d-4687-add5-af210c930e10)
- Unstructured data in Snowflake
	- https://youtube.com/watch?v=9YQTqQ2Ow48&si=erFkfj3O8g5oPoBK
![snowflake unstructured](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a1246109-a5bd-4635-93ac-1393e3d5e4d9)
- Snowflake + dbt
	- https://youtu.be/84RA7TuhCpg?si=_QxarT8WvkgMMsI4
- Snowflake & dbtvault
	- https://youtube.com/watch?v=u3LNHgUqFg4&si=jqXzh7mWm9Ez-aKz
- Snowflake + tinybird real time API speed layer
	- https://youtube.com/live/IOuXREaJj5Q?si=cwJJ3RqIbxqUHBDK
 	- tinybird kafka ingest  https://www.youtube.com/watch?v=ia_BN9AU-do
- data.world Snowflake native Data Catalog https://youtu.be/LcOel1im0tI?si=4KFtHDJBVh8KY4bz
- Snowflake 2024
	- [Snowflake 2024.pdf](https://github.com/user-attachments/files/15842303/Snowflake.2024.pdf)
- Snowflake Connector for Kafka
	- https://www.youtube.com/watch?v=ufUj5yP_tEQ

## Snowflake Hybrid Tables
- https://medium.com/snowflake/introducing-unistore-snowflakes-new-workload-for-transactional-and-analytical-data-daea01e49c61
- https://medium.com/snowflake/snowflake-hybrid-tables-all-you-need-to-know-58fd73426698
	- As of the Public Preview, you can expect an average of around ***20ms*** for both saves and reads from a HYBRID Table, resulting in a double-digit millisecond latency.
- like having postgres within Snowflake for low latency OLTP applications https://www.youtube.com/watch?v=GH7ZdiR9QG0
<img width="1920" alt="Screenshot 2024-09-30 at 12 12 28 PM (3)" src="https://github.com/user-attachments/assets/3c6f055b-a672-4117-8e8d-b972e9bac176">
<img width="1920" alt="Screenshot 2024-09-30 at 12 13 45 PM (3)" src="https://github.com/user-attachments/assets/932c6a99-0d5b-4774-9e5a-2440f57c1ae4">
<img width="1920" alt="Screenshot 2024-09-30 at 12 15 48 PM (3)" src="https://github.com/user-attachments/assets/3f55d9a8-f27f-4938-8b35-510f395fb2a5">
<img width="1920" alt="Screenshot 2024-09-30 at 12 17 33 PM (3)" src="https://github.com/user-attachments/assets/530638b0-9bdb-4c91-bb53-0dd8710cdce6">
<img width="1920" alt="Screenshot 2024-09-30 at 12 17 39 PM (3)" src="https://github.com/user-attachments/assets/52bd7c51-afd8-4b21-bd55-fa9818fae5ea">
<img width="1920" alt="Screenshot 2024-09-30 at 12 18 10 PM (3)" src="https://github.com/user-attachments/assets/fbc3c49d-0993-4235-8a2b-e39038153f56">

- Snowflake Hybrid Tables under the hood https://www.youtube.com/watch?v=tQsf-Nnx-RM
![Screenshot_20240701-112619_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/07aa10fd-3c98-4464-862c-cad776762144)
![Screenshot_20240701-112645_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/551e0dbe-6373-497a-bc60-a70a6e38000d)
![Screenshot_20240701-112711_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/38c80ef1-88f5-49be-8d50-481ac82e6f23)
![Screenshot_20240701-112737_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/25b0b86f-3492-423a-9407-dc8b5d52da55)
![Screenshot_20240701-112816_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3dcefe0d-5a2f-49c2-b0cb-3f0a53c8e989)
![Screenshot_20240701-112823_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5e091661-67ed-4b3f-b53f-5f2897126675)
![Screenshot_20240701-112857_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/54872cc5-f36a-45d1-885c-98bd4370917e)
![Screenshot_20240701-112909_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0f4c1cdd-34eb-4f1c-a823-ad7122f1f08b)
![Screenshot_20240701-112917_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/945ccc03-dc9c-4054-8bbb-a7a45a94cd5f)
- Hybrid Tables in production https://www.youtube.com/watch?v=uoHOxIPHvmg
![Screenshot_20240701-110509_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/51b7648a-0a08-451b-bea9-335b2909a8a8)
![Screenshot_20240701-110516_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7979d7fe-dbf9-4cff-9b2d-8708ea3390e3)
![Screenshot_20240701-111845_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c8410026-e9cb-44b6-b5a0-da2dd4287987)
![Screenshot_20240701-111849_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7e05458a-91cc-4a0b-992f-99fc6e25152d)
![Screenshot_20240701-111900_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cc29aebf-be68-4d5a-8f9c-a7625a0150ec)
![Screenshot_20240701-111915_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4ca6b337-d3b1-4274-bd90-6f7542ef2a56)
![Screenshot_20240701-111932_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/045e5823-86f0-4f58-b21d-f990aa36daae)
![Screenshot_20240701-111945_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e26beb92-b22f-4e1d-b70a-766c85fb16d4)
![Screenshot_20240701-112007_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0c4fe01d-bb5a-4666-a74c-dc5c596c6a39)
![Screenshot_20240701-112011_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1ed51e02-228d-4953-ad63-4094bfb1b276)
![Screenshot_20240701-112018_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1c3c7b0c-61cb-4bcc-b557-0328f4ae0ab1)
![Screenshot_20240701-112030_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8578742f-ffc2-4987-a83c-39b6773e32fe)
![Screenshot_20240701-112038_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f597c1e8-f717-4f5a-bdec-d32fee1c2e59)
![Screenshot_20240701-112052_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/41a65f94-6e9a-4cd8-a617-a71882edb301)
![Screenshot_20240701-112106_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e485d34b-40ca-4bc3-a476-ac4fd04f06a3)
![Screenshot_20240701-112124_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/440912d1-76a4-4340-b243-841920078809)
![Screenshot_20240701-112129_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6942fb59-8172-48dc-93e0-24863e6819da)
![Screenshot_20240701-112155_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e1b5c315-86b9-40ad-8fc3-8e129c80a461)

## Snowflake Notebooks
- https://www.youtube.com/watch?v=1zdciOSf8mA
	- Deploy snowflake notebook using snowflake task
	- GitHub actions CI CD
![Screenshot_20240701-113254_YouTube](https://github.com/user-attachments/assets/93c7ebcb-5fbb-4818-a5c5-5a2a6a5f0648)

## MLOps in Snowflake
- https://www.snowflake.com/blog/ml-enhances-mlops-streaming-feature-model-management/
	- ****Snowflake ML has a model registry and feature store****
- Transforming Snowflake into an MLOps ‘Feature Factory’ using Iguazio https://www.youtube.com/watch?v=8gUOvGE0xoU
- https://www.youtube.com/watch?v=hsnA8CiZNyY 
![Screenshot_20240701-172316_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/55a635c1-68d7-466c-a265-df9007254b3a)
![Screenshot_20240701-172327_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3825ecae-5a5c-4da3-8ed7-59ef6e0f5810)
![Screenshot_20240701-172335_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/59e3b9e6-be76-41bb-ae55-a3f165dca2a2)
![Screenshot_20240701-172343_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/416b1e21-50f9-4289-8b0e-f507c623dab5)
![Screenshot_20240701-172404_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/07f099dd-e8b8-4923-9c1e-91512c6535ac)
![Screenshot_20240701-172425_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a5212f48-3c59-426b-a246-38b160a8b9e8)
![Screenshot_20240701-172427_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/97cce32a-2d7b-4f6c-b6af-a15621be1343)
![Screenshot_20240701-172504_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d1bd14a9-8b95-4ee6-9c6d-2acf2788dd86)
![Screenshot_20240701-172515_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6bbe1c22-9241-48ec-836e-883fee7bd581)
![Screenshot_20240701-172520_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cfafcaf1-b8c3-47bc-a548-0be3809dc433)
![Screenshot_20240701-172530_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9c0d8d3e-e1ad-4f7a-9add-bb5bfb712519)
![Screenshot_20240701-172535_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c85e4280-e128-4253-8d85-5c64aa0b456b)
![Screenshot_20240701-172544_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e8461cd-308e-40c3-8cbd-3535bc06cca4)
![Screenshot_20240701-172606_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/08d1f54f-5da7-468a-bb32-fb6ff1cc80ec)
![Screenshot_20240701-172647_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e1d60062-becd-431d-adca-f45299d96d51)
![Screenshot_20240701-172655_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b60b7843-6c27-4069-bd2d-9c506275f4dd)
![Screenshot_20240701-172705_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a1e5739b-43b6-43a0-8928-6e0e6f3ae64d)
![Screenshot_20240701-172717_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/91b4ec12-f95a-4d28-92a7-a6d3533c543e)

## LLMs in Snowflake
- Snowflake Arctic LLM Foundational Model https://www.youtube.com/watch?v=kelxJkXE3bo
![Screenshot_20240701-171922_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/80424f75-600c-4d16-8c5e-50cb6eda2d35)
![Screenshot_20240701-171929_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c45a1076-6d35-4218-b634-572de778f114)
![Screenshot_20240701-171936_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b2a79752-7425-44f4-aab6-69e1dc155fa2)
![Screenshot_20240701-171945_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/37dd501d-7be4-42f3-8fe2-aba7fb43b8c3)
![Screenshot_20240701-171949_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c44737bc-95ee-43f4-a55b-c40ef445553f)
![Screenshot_20240701-172023_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2889f87b-2faa-445b-8cfb-4699d77df287)
![Screenshot_20240701-172026_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/77b22e52-bd4c-483d-b192-03e2d8df5bb3)
![Screenshot_20240701-172033_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d07b6c30-18bb-48dd-a8b0-abd1834917ff)
- RAG model in Snowflake https://www.youtube.com/watch?v=EClEf0S8zmk
	- ****Skyflow manages PII in Snowflake****
![Screenshot_20240701-171316_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f8325140-c1da-4cbb-92ad-92c3a2dab28f)
![Screenshot_20240701-171342_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5dfa7ca5-5519-4961-aec5-7a50f774345f)
![Screenshot_20240701-171347_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4dc5d36f-6a8b-4ecc-8e3e-313fb9e8b2ec)
![Screenshot_20240701-171350_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e1c99616-61dc-4553-870f-442bf0b2cf8b)
![Screenshot_20240701-171403_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/60c49163-d91f-4ebf-aa80-f5d097667bbf)
![Screenshot_20240701-171406_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a742a4b2-d0f4-46a9-8f75-140c3c2fbf44)
![Screenshot_20240701-171410_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c9a7bf5b-d556-45e1-a3b2-d9c7d0ade7e2)
![Screenshot_20240701-171418_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0b37e551-951f-4e9d-8f7d-eb951c41631d)
![Screenshot_20240701-171434_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc98c9bb-2262-472e-88c5-ab27c3912173)

## Snowflake Native Apps
- Aimpoint Digital's Anxiety-Free Guide To Deploying Snowflake Native Apps https://www.youtube.com/watch?v=O2RJrdzYB70
![Screenshot_20240701-131526_YouTube](https://github.com/user-attachments/assets/bc3438d9-5023-4752-88d2-9ebb02072bdc)
![Screenshot_20240701-131640_YouTube](https://github.com/user-attachments/assets/b54b2c0c-d36e-4c18-a20a-19a63615ecdd)
![Screenshot_20240701-131654_YouTube](https://github.com/user-attachments/assets/84b16ede-c7e3-4162-811f-a1b72b67ce5c)
![Screenshot_20240701-131719_YouTube](https://github.com/user-attachments/assets/6f9b31d1-0d7e-4045-b150-1e4ce7df9e70)
![Screenshot_20240701-131756_YouTube](https://github.com/user-attachments/assets/d3874e1f-a03d-4dd0-9773-da466d44777a)
![Screenshot_20240701-131821_YouTube](https://github.com/user-attachments/assets/77e1a137-6b45-4510-abcc-369edc3d8b26)
![Screenshot_20240701-131929_YouTube](https://github.com/user-attachments/assets/349c288d-a917-4d13-90fe-a9bd91ceea3e)
