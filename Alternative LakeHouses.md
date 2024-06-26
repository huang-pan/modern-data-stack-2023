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

## StarRocks / CelerData

- StarRocks / CelerData fastest RT LakeHouse query engine: Iceberg, etc.
