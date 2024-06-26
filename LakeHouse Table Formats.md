# LakeHouse Table Formats

## Delta Lake Uniform: Iceberg, Delta Lake, Hudi

- Apache XTable: Interoperability with Hudi, Iceberg, and Delta Tables https://www.youtube.com/watch?v=8IukpmyGDB8
	- works with Spark, AWS glue catalog
- Data Lake Table formats: https://youtube.com/live/mXitwotQaAU?feature=share
	- https://tabular.io/guides/
    - Apache Iceberg: most comprehensive format, supports table / catalog versioning that the other formats don't, but isn't as good for stream processing
    - Apache Hudi: event based table format, for events
    - Delta Tables: periodic log checkpoints
    - https://delta.io/blog/delta-lake-vs-parquet-comparison/
    - https://medium.com/starschema-blog/open-table-formats-for-efficient-data-processing-delta-lake-vs-iceberg-vs-hudi-b1107141e9a6
    - https://www.onehouse.ai/blog/apache-hudi-vs-delta-lake-vs-apache-iceberg-lakehouse-feature-comparison
    - https://iomete.com/blog/apache-iceberg-delta-lake
    - Open Lakehouse Architecture: https://www.linkedin.com/posts/alexmerced_cloud-based-open-lakehouse-architecture-activity-7107740230387912705-fAlb/ 
- Iceberg vs. Hudi vs. Delta Lake https://www.youtube.com/watch?v=rQ_jNoDr3KE
![Screenshot_20240621-164745_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d4f67a85-d544-41fe-9843-662bdd8c79f6)
![Screenshot_20240621-164751_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c2544cc5-5d83-40e2-b2ee-4d3cd1062c68)
![Screenshot_20240621-164757_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dff53663-ef6c-4a8f-8b54-fd4ab1c70f8a)
![Screenshot_20240621-164802_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d51eed58-0d42-43f6-9fe7-17d594aea31d)
![Screenshot_20240621-164806_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e0f00219-96f8-4d8b-8ad4-4a9a1bf94c53)
![Screenshot_20240621-164816_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/abcd71e2-984f-4839-bb3f-05ec63205c33)
![Screenshot_20240621-164826_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2a8c2890-2a8a-4cbc-a22b-3d71316c1d59)
![Screenshot_20240621-164829_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b666df3-3e50-4b62-99f5-be8976b25125)
![Screenshot_20240621-164832_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f11be0bd-61aa-4005-a4b7-edc63771d623)
![Screenshot_20240621-164836_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a16768ce-2c1a-4e3e-962b-78fe01ca5056)
![Screenshot_20240621-164839_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a949494f-7c69-4438-9059-5d361d53369b)
![Screenshot_20240621-164842_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f0cbe3f7-8721-4ad7-ab80-dc86ed9af994)
![Screenshot_20240621-164859_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cc01a364-835a-4b8b-ac3d-605979aba496)
![Screenshot_20240621-164909_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/93e58a8e-6b52-4303-be82-3f5ecf3c55be)
![Screenshot_20240621-164914_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/efda7d91-3958-4b92-b937-842d9ceff205)

## Arrow

- https://www.linkedin.com/posts/jorritsandbrink_dataengineering-softwareengineering-activity-7210043267881549824-7dv-/
	- Parquet and Arrow are complementary. Both can be considered "the standard" in their domain.
		- Parquet is an on-disk format.
  		- Arrow is primarily an in-memory format¹
- Similarities — both are:
	- designed for analytics
	- "hybrid columnar" ➜ column chunks are stored contiguously within row groups²
- Differences:
	- Parquet uses general-purpose block compression (e.g. Snappy), Arrow does not³
	- Parquet encodes heavily, Arrow does not⁴
- They optimize for different things:
	- Parquet is small on disk and on wire ➜ good if storage or network is bottleneck
	- Arrow does not compress and encode ➜ good if compute is bottleneck
- Last but not least, Arrow supports O(1) "random access", while Parquet needs to decompress and decode entire "pages" to access individual values.
- The small print:
	- ¹ Arrow can also be serialized on disk (".arrow" file) or sent over a wire.
 	- ² Parquet speaks of "column chunks" and "row groups". Arrow calls them "arrays" and "record batches".
  	- ³ Compression can be disabled in Parquet.
  	- ⁴ Arrow does support dictionary encoding.

## Delta Tables

