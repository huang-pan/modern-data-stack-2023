# LakeHouse Table Formats

## Delta Lake Uniform: Iceberg, Delta Lake, Hudi
- Apache XTable: Interoperability with Hudi, Iceberg, and Delta Tables https://www.youtube.com/watch?v=8IukpmyGDB8
	- works with Spark, AWS glue catalog
	- X-Table convert from Hudi to Iceberg, Delta and ingest to Unity Catalog https://www.youtube.com/watch?v=1SKQRrenBj4
	- Apache XTable™ is a standalone github project that provides a neutral space for all the lakehouse table formats to constructively collaborate together.
	- Delta Lake Uniform is a one-directional conversion from Delta Lake to Apache Hudi or Apache Iceberg
	- https://www.youtube.com/watch?v=ybJ_wa2CRcQ
![Screenshot_20240729-101629_YouTube](https://github.com/user-attachments/assets/de7b8939-bb4c-41c4-8798-3b8579422cdd)
![Screenshot_20240729-101506_YouTube](https://github.com/user-attachments/assets/eae6e182-1e94-4f73-8402-2eecbe4c4cd6)

- Delta Lake Uniform: Databricks bought out Tabular (Iceberg) in 2024, unifying Delta Tables, Iceberg, Hudi
![Screenshot_20240618-103517_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2616d198-3abf-47f3-90d1-69ee570c66a0)
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
![Screenshot_20240703-183350_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8bf43bfe-6622-4d39-ab90-ffc64c4d3ca9)

## Arrow
- In memory columnar data store (serialized, deserialized) https://www.youtube.com/watch?v=YhF8YR0OEFk
![Screenshot_20240703-175329_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b23f5828-5de9-41ea-8299-a86e8a42d609)
![Screenshot_20240703-175355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0482f47d-2c22-4512-b928-b564cc3ef842)
![Screenshot_20240703-175404_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4a74dea4-ba39-47e2-a889-0d96c5fc8562)
![Screenshot_20240703-175414_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cfda9c3d-19fb-494c-a5d8-30e62b20113b)
![Screenshot_20240703-175442_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9d271cb7-d25e-4909-ba4d-db9b4c905ca6)
![Screenshot_20240703-175506_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fdfc33fa-2301-488a-9e91-160b73af759b)
![Screenshot_20240703-175512_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/687513e0-c209-450e-a4f8-b3f5df9c82e0)
![Screenshot_20240703-175516_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2a3b3542-c60a-4435-b6b1-c0142f27fddf)
![Screenshot_20240703-175522_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0cf7824f-d214-4edd-854b-e47c4d874e2d)
![Screenshot_20240703-175525_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/17cf8f2e-36ae-4cbd-a204-3ff04d4902cb)
![Screenshot_20240703-175530_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/974622b6-e836-4c1e-86d0-b0a549b20ac7)
![Screenshot_20240703-175537_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dac2def8-ebae-41c7-b4dd-8042d468936e)
![Screenshot_20240703-175541_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3f8b0982-5f4c-4e90-8296-2509eb73e107)
![Screenshot_20240703-175546_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/70ebf2d0-ff26-405d-b80f-ebb7502758f1)
![Screenshot_20240703-175550_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0ba71a3a-a18d-407f-b0a6-989be22aa857)
![Screenshot_20240703-175553_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d79a835a-5738-454b-9c81-43e0b73d6fbd)
![Screenshot_20240703-175556_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/99f77b75-f3cf-47a8-979d-3437e085252f)
![Screenshot_20240703-175604_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/717d4359-5b46-4225-af69-b055f7d9db9f)
![Screenshot_20240703-175608_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/82fdb3cf-0982-4a67-a770-bfd09bcc6da0)
![Screenshot_20240703-175611_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/82268a6d-67f1-41f5-b733-255c360a23f5)
![Screenshot_20240703-175615_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e21db4f8-77d9-4035-a962-233dfd17fe5f)
![Screenshot_20240703-175618_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bd80237b-27c2-400e-b739-860ad5cc98bf)
![Screenshot_20240703-175629_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/26fa4f8b-01e4-40ae-bc6d-7bc3a561dbd7)
![Screenshot_20240703-175637_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/220c9d6e-939d-44c7-8811-8f3cfebb8c49)
![Screenshot_20240703-175642_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/726ae9f3-4bde-465b-977c-ffb6f45b4dec)
![Screenshot_20240703-175654_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/290e446e-b13b-4f48-a603-628a34b26527)
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

## Delta Tables / Databricks
![Screenshot_20240703-183342_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8fad028a-4ecf-4516-a4d3-015bcdef60d7)
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
![Screenshot_20240703-183355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8d4e34a0-9f11-49c2-b5c4-9dc0415b428f)
- Intro to Hudi basic https://www.youtube.com/watch?v=-Wp7itPDtgo
![Screenshot_20240628-150304_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/97c37c79-4cd2-4435-9169-7bf3a06987e5)
![Screenshot_20240628-150328_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1111f631-0635-41f7-9856-03c93470f146)
![Screenshot_20240628-150345_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cf04a4f6-f2d2-4a68-824a-c6e72ac48e2f)
![Screenshot_20240628-150405_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1aff8052-5fe9-4a76-82c2-c26bfb89910c)
![Screenshot_20240628-150433_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d1b6e6cd-fa8e-432f-b5dc-fcecc43d0e72)
![Screenshot_20240628-150444_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2eaadc5d-e62d-4eff-85f3-436240bdc921)
- Intro to Hudi https://www.youtube.com/watch?v=TvXFVkcZUlU
![Screenshot_20240703-054259_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b2e23d5d-8674-4bb6-9439-c19b43d7763b)
![Screenshot_20240703-054313_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4483ca46-8895-40c6-bc3f-a8428543e666)
![Screenshot_20240703-054320_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/86fba8a4-d724-414a-81df-08a80529735e)
![Screenshot_20240703-054326_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e7011717-c7d4-4f57-90aa-44e806fbf84c)
![Screenshot_20240703-054334_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1b821695-b593-4135-bad6-d24f1ead5a91)
![Screenshot_20240703-054353_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a058dc90-0256-4b21-b67b-853d7cbb7ab1)
![Screenshot_20240703-054357_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2e3b8982-8af9-4c6e-97d9-1d713bf781a0)
![Screenshot_20240703-054400_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4e6f49fc-c9a6-477d-97c9-034ba0e06d5d)
![Screenshot_20240703-054406_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/835eee51-7af6-4eca-8d9a-901290958c7a)
![Screenshot_20240703-054411_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a2792fc6-6875-4b63-9d15-1e623df11c94)
![Screenshot_20240703-054430_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2126c994-463a-49be-8f89-1484afe99447)
![Screenshot_20240703-054434_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1bd0d291-16c2-4860-a161-34442ccb17db)
![Screenshot_20240703-054500_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4e6620e6-09c5-4efb-8b39-e13a751cf553)
![Screenshot_20240703-054517_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c19057c9-d12d-4044-b3d1-98f037a3d82b)
![Screenshot_20240703-054526_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d4aae68a-eb17-4944-b799-361c6ce32602)
![Screenshot_20240703-054538_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8df56396-bf1d-4d04-8f95-4e506fe63ffb)
![Screenshot_20240703-054546_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/74d4ea61-d26b-4d8a-b0fb-2f03291cc23e)
![Screenshot_20240703-054554_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/28d0d4d8-f00d-46e6-bb8f-5e0c03924384)
![Screenshot_20240703-054606_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fb03cd48-4a7e-477e-9a58-02fbdd5159a5)
![Screenshot_20240703-054620_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1fbc2c42-4192-4ba0-b682-20a493a9a5bb)
![Screenshot_20240703-054624_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6544f2b5-4469-47af-9f78-71b123c87eff)
![Screenshot_20240703-054627_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ff887d4-082a-4f56-b864-1fd345bf8cb3)
![Screenshot_20240703-054634_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/49bec689-a56f-4ade-bc57-958f4d0352ff)
![Screenshot_20240703-054637_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/27b7ef33-388f-4564-b220-f801f727f7e4)

## Apache Iceberg / Tabular
![Screenshot_20240703-183402_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/616293c2-7a2c-4180-ad54-f461f859ab14)
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
- Vendors supporting Iceberg https://iceberg.apache.org/vendors/
	- CelerData, ClickHouse, Cloudera, Dremio, Iomete, ****PuppyGraph****, Snowflake, Starburst, Tabular, ****Upsolver****

### Apache Iceberg Overview (Jan 2024 Edition) - Architecture, Ecosystem, and more!
- https://www.youtube.com/watch?v=stJLaIZRcJs
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

### Iceberg table optimizations
- https://www.youtube.com/live/rLs4bjtXSrg
![Screenshot_20240701-164726_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0d223a7d-d15b-40db-a7d6-116cc28090f1)
![Screenshot_20240701-164729_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/93796673-08da-4607-9d07-e1f640487a43)
![Screenshot_20240701-164750_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c37aaafd-b9bd-4b1e-88b6-cf1300a8e673)
![Screenshot_20240701-164756_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/46fd4827-911a-4b64-b5ea-1ceb9150db8a)
![Screenshot_20240701-164805_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1a204a28-f496-470f-9160-649554c28d56)
![Screenshot_20240701-164938_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1bee0e68-654d-47df-ab13-a08654c15c3f)
![Screenshot_20240701-164944_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3ea7bdfc-92b3-4595-a28a-e7bb733afa9f)
![Screenshot_20240701-164948_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/78deac82-c20f-43ad-a537-b6559e8982bb)
![Screenshot_20240701-164951_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/18d1dbef-719c-4aa6-a349-7b8157e0fd82)
![Screenshot_20240701-165001_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/23d4a2bb-d4eb-4bbd-9024-5091c742d3a5)

## Iceberg Catalogs
- Deep Dive into Apache Iceberg Catalogs (Nessie, Hive, REST Catalog, Hadoop) https://www.youtube.com/watch?v=IENHQpIA5l4
	- Great youtube channel for open lakehouse info
