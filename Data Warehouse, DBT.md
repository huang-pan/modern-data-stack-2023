# Udemy Data Warehouse / dbt

## Logical vs Physical Architecture
- https://www.youtube.com/watch?v=0QOi3DiFlSg
![Screenshot_20240630-173000_YouTube](https://github.com/user-attachments/assets/2e67921d-b82e-4b70-93eb-c77de5222aa1)
![Screenshot_20240630-173114_YouTube](https://github.com/user-attachments/assets/ad0f14dd-3331-40d9-9476-a29816d10b66)
![Screenshot_20240630-173024_YouTube](https://github.com/user-attachments/assets/b804e1aa-89f8-4198-a36a-b7a4bcfeda82)
![Screenshot_20240630-173226_YouTube](https://github.com/user-attachments/assets/0c61067a-cd97-4571-b2ae-6f367b35fd1f)
![Screenshot_20240630-173258_YouTube](https://github.com/user-attachments/assets/8cd7991d-8b02-46f8-892d-e5b71eae7e11)

## [https://www.udemy.com/course/data\-warehouse\-fundamentals\-for\-beginners/](https://www.udemy.com/course/data-warehouse-fundamentals-for-beginners/)

- Course completion certificate: [https://www.udemy.com/certificate/UC\-9875515d\-9606\-4bfc\-8ddc\-e408d9d65aae/](https://www.udemy.com/certificate/UC-9875515d-9606-4bfc-8ddc-e408d9d65aae/) 
- Summary:
    - This is a basic refresher course on data warehouses for me.

![medallion](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1f7a9164-bd06-4401-bbbf-dec23133abcd)

- https://lakshmanok.medium.com/what-goes-into-bronze-silver-and-gold-layers-of-a-medallion-data-architecture-4b6fdfb405fc

- warehouse / data lake
    - **Possible ways to structure a data warehouse like Snowflake**
        - Ultimately depends on company / project / use case
            - separate DBs for source, consumption, dev work?
            - think about boundaries, RBAC
        - Example:
            - one database per source, e.g. ATTOM\_DB, ZILLOW\_DB
                - RAW schema: data from source, aka dbt **src**
                    - can save historical data in dated tables
                        - time travel capabilities limited to finite time in Snowflake
                - BASE / STAGE schema: cleaned RAW data, aka dbt **stg**
                    - use views based off of RAW tables
            - ANALYST\_DEV\_DB, ANALYST\_PROD\_DB \(also TEST\_DB? only PROD\_DB gets exposed to BI tools used by end users.  can also name DB by analyst project\)
                - Dimensional Modeling
                    - INT schema: aka dbt **int**
                    - CORE schema:
                        - for dbt **fct**, **dim**
                            - by default, dbt seems to use dimensional modeling with fact / dimension tables, star and snowflake schemas
                        - for dbt **mart** 
                            - can also name schema by specific MART, e.g. marketing, biz dev, etc.
                            - can be wide tables for OBT architecture
                - One Big Table
                    - INT schema
                - Data Vault 2.0 \(Don't start with this on a greenfield project \- too much upfront complexity, only for enterprise data warehouses with 100s of sources of data \- data swamp\)
                    - RAW\_VAULT schema
                    - BUSINESS\_VAULT schema: \(optional\)
                - WRK schema: for dev work
            - DATASCIENCE\_DEV\_DB, DATASCIENCE\_PROD\_DB \(can also name them by Data Science or Machine Learning project\)
            - ADHOC\_DB: for one off work
        - [https://airbyte.com/blog/snowflake\-data\-warehouse\-architecture](https://airbyte.com/blog/snowflake-data-warehouse-architecture)
        - [https://www.analytics.today/blog/snowflake\-accounts\-best\-practice](https://www.analytics.today/blog/snowflake-accounts-best-practice)
        - [https://www.reddit.com/r/snowflake/comments/umvn1f/how\_to\_design\_snowflake\_databases\_and\_schemas/](https://www.reddit.com/r/snowflake/comments/umvn1f/how_to_design_snowflake_databases_and_schemas/)
        - https://www.reddit.com/r/Database/comments/dovxgo/determining_schema_for_real_estate_data_warehouse/
    - Data Warehouse data modeling
    	- Entity & attributes https://www.youtube.com/watch?v=ZdaxYazyw5Y
		- 1st, 2nd, 3rd normal form, BCNF, 4NF, 5NF
			- https://youtube.com/watch?v=J-drts33N8g&feature=share 
			- https://www.youtube.com/watch?v=xPCimZd4Dog 
        - 3NF Third Normal Form vs Dimensional Modeling vs Data Vault
            - [https://youtu.be/l5UcUEt1IzM](https://youtu.be/l5UcUEt1IzM)
            - **3NF Third Normal Form: OLTP, optimized for fast writes**
            - Dim modeling: Kimball, fact, dim, mart, **optimized for fast reads**
            - Data Vault 2.0: hub, link, satellite, optimized for fast reads and constant addition of new data sources
                - combination of 3NF \+ DIM modeling
                - good for organizing data when you have a lot \(100s\) of different sources: Enterprise Data Warehouse only
        - **Data Modeling in the Modern Data Stack**
            - **[https://youtu.be/IdCmMkQLvGA](https://youtu.be/IdCmMkQLvGA)**
                - conceptional \(biz needs\) \-\-\> logical \(detailed biz solution\) \-\-\> physical layers \(detailed tech solution\)
![Screenshot_20240624-155827_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/951332a1-2e25-427c-afc8-ae02796d91ce)
            - Normalized modeling: Inmon copies directly from databases to data warehouse, also has data marts
            - Denormalized modeling: Kimball, dimensional modeling \(fact, dim, mart\), star, snowflake schemas, SCD
                - single source of truth for data source that maintains consistency, conformity, and understandability
                - dbt naturally supports dim modeling
                - good balance between normalized modeling and data vault 2.0
                - https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/ 
            - Data Vault 2.0: Linstedt, hub, link, satellite, optimized for fast reads and constant addition of new data sources
                - mainly for Enterprise Data Warehouses with a lot of different data sources, optimized for data ingestion, not reporting
                    - data supply driven
                        - complex to set up; time to get BI results slow in beginning
                        - BUT: single source of truth for data source that maintains consistency, conformity, and understandability
                - [https://www.phdata.io/blog/building\-modern\-data\-platform\-with\-data\-vault/](https://www.phdata.io/blog/building-modern-data-platform-with-data-vault/)
                    - raw vault: hub, link, satellite
                    - business vault: Business Vault is an optional tier in the Data Vault where the business can define common business entities, calculations, and logic.
                    - marts
                - dbtvault / AutomateDV: Data Vault 2.0 using dbt \+ Snowflake 
                    - [https://youtu.be/bi3x9f5lxp0](https://youtu.be/bi3x9f5lxp0)
                    - [https://youtu.be/FrdEROEUvVI](https://youtu.be/FrdEROEUvVI)
                    - https://www.youtube.com/watch?v=fDCxGM6Sh8M
                    - https://www.youtube.com/watch?v=qqnnsy393Ro
            - One Big Table: for modern column store data warehouses
                - reporting driven
                    - data optimized for modern column store data warehouse \(storage cheap\)
                        - joins \(compute\) from star / snowflake schemas expensive for modern data warehouses
                            - queries from OBT faster in column store data warehouses
                        - creating star / snowflake schema add another layer of complexity to manage; have to make sure the complexity is justified \-\> implement dim modeling when data gets bigger
                    - fast BI results, data may get complex to manage later
                - INT schema
                - wide MART schema
                - [https://youtu.be/3OcS2TMXELU](https://youtu.be/3OcS2TMXELU)
                    - OBT approach ok for modern data warehouses
                - [https://www.youtube.com/watch?v=\-yQa\_DxEqaQ](https://www.youtube.com/watch?v=-yQa_DxEqaQ)
                    - adds to discussion above, dimensional modeling ok before OBT: hybrid approach
                    - data warehouse normalized \(Data Vault 2.0, dim modeling\) \-\> denormalized \(OBT\)
            - Hybrid Approach
                - Star schema \+ wide Marts
                - INT schema
                    - start with dimensional model
                    - consistency, conformity, and understandability point of dim model
                        - SCD type 2, data lineage
                - wide MART schema
                    - create wide fact \+ dim tables
            - Bus Architecture
                - create data warehouse from multiple data marts, use conformed dimensions
                - https://youtube.com/watch?v=z7uNwS-OWHA&feature=share
                - https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/kimball-data-warehouse-bus-architecture/
            - Conformed dimensions https://www.youtube.com/watch?v=mK1MKKRmAoA
![Screenshot_20240624-155548_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1ba7c9f7-9f94-4623-950a-f63e2066b643)
![Screenshot_20240624-155435_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/34781ab6-f80e-43c9-9dad-6b8e94d4f387)
            - Advice on data modeling
                - https://youtube.com/watch?v=F-vkxuq5nv0&feature=share
    - Data Lakehouse **Medallion** architecture:
        - [https://www.databricks.com/glossary/medallion\-architecture](https://www.databricks.com/glossary/medallion-architecture)
        - bronze \-\> silver \-\> gold
            - structure good for data scientists
            - can possible have bronze = raw, silver = cleaned, gold = core \(fact / dimension / mart\)
                - [https://youtu.be/aA5upa1iqJ0](https://youtu.be/aA5upa1iqJ0)
            - can also have DEV schema, just as a dev playground for data engineers / scientists
                - can create more schemas as needed
	- https://www.youtube.com/watch?v=8Qlfs2IohHM
 		- Raw, Staging, Bronze, Silver, Gold, harmonized, archived
        - medillion architecture generated with chatgpt
            - [https://betterprogramming.pub/i\-asked\-chatgpt\-to\-build\-a\-data\-pipeline\-and\-then\-i\-ran\-it\-4537670a60ca](https://betterprogramming.pub/i-asked-chatgpt-to-build-a-data-pipeline-and-then-i-ran-it-4537670a60ca) 
        - [https://piethein.medium.com/using\-dbt\-for\-building\-a\-medallion\-lakehouse\-architecture\-azure\-databricks\-delta\-dbt\-31a31fc9bd0](https://piethein.medium.com/using-dbt-for-building-a-medallion-lakehouse-architecture-azure-databricks-delta-dbt-31a31fc9bd0)
            - Data Lakehouse Medallion architecture \+ dbt
![medallion-dbt](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cd440c75-d6a1-4607-86a5-5b54c997cbff)
![datalakehouse_mesh](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/00ed80d7-c8cc-4687-8460-8cb2cbf70119)
        - Unity Catalog
  ![Screenshot 2023-08-17 at 8 24 24 AM (2)](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7f081874-35e7-41dc-8c20-f31549d2ea99)

    - **Core** architecture
        - [https://airbyte.com/blog/data\-modeling\-unsung\-hero\-data\-engineering\-architecture\-pattern\-tools](https://airbyte.com/blog/data-modeling-unsung-hero-data-engineering-architecture-pattern-tools)
            - **raw \-\> staging \-\> cleansing \-\> core \-\> marts**
            - Popular data modeling tools include [Sqldbm](https://sqldbm.com/?_gl=1*1oc44lc*_ga*MTUzNzQ2NzYxNi4xNjg2NDMwODU5*_ga_HDBMVFQGBH*MTY4Nzc1MDQyNC4yLjAuMTY4Nzc1MDQyNC4wLjAuMA..), [DBDiagrams](https://dbdiagram.io/), [Enterprise Architect](https://sparxsystems.com/), and [SAP PowerDesigner](https://www.sap.com/products/technology-platform/powerdesigner-data-modeling-tools.html). These tools are widely used in the industry and offer powerful features such as data modeling, profiling, and visualization.
            - Open\-source data modeling tools such as [MySQL Workbench](https://www.mysql.com/products/workbench/?_gl=1*hdnksn*_ga*MTUzNzQ2NzYxNi4xNjg2NDMwODU5*_ga_HDBMVFQGBH*MTY4Nzc1MDQyNC4yLjAuMTY4Nzc1MDQyNC4wLjAuMA..) and [OpenModelSphere](http://www.modelsphere.com/) are free and offer essential features for creating data models. They are helpful for small projects and provide an opportunity for data engineers to learn data modeling skills.
            - Other tools are [Ellie.ai](https://www.ellie.ai/), whose key features are Data Product Design, Data Modeling, Business Glossary, Collaboration, Reusability, and Open API.
            - dbt can be seen as a transformation modeling tool. [Dagster](https://glossary.airbyte.com/term/dagster/) can be used as a [DAG](https://glossary.airbyte.com/term/dag-directed-acyclic-graph/) modeling tool. And so forth. But you can also use [ExaliDraw](https://excalidraw.com/?_gl=1*1vut0at*_ga*MTUzNzQ2NzYxNi4xNjg2NDMwODU5*_ga_HDBMVFQGBH*MTY4Nzc1MDQyNC4yLjAuMTY4Nzc1MDQyNC4wLjAuMA..) for Markdown\-based drawing or [draw.io](https://draw.io/?_gl=1*1vut0at*_ga*MTUzNzQ2NzYxNi4xNjg2NDMwODU5*_ga_HDBMVFQGBH*MTY4Nzc1MDQyNC4yLjAuMTY4Nzc1MDQyNC4wLjAuMA..) \(lots of [templates](https://www.drawio.com/example-diagrams) for AWS, Azure, etc.\) to draw architectures.
            - [https://airbyte.com/blog/data\-modeling\-unsung\-hero\-data\-engineering\-introduction](https://airbyte.com/blog/data-modeling-unsung-hero-data-engineering-introduction)
                - normalized vs unormalized
                - Slowly Changing Dimensions https://phanikumaryadavilli.medium.com/managing-dimensional-data-changes-a-refresher-to-slowly-changing-dimensions-scds-and-their-types-d7f181b7492c
            - [https://airbyte.com/blog/data\-modeling\-unsung\-hero\-data\-engineering\-approaches\-and\-techniques](https://airbyte.com/blog/data-modeling-unsung-hero-data-engineering-approaches-and-techniques)
                - conceptual \-\> logical \-\> physical 
        - **Entity Relationship Modeling \(ERM\): OLTP**
        - **Dimensional Modeling: OLAP**
            - star vs snowflake schemas
                - snowflake: more normalization of dimension tables
                - [https://www.guru99.com/star\-snowflake\-data\-warehousing.html](https://www.guru99.com/star-snowflake-data-warehousing.html)
	- https://www.interviewquery.com/p/data-modeling-interview-questions 
    - dbt: Naming Conventions
        - **https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview**
        - **[https://docs.getdbt.com/blog/stakeholder\-friendly\-model\-names](https://docs.getdbt.com/blog/stakeholder-friendly-model-names)** 
        - [https://towardsdatascience.com/the\-most\-efficient\-way\-to\-organize\-dbt\-models\-244e23c17072](https://towardsdatascience.com/the-most-efficient-way-to-organize-dbt-models-244e23c17072) 
        - In working on this project, we established some conventions for naming our models.
        - **Sources** \(`src`\) refer to the raw table data that have been built in the warehouse through a loading process. \(We will cover configuring Sources in the Sources module\)
        - **Staging** \(`stg`\) refers to models that are built directly on top of sources. These have a one\-to\-one relationship with sources tables. These are used for very light transformations that shape the data into what you want it to be. These models are used to clean and standardize the data before transforming data downstream. Note: These are typically materialized as views.
            - can have persistent or non persistent data
        - **Intermediate** \(`int`\) refers to any models that exist between final fact and dimension tables. These should be built on staging models rather than directly on sources to leverage the data cleaning that was done in staging.
        - **Fact** \(`fct`\) refers to any data that represents something that occurred or is occurring. Examples include sessions, transactions, orders, stories, votes. These are typically skinny, long tables.
        - **Dimension** \(`dim`\) refers to data that represents a person, place or thing. Examples include customers, products, candidates, buildings, employees.
![granularity](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c0f24dae-5893-48bf-956d-874512d3ec8c)
![conformed](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4f6e2257-a44e-4f9a-be7c-58b17327e60e)

- 4 ETL patterns
    - append
    - in\-place update
    - complete replacement \(obsolete\)
    - rolling append \(delete older data\) \(obsolete\)
- stg clean data
    - raw \-\> stg; bronze \-\> silver; src \-\> stg
    - data value unification
    - data type unification
    - deduplication
    - drop columns
    - value based row filtering
    - error correction
- fact
    - additive fact \(e.g. salary\): store in fact table
    - non\-additive fact \(e.g. GPA\): store underlying components in fact tables
    - semi\-additive fact: used in periodic snapshot fact table
- star \(denormalized dimension tables\) vs snowflake \(normalized dimension tables\) schema
    - **only store lowest level PF\-FK relationship in fact table in snowflake schema**
    - ETL simpler for star schema
- keys
    - natural key: might be cryptic or understandable, travels from source systems with the rest of the data
        - keep natural keys in dimension tables in data warehouse, discard them in fact tables
    - surrogate key: no business meaning, generated by database
        - **use surrogate keys in data warehouse**
- dimensional tables
    - dimension = dimensional table
    - hierarchical \(college \-\> department \-\> faculty\) vs flat \(students\)
    - snowflake schema Primary Key \- Foreign Key rules
        - 1 table for each level of hierarchy
        - every non\-terminal dimension has: primary / surrogate key, the next\-highest level's PK/SK as a Foreign Key, can have multiple FKs
        - every terminal dimension has PK/SK, no FK
- fact tables
    - fact \!= fact table
    - **Primary Key of fact table is a combination of Foreign Keys to all dimensional tables**
    - **transaction: most common type of fact table**
        - store measurements from OLTP databases
        - add Surrogate Keys to Dimension Tables
        - can store facts that are available at same grain in same fact table, but facts have to occur simultaneously
        - PK of fact table: combination of all FKs of dimension tables
            - can store natural key in fact table
    - periodic snapshot
        - aggregated result of regular transactions
        - levels that are not related to regular transactions
    - accumulating snapshot
        - tracks elapsed time spent in each phase
            - can also track other related measures
        - **multiple relationships from fact table back to single dimension table**: e.g. date\_phase1\_key / date\_phase2\_key \-\> data\_dim
    - factless
        - record an event without a measurement
        - record existence of event / relationship or not
- slowly changing dimension \(obsolete with history tables?\)
    - techniques to manage history in data warehouse
    - type 1: no history retention
    - type 2: maintain unlimited history
        - create new dimension table row for each new version of history
            - create new Surrogate Key / Primary Key for new row in dim table
            - can create current\_flag column and / or effective\_date / expiration\_date columns to determine current \(not history\) row
        - most complex arch
    - type 3: maintain limited history
        - small number of dimension table columns for multiple versions of history
        - add new column rather than new row to reflect changes: old value vs new value column
        - best used for a dimension being reorganized, limited number of column categories \(\<= 4, \> 4 use type 2\)
    - less common:
        - type 0: always retain original value in the data warehouse
        - type 4: min\-dimension
        - type 5, 6, 7: hybrid
- Bridge Tables (or Link Tables)
	- “These are used in “many-to-many relationships” between dimensions. For instance, if you have a scenario where multiple products can be in different promotions at the same time, a bridge table would be used to manage this relationship. “ -Ralph Kimball
 	- Another common example used in most articles and in Kimballs’ books is healthcare and a patient’s diagnosis, which can have more than one diagnosis at a time. In turn, you’ll often see a bridge table used (See the model below).
  	- Many data modelers try to avoid implementing too many bridge table situations as they can add a lot of risk in terms of miscounting or joining across the tables.- ETL
    - use CDC to limit data ingest to warehouse
    - process dim tables before fact tables: create new dim table Surrogate Keys \-\> update fact table FKs
    - look for opportunities for parallel processing
- Case study dimensional modeling
	- https://youtube.com/watch?v=7HyGM3Iw0Kc&si=kX1FdNosFXzgXHba 
		- start with business problem --> find smallest grain --> create conceptual model --> create logical model
		- logical model: fact, dimension tables (who, what, when, how); each table: primary key, attributes
		- degenerate dimension ID: ID without any attributes (e.g. bar code), put in fact table, no dimension table
  	- ![fact_dim](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/73c1cf9f-73d9-48e8-b3ef-098f41555c46)
  	- Dim tables: Who What When How; Fact: measures
  		- https://www.interviewquery.com/questions/retailer-data-warehouse
- Fixing slow queries: If a query is running slowly or incurring high costs, I instinctively check for the following six factors. This approach typically resolves most issues related to query speed and cost.
	- 𝟭. 𝗨𝘀𝗲 𝗶𝗻𝗱𝗲𝘅𝗲𝘀 𝗮𝗻𝗱 𝗽𝗮𝗿𝘁𝗶𝘁𝗶𝗼𝗻𝘀
		- Partitioning divides the data into smaller parts, and indexing helps the database retrieve data more quickly. Before executing your query, check if there is a partition or index you can use; this will significantly enhance your query's performance.
	- 𝟮. 𝗔𝘃𝗼𝗶𝗱 𝘂𝘀𝗶𝗻𝗴 𝗳𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝘀 𝗼𝗻 𝗪𝗛𝗘𝗥𝗘 𝗰𝗹𝗮𝘂𝘀𝗲𝘀 𝗮𝗻𝗱 𝗝𝗢𝗜𝗡’𝘀 Functions can prevent index usage. Instead, consider using calculated/generated columns with indexes.
	- 𝟯. 𝗥𝗲𝘃𝗶𝗲𝘄 𝗲𝘅𝗲𝗰𝘂𝘁𝗶𝗼𝗻 𝗽𝗹𝗮𝗻
		- Review the execution plan to identify any performance bottlenecks. Determine which operation is incurring high costs and explore ways to reduce the query's overall cost. Sometimes even though there is an index is present and the query intended to use it, query engine still might not use it. Maybe your index has corrupted? You can repair your index. You can even force query engine to use the index if it is still not using it.
	- 𝟰. 𝗔𝘃𝗼𝗶𝗱 𝗰𝗼𝗺𝗽𝘂𝘁𝗮𝘁𝗶𝗼𝗻𝗮𝗹𝗹𝘆 𝗲𝘅𝗽𝗲𝗻𝘀𝗶𝘃𝗲 𝘀𝘁𝗮𝘁𝗲𝗺𝗲𝗻𝘁𝘀: 𝗨𝗡𝗜𝗢𝗡 𝗗𝗜𝗦𝗧𝗜𝗡𝗖𝗧, 𝗟𝗜𝗞𝗘 %%, 𝗖𝗧𝗘’𝘀, 𝗦𝘂𝗯𝗾𝘂𝗲𝗿𝗶𝗲𝘀
		- Some statements are costly. Try to write queries without costly statements, use them as a last resort.
		- UNION DISTINCT compares the results of two sets and removes duplicates. If you are certain that the two result sets do not have duplicate rows, you can use UNION ALL, which is less computationally expensive.
		- The same principle applies to the 'LIKE' operator. Not only does it prevent index usage, but when used with both beginning and end wildcards, it becomes more computationally expensive. Try to avoid wildcard matching whenever possible.
		- Common Table Expressions (CTEs) and subqueries cannot be indexed, so they can also be slow if they produce large results. Use them with caution.
	- 𝟱. 𝗨𝘀𝗲 𝗪𝗛𝗘𝗥𝗘, 𝗳𝗶𝗹𝘁𝗲𝗿 𝗱𝗮𝘁𝗮 𝗲𝗮𝗿𝗹𝘆
		- Optimize your queries by filtering your data early with the WHERE clause. This is one of the most fundamental yet occasionally overlooked query optimization techniques. If you don't require data from the previous year, make sure to filter it out.
	- 𝟲. 𝗔𝘃𝗼𝗶𝗱 𝗦𝗘𝗟𝗘𝗖𝗧 *
		- If you don’t need column do not select it. This rule holds significant importance, especially for columnar storage systems like BigQuery and Redshift, as they store and retrieve data based on columns rather than rows.

## [https://www.udemy.com/course/complete\-dbt\-data\-build\-tool\-bootcamp\-zero\-to\-hero\-learn\-dbt/](https://www.udemy.com/course/complete-dbt-data-build-tool-bootcamp-zero-to-hero-learn-dbt/)

- Course completion certificate: [https://www.udemy.com/certificate/UC\-de00a2d0\-a8a1\-4319\-8101\-bbea3cb3cc5b/](https://www.udemy.com/certificate/UC-de00a2d0-a8a1-4319-8101-bbea3cb3cc5b/) 
- Summary:
    - This is a refresher course on dbt for me. It covers all the basics with simple example, it's more like a tutorial introduction to dbt. While basic, I found this course to be a comprehensive re-introduction to dbt.
- Github repos for course:
    - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero)
    - [https://github.com/huang\-pan/complete\-dbt\-bootcamp\-zero\-to\-hero](https://github.com/huang-pan/complete-dbt-bootcamp-zero-to-hero)
    - https://tech.instacart.com/adopting-dbt-as-the-data-transformation-tool-at-instacart-36c74bc407df
    - https://github.com/Hiflylabs/awesome-dbt
- **preset**: managed superset tool
- dbt Cloud vs Vscode
    - **dbt Cloud nice, but you can do everything in VScode & CLI**
- create snowflake trial account
    - Airbnb database:
        - RAW schema
        - DEV schema: build dbt objects into
        - RAW \-\-\> DEV / SRC\_ tables \-\-\> DEV / FCT\_ / DIM\_ tables \-\-\> MART\_ tables
            - also dbt tests
- set up dbt
    - can also set everything up in **dbt cloud** \(but not covered in course\)
    - dbt init: set up initial connection to Snowflake
        - ~/.dbt/profiles.yml
        - /Users/huangpan/Documents/udemy/dbt/dbtlearn/dbt\_project.yml
    - dbt debug: test connection working
- models
    - SQL definitions that are materialized as tables, views, etc.
        - they live in SQL files in the models folder
            - by default, views are created
        - models can reference each other and use templates and macros
    - RAW schema: RAW layer
        - raw\_listings, raw\_hosts, raw\_reviews tables
    - DEV schema: STAGING layer \(basic checks\)
        - src\_listings, src\_hosts, src\_reviews views
    - DEV schema: CORE layer
        - dim\_listings\_cleansed \+ dim\_hosts\_cleansed \-\> dim\_listings\_with\_hosts \(final dimension table\)
        - fct\_reviews \(incremental table\)
        - **mart\_**fullmoon\_reviews: table used by BI tools
    - DEV schema:
        - seeds \(csv files\) uploaded here
        - snapshot tables created here
- materializations \(of models\)
    - dim / fct / mart / src
    - view
        - lightweight representation
        - don't reuse data too often, single use
    - table
        - read from model repeatedly
    - incremental \(table appends\)
        - use for fact tables, event data
    - ephemeral \(CTEs\)
        - only used as intermediate step between models
    - **dbt\_project.yml**
        - project defaults
    - **dbt run \-\-full\-refresh** command
        - rebuild all tables / views from scratch, for schema changes, etc.
    - **target folder**: actual SQL that is run by dbt, useful for debug
- seeds
    - local files that you upload to the data warehouse from dbt
    - **dbt seed** command
        - automatically load all csv files in seed folder \(specified in dbt\_project.yml\) to data warehouse
        - loads to DEV schema table
        - dbt automatically creates column types of table in data warehouse
- sources
    - **models/sources.yml** file
        - an abstraction layer on top of your input tables
        - one place to specify / hardcode all the source tables referred to in model files
    - **dbt source freshness** command
        - source freshness can be checked automatically
    - **dbt compile** command
        - check to see if all dbt files compile correctly without running them
- snapshots
    - how dbt handles **type\-2** slowly changing dimensions
        - **snapshots** folder
    - how dbt monitors changes
        - 1. timestamp strategy: unique key and updated\_at timestamp column
        - 2. any change in a set of columns \(or all columns\)
    - **dbt adds columns to snapshot table**
        - dbt\_updated\_at, dbt\_valid\_from, dbt\_valid\_to
        - snapshot table in DEV schema
    - **dbt snapshot** command to update snapshot table
- tests
    - singular
        - SQL queries stored in tests which are expected to return an empty result set
    - generic
        - unique
        - not\_null
        - accepted\_values
        - relationships
    - **models/schemas.yml** file
        - apply generic test to cleansed tables
    - **tests/\*.sql** files
        - singular tests, SQL query expected to return empty result set
    - **dbt test \-\-select dim\_listings\_w\_hosts**
        - run tests on specific model
    - dbt testing frameworks
    	- https://github.com/calogica/dbt-expectations
     		- has a lot more generic tests than dbt core https://datacoves.com/post/dbt-test-options
    	- https://github.com/EqualExperts/dbt-unit-testing
    - Datafold data-diff complete dataset comparison testing
    	- https://github.com/huang-pan/modern-data-stack-2023/blob/main/dbt/Download%20the%20definitive%20guide%20to%20dbt%20testing.pdf
	- https://www.youtube.com/watch?v=nHSEiwa9iIQ
		- data diff used for: data replication & migration, CI / CD
		- Allium.so uses datafold
		- ****Y42**** implicitly has data-diff in their git PR processes: https://www.linkedin.com/posts/hung-dang-y42_datafold-recently-announced-that-they-will-ugcPost-7199017036537069568-a6NC/
- Data Quality
	- https://blog.det.life/mastering-data-quality-10-essential-checks-with-real-world-examples-and-7-best-practices-fa303f2ae42b
    	- https://ssmertin.com/articles/strategies-for-data-quality-with-apache-spark/
    		- test for: completeness (check for missing data), consistency (data within range), uniqueness, timeliness, relevance, accuracy, validity
     	- https://seattledataguy.substack.com/p/how-and-why-we-need-to-implement
	- https://www.linkedin.com/posts/josephmachado1991_data-dataengineering-dataquality-activity-7254825978760175616-LklH/ 
- macros
    - dbt has many built in macros
    - **macros/\*.sql** files
        - jinja templates that can be referenced by models, tests, etc.
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/tests/no\_nulls\_in\_dim\_listings.sql](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/tests/no_nulls_in_dim_listings.sql) uses macro
        - dbt loops https://docs.getdbt.com/guides/advanced/using-jinja 
- [hub.getdbt.com](http://hub.getdbt.com)
    - dbt third party packages, specify them here:
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/packages.yml](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/packages.yml) 
    - **dbt deps** installs packages
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/fct/fct\_reviews.sql](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/fct/fct_reviews.sql) uses [https://github.com/dbt\-labs/dbt\-utils/tree/1.1.1/\#generate\_surrogate\_key\-source](https://github.com/dbt-labs/dbt-utils/tree/1.1.1/#generate_surrogate_key-source)
        - https://docs.getdbt.com/reference/commands/deps
        - https://docs.getdbt.com/docs/collaborate/govern/project-dependencies
- documentation
    - 2 ways to define documentation:
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/schema.yml](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/schema.yml) description: fields
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/overview.md](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/overview.md) markdown files, this is the documentation landing page
            - references this image: [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/assets/input\_schema.png](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/assets/input_schema.png) 
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/schema.yml\#L32](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/schema.yml#L32) references [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/docs.md](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/docs.md) 
    - **dbt docs generate** generates documentation into target/ folder
        - **dbt docs serve** creates lightweight localhost dbt documentation server
            - project details, model details, test details
            - dbt **data lineage** dependency graph automatically created
        - copy target/ files into web server for more permanent serving, or use dbt cloud
- analyses
    - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/analyses/full\_moon\_no\_sleep.sql](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/analyses/full_moon_no_sleep.sql) example of ad hoc queries
- hooks
    - SQL executed at predefined times, can be configured in:
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/dbt\_project.yml\#L38](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/dbt_project.yml#L38) project
        - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/tree/main/hooks](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/tree/main/hooks) subfolder, has many hook examples, e.g. [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/hooks/commit\-msg.sample](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/hooks/commit-msg.sample) 
        - model
    - hook types
        - on\_run\_start: executed at the start of dbt \(run / seed / snapshot\)
        - on\_run\_end: executed at the end of dbt \(run / seed / snapshot\)
        - pre\-hook: executed before a model / seed / snapshot is built
        - post\-hook:  executed after a model / seed / snapshot is built
- exposures
    - [preset.io](http://preset.io) \(managed superset\)
        - create BI dashboard connected to data in Snowflake
    - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/dashboards.yml](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/dashboards.yml) example exposure, information is integrated into dbt documentation server
- dbt\-expectations
    - [https://github.com/calogica/dbt\-expectations](https://github.com/calogica/dbt-expectations) 
    - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/schema.yml\#L58](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/schema.yml#L58) 
        - uses [https://github.com/calogica/dbt\-expectations\#expect\_table\_row\_count\_to\_equal\_other\_table](https://github.com/calogica/dbt-expectations#expect_table_row_count_to_equal_other_table) 
        - many other tests
    - [https://github.com/nordquant/complete\-dbt\-bootcamp\-zero\-to\-hero/blob/main/models/sources.yml\#L12](https://github.com/nordquant/complete-dbt-bootcamp-zero-to-hero/blob/main/models/sources.yml#L12) more dbt\-expectations tests
    - **dbt test** run tests

dbt + snowflake + blockchain: they use medallion arch (bronze silver gold)
- https://youtube.com/watch?v=HxJ6Gt_PK_E&feature=share 
- types of tests:
![dbt_snowflake](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/addf1a28-f42a-49e4-b7b9-685f384f48f7)

dbt best practices https://docs.getdbt.com/guides/best-practices/how-we-structure/1-guide-overview 
- directory / project scaffolding, style guide
- CI / CD: https://paulfry999.medium.com/v0-4-pre-chatgpt-how-to-create-ci-cd-pipelines-for-dbt-core-88e68ab506dd
	- use dbt cloud to enable CI / CD from git changes
- https://www.arecadata.com/the-definitive-guide-for-debugging-dbt/
- dbt clone
	- https://docs.getdbt.com/reference/commands/clone
 	- clone snowflake databases
- dbt threads to parallel process models in parallel https://docs.getdbt.com/docs/running-a-dbt-project/using-threads

dbt Core v1.5 is slated for release at the end of April, and it will include three new constructs:
- https://www.getdbt.com/blog/analytics-engineering-next-step-forwards/
- Access: Choose which models ought to be “private” (implementation details, handling complexity within one team or domain) and “public” (an intentional interface, shared with other teams). Other groups and projects can only ref a model — that is, take a critical dependency on it — in accordance with its access.
- Contracts: Define the structure of a model explicitly. If your model’s SQL doesn’t match the specified column names and data types, it will fail to build. Breaking changes (removing, renaming, retyping a column) will be caught during CI. On data platforms that support build-time constraints, ensure that columns are not null or pass custom checks while a model is being built, in addition to more flexible testing after.
- Versions: A single model can have multiple versioned definitions, with the same name for downstream reference. When a mature model with an enforced contract and public access needs to undergo a breaking change, rather than breaking downstream queriers immediately, facilitate their migration by bumping the version and communicating a deprecation window.
  
dbt bought Metricflow, dbt Core v1.6+
- https://docs.getdbt.com/docs/build/about-metricflow
    - logical models: current models
    - semantic models: KPI models
        - entities: ID
	    - dimensions: columns you aggregate / group by
	    - measures: columns you sum / avg, etc.
- https://www.getdbt.com/blog/dbt-semantic-layer-whats-next/
	- ****How to build dbt semantic layer**** https://docs.getdbt.com/blog/semantic-layer-in-pieces
- https://github.com/dbt-labs/metricflow
- https://github.com/dbt-labs/jaffle-sl-template
- https://news.kpiinstitute.org/key-performance-indicators-infographic/
- With ****dbt Explorer****, you can view your project's resources (such as models, tests, and metrics) and their lineage to gain a better understanding of its latest production state. Navigate and manage your projects within ****dbt Cloud**** to help your data consumers discover and leverage your dbt resources. https://docs.getdbt.com/docs/collaborate/explore-projects

Coalesce 2023
- Scale dbt and BigQuery
	- https://youtu.be/jevxRnJDS94?si=nZBXoJTG2Tc05SY8
 	- 22k dbt models, use macros to parameterize models, python script to general models from macros
	- BigQuery 100 concurrent queries per project, use terraform to scale projects
 	- dbtCloud 2000 models in a single job -> use Airflow + dbt core instead of dbt cloud
  	- date partition when possible, cluster keys based on most common where clauses and join keys
  	- use One Big Table approach for long running queries to avoid joins
- Secoda Data Catalog: great way to monitor end to end metadata of all your data processes
	- https://youtu.be/7hdlZ6rDa5g?si=5jO3nOfpI05WfU26
	- macro and micro metadata (table, column level)
- Select Star: best column level lineage
	- https://www.youtube.com/watch?v=bQmTS3oCJS0
- Databricks (unity catalog) + dbt works well
	- https://youtube.com/watch?v=ih4vRcFjFTo&si=pPhz4NUtBVzKQqqE 
	- https://youtube.com/watch?v=yoalcSP1lbo&si=pcbmjSdkP7r05XhK 
		- Udemy stack: ****Airflow, dbt, Databricks / delta lake, soda.io****
- dbtCloud updates
	- https://youtube.com/watch?v=NIseH-Gd-U4&si=MjQ_dSPSGQF0vqEK 
		- Dbt mesh, data contract, model version 
		- Dbt cloud cross project collaboration, dbt explorer cross project 
	- https://youtube.com/watch?v=3sp6tmYykVc&si=HABsr2cXYIdJkCRL 
		- Dbt cloud git PR incremental CI
	- https://youtube.com/watch?v=8QburYXTUuo&si=5dcb-HfJ5XLpEL4X 
		- Sqlfluff incorporated into dbt cloud ide
		- Dbt cloud cli
- ****Terraform + dbt Cloud, Fivetran, etc****
	- https://youtube.com/watch?v=vkQsGLhqF6I&si=1oOeiFz-m5yneqTf
- **Materialize**: real time data warehouse plus dbt
	- https://youtube.com/watch?v=WS23Hb9sNy4&si=37Y21Rwiyk4XxFXq
 	- https://www.youtube.com/watch?v=pLb5sFZ7nWw
- Data team advice
	- https://youtube.com/watch?v=6HLo36SjOdo&si=ymtFT7JhkUukQ5sl
		- ****Focus on metric deltas between time periods,  cohorts****
		- ****Attend non data team meetings,  e.g. marketing, revenue driving****
- dbt semantic layer (metricflow)
	-  https://youtube.com/watch?v=2Qo5_CIsSH4&si=_rjS78msW_DaLMaU 
		- Integration hex, mode, Google sheets, Tableau
	- https://youtube.com/watch?v=mqKrTZwfjbM&si=bqhZpemm8Zm_v7Dq 
		- Zenlytic llm for semantic layer
- ****Datafold catches data errors before PR merge****
	- https://youtube.com/watch?v=5Xxm6cYRmFg&si=Faw4zxqClgXjNTS5 
		- Datafold part of ci CD process 
		- Collibra data dictionary 
- ****dbt-meshify**** package
	- https://youtube.com/watch?v=FAsY0Qx8EyU&si=LB53V_XAFo2uBczK 
		- ****Auto create model contracts, versions****, groups, multiple projects, cross project dependencies
- dbt + Data Vault
	- https://www.youtube.com/watch?v=bi3x9f5lxp0 
	- https://youtube.com/watch?v=V7mPgMRCnpQ&si=_lYTYhOWGTjW5JBc
- Data Lineage using dlt and dbt
	- https://dlthub.com/docs/blog/dlt-data-lineage
- dbt + Soda.io (error monitoring)
	- https://youtube.com/watch?v=lcGHJxVLOLI&si=sj8ovWynZR-3EW11
- dbt practical advice https://www.youtube.com/watch?v=-QmCTS2viMQ
	- data engineering dbt repo, analyst dbt repo
- Semantic Layer can be used in feature store for ML
	- https://www.youtube.com/watch?v=HbpdnJv2TKc
	- Tecton best feature store
- common data models
	- https://youtube.com/watch?v=ltQgbSs99WU&si=XfBfHGqtARZHLPz9
- dbt semantic layer
	- https://youtube.com/watch?v=9aKaouNBYHw&si=tZ_ZasVEoDLP0X7i

Also see:
- Activity Schema: https://www.activityschema.com/
- https://enigma.com/blog/post/dev-stage-prod-is-the-wrong-pattern-for-data-pipelines
- ****Y42**** now better DBT IDE than DBT Cloud, has data versioning, orchestration, lineage, easy model modify & documentation, model draft or verified, etc.
	- Virtual Data Build: https://www.y42.com/blog/virtual-data-builds-one-data-warehouse-environment-for-every-git-commit/
	- https://youtu.be/_reNgMlqYu0?si=B6jUEOMsXqOojv1w
	- https://www.youtube.com/watch?v=UJ5FJ7BFP-k
 		- file names always src_object from dbt style guide, e.g. stg_trips_departures.sql / .yml, int_modelxxx.sql / .yml, etc.
	- https://www.youtube.com/watch?v=9kWkNI9k28U
 		- data analysis on Tableau
	- Y42 implicitly has data-diff in their git PR processes: https://www.linkedin.com/posts/hung-dang-y42_datafold-recently-announced-that-they-will-ugcPost-7199017036537069568-a6NC/
- https://seattledataguy.substack.com/p/data-modeling-where-theory-meets
	- ****datelist**** tables https://ctskennerton.github.io/2022/09/29/datelist-tables-at-roblox-data-engineering-meetup/

### Cumulative table design 
- Turning 100 TB data lake into 5 TBs at Airbnb with One Big Table Data Modeling https://www.youtube.com/watch?v=7JbCVXmJ1bs
![Screenshot_20240629-203119_YouTube](https://github.com/user-attachments/assets/c0ee6a0b-c049-4e88-b30d-a224a875697a)
![Screenshot_20240629-203226_YouTube](https://github.com/user-attachments/assets/b4fed636-2b0b-4c07-9f5d-763b498097a0)
![Screenshot_20240629-203249_YouTube](https://github.com/user-attachments/assets/55adfd09-0a4e-4a1c-a90b-0689533200c2)
![Screenshot_20240629-203304_YouTube](https://github.com/user-attachments/assets/a386071b-d693-4653-9de3-ac577f6a222a)
![Screenshot_20240629-203318_YouTube](https://github.com/user-attachments/assets/6e8a7cd9-e941-4e67-a425-edaff3f3a187)
![Screenshot_20240629-203335_YouTube](https://github.com/user-attachments/assets/cc7f003d-b2fd-4767-a751-00339629f50a)
![Screenshot_20240629-203351_YouTube](https://github.com/user-attachments/assets/2c4e884d-f346-4a9d-8d5e-bee17b42c54d)
![Screenshot_20240629-203446_YouTube](https://github.com/user-attachments/assets/83f51caa-6877-4d95-b6d9-95826a408c92)
![Screenshot_20240629-203457_YouTube](https://github.com/user-attachments/assets/47e20abe-1b31-44a4-b0d9-46cf7e613a0e)
![Screenshot_20240629-203507_YouTube](https://github.com/user-attachments/assets/2268fe2c-4707-4e7a-b32f-b9728e77bab6)
![Screenshot_20240629-203550_YouTube](https://github.com/user-attachments/assets/a44d77bc-4e05-430a-b404-e12fbbb61793)
![Screenshot_20240629-203557_YouTube](https://github.com/user-attachments/assets/ab56ccd9-51e6-4f6d-8f9f-2151e5efda0d)
![Screenshot_20240629-203603_YouTube](https://github.com/user-attachments/assets/da97ac7f-92cc-44f4-ac0c-5c44c08c3488)
![Screenshot_20240629-203635_YouTube](https://github.com/user-attachments/assets/5c6a73ee-e72b-4926-bcbb-661102a24a6f)

### dbt + Spark
- https://www.youtube.com/live/dwZlYG6RCSY
![Screenshot_20240701-134844_YouTube](https://github.com/user-attachments/assets/27e40147-1d82-4300-ae2f-da75f52dd77a)
![Screenshot_20240701-134848_YouTube](https://github.com/user-attachments/assets/9edbf118-83f0-49af-9114-ced7312140ef)
![Screenshot_20240701-134851_YouTube](https://github.com/user-attachments/assets/1e5d8210-7bcb-4c6f-a410-ed030c703161)
![Screenshot_20240701-134858_YouTube](https://github.com/user-attachments/assets/f53e8934-136e-4a48-918c-67b66fe96dad)
![Screenshot_20240701-134904_YouTube](https://github.com/user-attachments/assets/2fad8a05-f833-49c5-b0ca-9ca14a616b69)
![Screenshot_20240701-134907_YouTube](https://github.com/user-attachments/assets/b7b99738-ec8f-44b4-9f26-5aacde50257e)
- Hudi Live Event: Incremental Data Processing with Spark & DBT https://www.youtube.com/watch?v=vUJyYdw4igw
![Screenshot_20240628-151542_YouTube](https://github.com/user-attachments/assets/ce5e5b3d-1c53-4a7b-a91f-a4058953bdb7)
![Screenshot_20240628-151605_YouTube](https://github.com/user-attachments/assets/0d7d2719-aa28-49b7-a8e7-f03b1bc1e1b6)
![Screenshot_20240628-151708_YouTube](https://github.com/user-attachments/assets/4509b224-f15e-4200-aea4-b5f98b30bb2c)
![Screenshot_20240628-151909_YouTube](https://github.com/user-attachments/assets/bde6f55b-52cf-49cd-a5b0-eeae754fc8ea)
![Screenshot_20240628-151933_YouTube](https://github.com/user-attachments/assets/ba46ecd3-2070-4597-9079-4faf458f2420)
![Screenshot_20240628-151953_YouTube](https://github.com/user-attachments/assets/518e0322-8be4-4b34-8e4a-7d2427507293)
![Screenshot_20240628-152035_YouTube](https://github.com/user-attachments/assets/34dbe24c-616e-4a01-9df2-820a0fbdde14)
![Screenshot_20240628-152053_YouTube](https://github.com/user-attachments/assets/ac0041c8-9eba-4de5-9382-e9004902173d)
![Screenshot_20240628-152131_YouTube](https://github.com/user-attachments/assets/4c441474-7103-4565-a8ff-a6acd19aa23c)
![Screenshot_20240628-150646_YouTube](https://github.com/user-attachments/assets/f78beb76-4a1d-4f6b-b9fc-e9c365554702)
![Screenshot_20240628-152143_YouTube](https://github.com/user-attachments/assets/3010dae5-b55e-46c5-9c99-f10cca1b17cc)
![Screenshot_20240628-150535_YouTube](https://github.com/user-attachments/assets/50cefde6-83c7-480d-a271-f400cb7062bd)

### Good article about data quality checks
- https://www.linkedin.com/posts/josephmachado1991_data-dataengineering-dataquality-activity-7254825978760175616-LklH/
1. Check table constraints
The goal is to ensure your table's structure is what you expect:
* Uniqueness
* Not null
* Enum check
* Referential integrity
Ensuring the table's constraints is an excellent way to cover your data quality base.
2. Check business criteria
Work with the subject matter expert to understand what data users check for:
* Min/Max permitted value
* Order of events check
* Data format check, e.g., check for the presence of the '$' symbol
Business criteria catch data quality issues specific to your data/business.
3. Table schema checks
Schema checks are to ensure that no inadvertent schema changes happened
* Using incorrect transformation function leading to different data type
* Upstream schema changes
4. Anomaly detection
Metrics change over time; ensure it's not due to a bug.
* Check percentage change of metrics over time
* Use simple percentage change across runs
* Use standard deviation checks to ensure values are within the "normal" range
Detecting value deviations over time is critical for business metrics (revenue, etc.)
5. Data distribution checks
Ensure your data size remains similar over time.
* Ensure the row counts remain similar across days
* Ensure critical segments of data remain similar in size over time
Distribution checks ensure you get all the correct dates due to faulty joins/filters.
6. Reconciliation checks
Check that your output has the same number of entities as your input.
* Check that your output didn't lose data due to buggy code
7. Audit logs
Log the number of rows input and output for each "transformation step" in your pipeline.
* Having a log of the number of rows going in & coming out is crucial for debugging
* Audit logs can also help you answer business questions
Debugging data questions? Look at the audit log to see where data duplication/dropping happens.
DQ warning levels: Make sure that your data quality checks are tagged with appropriate warning levels (e.g., INFO, DEBUG, WARN, ERROR, etc.). Based on the criticality of the check, you can block the pipeline.
Get started with the business and constraint checks, adding more only as needed. Before you know it, your data quality will skyrocket!

### dbt models should always be incremental
- https://medium.com/@AtheonAnalytics/supercharging-dbt-vol-2-how-we-modified-dbts-incremental-materialisation-to-more-than-halve-f5def3ecbe3f
- https://www.linkedin.com/posts/hugo-lu-confirmed_dbt-merge-dbt-activity-7254772352696074241-vNKh/
	- For log-type / eventtype / anything with a proper updated on field or ID there is no excuse for not writing an incremental model
	- merge is powerful but expensive. I almost always use insert_overwrite !
	- When working with large datasets, full refreshes can be expensive and time-consuming. That's where incremental models in dbt come in! They allow you to process only the changes, making your ETL pipelines more efficient. But not all incremental strategies are created equal. Let’s break down a few of them:
- Append :inbox_tray:
	- Simply adds new rows without touching existing data.
	- Best for: Logs and time-series data where records are immutable.
- Merge :arrows_counterclockwise:
	- Combines new and existing records, updating or inserting as needed.
	- Best for: Fact tables where data can change, like sales or inventory.
- Delete + Insert :scissors::heavy_plus_sign:
	- Deletes existing rows and then inserts new data.
	- Best for: Cases where you want to ensure only unique records stay in the table.
- Insert Overwrite :package::arrows_counterclockwise:
	- Overwrites existing partitions with new data, great for managing data in chunks.
	- Best for: Partitioned data where you want to keep things tidy, like monthly reports.
- Microbatch :stopwatch::arrows_counterclockwise:
	- Continuously processes small batches of new data.
	- Best for: Real-time analytics, streaming data, or minimizing data processing windows.
- Each of these strategies has its own use cases, so understanding when to use them can be a game-changer for your data pipelines. :bulb:

- https://github.com/OpenLineage/OpenLineage/tree/main/integration/dbt