- Delta Live Tables https://docs.databricks.com/en/delta-live-tables/tutorial-sql.html 
	- Delta Live streaming tables, delta live tables (batch, aggregation)
	- Delta tables have checkpoints, including streaming tables
	- Delta Live Expectations: data quality constraints
	- enhanced autoscaling: primarily for streaming data
 	- https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/transform
  		- DLT (bronze, raw, incremental, streaming) -> DLT (silver, cleaned) -> Materialized View (Gold, aggregates)
    	- https://stephenallwright.com/materialize  Materialized View vs Table
     		- If you need to store data long term and use it as part of a data model then you should create a table, however if you want to join multiple tables and query this infrequently, as part of an analysis for example, then a materialized view would be the better choice.

## Apache Hudi

## Apache Iceberg

- Also see Apache Iceberg: https://www.linkedin.com/posts/sesha-reddy-pattem-543aa311b_apacheiceberg-datamanagementbrilliance-metadatamastery-activity-7100064046502027266-FsDs/
	- Iceberg 101: https://tabular.io/guides-and-papers/
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
	- partition evolution, table versioning, catalog versioning
- Polars is a pandas replacement: https://www.confessionsofadataguy.com/replacing-pandas-with-polars-a-practical-guide/
- Apache Iceberg Overview (Jan 2024 Edition) - Architecture, Ecosystem, and more! https://www.youtube.com/watch?v=stJLaIZRcJs
![Screenshot_20240621-165232_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/07200201-636e-4d52-879d-08f8ea163618)
![Screenshot_20240621-165238_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/76411304-0823-48af-ad34-0b05a90a1363)
![Screenshot_20240621-165241_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/98a7d94e-6071-427b-accb-cb54507e34e9)
![Screenshot_20240621-165245_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc496e1d-c026-4481-8c25-3192ce420c42)
![Screenshot_20240621-165301_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a2804bd5-a1fc-42c7-a088-614e2fcab35a)
![Screenshot_20240621-165307_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a9b1d3fa-deb9-4e51-961b-151a16bc9a6d)
![Screenshot_20240621-165310_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0e3cadbc-26b4-4a3c-ba18-10d9fb4106e4)
![Screenshot_20240621-165408_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bc8c57c8-5f50-4d27-a2ef-3fae84a18b4a)
![Screenshot_20240621-165413_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e5a3a00a-4c95-4ded-8ad0-280362a8a61f)
![Screenshot_20240621-165419_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/68445ae4-b73c-4d96-920a-4e4718f94140)
![Screenshot_20240621-165427_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3e70db46-8429-41fb-8c09-6a66baa88e20)
![Screenshot_20240621-165502_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/813f1bdc-2c97-45e2-a11e-e6cbe82e16e7)
![Screenshot_20240621-165507_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5e098aa4-acd6-4582-9a09-8f45e36c9da1)
![Screenshot_20240621-165515_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c89a1e07-cd14-457b-ada7-b55b138eb46f)
![Screenshot_20240621-165534_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4219e94d-ee48-4d1d-a98c-96e31c1eebee)
![Screenshot_20240621-165538_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/66646ba9-b266-4cc6-a309-4ea13b2238f1)
![Screenshot_20240621-165541_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/612d3689-07df-4e0e-ad9a-d08211a0e9fb)
![Screenshot_20240621-165554_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7ae20f72-8410-4e8a-81bb-bba71f7752c9)
![Screenshot_20240621-165557_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c350d6f6-7fd6-4716-9542-ac917b32c776)
![Screenshot_20240621-165606_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a8f0677f-0ff5-433a-b684-f2afb914ae63)
![Screenshot_20240621-165612_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/861b9c13-5f58-473f-8a78-a292f5553a7c)
![Screenshot_20240621-165639_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d0688185-b230-4cfc-82e7-724e36277954)
![Screenshot_20240621-165653_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/50fc441a-adbd-4f9f-b5c6-fef7cc921f46)
![Screenshot_20240621-165657_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/163ed6cf-4257-4e8c-b407-d0b909f849a4)
![Screenshot_20240621-165714_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c171e8bf-4c60-46cc-9604-74cff6385929)
![Screenshot_20240621-165721_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7aa32574-b569-4ed9-9b0f-7dda4fca153e)
![Screenshot_20240621-165835_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ba836850-97a8-4e6c-bdd9-931e052ecca4)
![Screenshot_20240621-165836_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/86fa5220-0383-49a3-ad48-a196477d7847)
![Screenshot_20240621-165839_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ef44fb48-ab49-425e-b437-a0c6d36d0784)
![Screenshot_20240621-170005_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cc9b1d33-76a3-449e-b2fb-1894d05261fc)
