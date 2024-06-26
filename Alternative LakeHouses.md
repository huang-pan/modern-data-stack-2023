# Alternative LakeHouses

## Dremio
- Open source, unified data lakehouse solution https://www.youtube.com/watch?v=cc6CCQpg1FA
	- 1 to 5 minute latency from data sources
	- has own semantic layer
	- product targeted towards existing enterprises with many data sources and complex data engineering
 		- can replace databricks, pinot, presto, etc.
   		- better than AWS Athena
- zero-etl solution: databases, snowflake, etc. accessible as data sources in lakehouse, no need to copy and move data
	- https://www.dremio.com/wp-content/uploads/2023/12/Episode-41-Zero-ETL.pdf
	- Snowflake as data source https://www.youtube.com/watch?v=Aa2xAfI8wNs
 	- Dremio Arctic: uses Iceberg's data versioning, ****data versioned as code**** (like Y42), auto optimization, data catalog
- has own SQL warehouse compute solution, cheaper than Snowflake? yes
	- Dremio Sonar: uses Apache Arrow (great for in-memory querying, column store)
- uses Apache Iceberg under the hood (superior to Delta Table, Parquet; has strong data versioning / data catalog, automated partitioning, time travel, ****partition versioning, schema evolution****, )
 	- Dremio data reflections replicates data from data sources into queryable Apache Iceberg files
- Project Nessie for CI/CD on Dremio's LakeHouse https://www.youtube.com/live/xqF8sgIBiDA
- Data sources supported:
	- https://docs.dremio.com/current/sonar/data-sources/
	- https://docs.starburst.io/latest/connector.html
- BI tools supported:
	- https://docs.dremio.com/current/sonar/client-applications/clients/
 	- https://docs.starburst.io/clients/index.html
 	- currently no Sigma Computing support
- real life performance: ?
	- https://www.starburst.io/platform/compare/dremio/
 	- https://www.reddit.com/r/dataengineering/comments/17svlvl/dremio_vs_starburst/
- Dremio vs Starburst vs lakeFS
	- Dremio 351 https://www.linkedin.com/company/dremio/people/
 	- Starburst 552 https://www.linkedin.com/company/starburstdata/people/
  	- lakeFS https://www.youtube.com/@lakefs/videos
- Can have Snowflake Reflection (Snowflake as a data source -> Dremio query cheaper, faster than Snowflake query) https://www.youtube.com/watch?v=TLVnfCXlfrI
![Screenshot_20240620-165337_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/54726359-9890-4540-bc76-ffa6184f89b0)
![Screenshot_20240620-165353_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/437a2f0b-667f-40f9-993c-54694b646d60)
![Screenshot_20240620-165405_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a2b9450a-0c2e-4cd2-9eaa-b98e605f6662)
![Screenshot_20240620-165415_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f447286a-d6e9-45bb-81cc-d78aee952bbf)
![Screenshot_20240620-165421_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/98a85129-0a10-430d-bacb-3522da3dd689)
![Screenshot_20240620-165435_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1caf41ed-d951-4457-bf3d-e26f8aee246b)
![Screenshot_20240620-165444_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a2451dde-77c8-4f09-9733-01ad7825fcee)
![Screenshot_20240620-165454_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/401d74e3-6ed0-4f46-85ce-f0efb98a13fe)
![Screenshot_20240620-165503_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5f8ff7d2-f2e6-4bbe-9f65-d13e3df1a733)
![Screenshot_20240620-165510_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0a6aa249-c493-4773-aebc-4a2e78f71c0b)

## Apache Doris / VeloDB

- Apache Doris is an open source, real time data warehouse / LakeHouse https://doris.apache.org/
	- https://www.velodb.io/ is the commercial version of Doris
 	- https://www.linkedin.com/company/velodb/people/ they are in China
- StarRocks is a fork of Doris
- Doris architecture https://www.youtube.com/watch?v=w_hreEaiDQ4
![Screenshot_20240622-075920_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7b537b81-a070-4432-9231-c8832b845cd8)
![Screenshot_20240622-080105_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4a36143e-4a96-4f10-8e9a-90ac676e05f2)
![Screenshot_20240622-080207_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/da86add7-9560-48be-8a63-88149fb1c318)
![Screenshot_20240622-080216_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5a0d1cc3-596d-4b34-acfa-bb596211f114)
![Screenshot_20240622-080455_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a1f58285-9c33-4638-ac1b-e7cbd717ab91)
![Screenshot_20240622-080459_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ff53bbe2-246a-4828-bf17-eec3dd190a79)
![Screenshot_20240622-080520_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2d913546-3dab-41d0-9df9-960817bbc4ad)
![Screenshot_20240622-080532_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4dfa586-5f87-4e0f-b1bd-2c5e99e9a778)
![Screenshot_20240622-080552_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/474d05a8-4481-4cf7-b64b-a1467ffb0ca8)
![Screenshot_20240622-080558_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/72dc13d8-a6b9-4aad-940e-db66dabbc283)
![Screenshot_20240622-080609_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e9dcfc52-1b65-4430-a2a2-ef6c8a40de83)
![Screenshot_20240622-080625_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7a5f893d-9ab5-49a5-ba92-f2a72ae96868)
![Screenshot_20240622-080628_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/cba9f12f-1b4c-426b-888d-356b26062196)
![Screenshot_20240622-080647_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d1b27ac3-6edc-4302-b40f-0f8458ef3c23)

## StarRocks / CelerData

- StarRocks / CelerData fastest RT LakeHouse query engine: Iceberg, etc.
