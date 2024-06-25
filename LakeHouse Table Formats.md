# LakeHouse Table Formats

## Delta Lake Uniform: Iceberg, Delta Lake, Hudi

- Delta Live Tables https://docs.databricks.com/en/delta-live-tables/tutorial-sql.html 
	- Delta Live streaming tables, delta live tables (batch, aggregation)
	- Delta tables have checkpoints, including streaming tables
	- Delta Live Expectations: data quality constraints
	- enhanced autoscaling: primarily for streaming data
 	- https://learn.microsoft.com/en-us/azure/databricks/delta-live-tables/transform
  		- DLT (bronze, raw, incremental, streaming) -> DLT (silver, cleaned) -> Materialized View (Gold, aggregates)
    	- https://stephenallwright.com/materialize  Materialized View vs Table
     		- If you need to store data long term and use it as part of a data model then you should create a table, however if you want to join multiple tables and query this infrequently, as part of an analysis for example, then a materialized view would be the better choice.
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