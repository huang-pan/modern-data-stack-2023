# Real Time Data Warehouses

***RT OLAP***

## RocksDB / Rockset

- Rockset replicates AWS DynamoDB tables https://www.youtube.com/watch?v=JGIzdFHZVXs
	- Rockset search and analytics DB https://www.youtube.com/watch?v=xGaUJTHuehQ
 	- Essentially makes a low latency copy of data source using 
		- converged indicies: row based index, column based index, inverted (document) index
- Rockset product overview https://www.youtube.com/watch?v=4nEQpISidw4
![Screenshot_20240620-104355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0baab291-2d40-4db4-9efc-8ed3b2820df8)
- Rockset architecture https://www.youtube.com/watch?v=msW8nh5TTwQ
![Screenshot_20240620-115528_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8cd2eb60-95ca-4e0d-950d-0bd92ec6f27d)
![Screenshot_20240620-115550_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4cb73583-4b99-475a-9efe-c48a65875721)
- Snowflake export to S3 import to Rockset https://www.youtube.com/watch?v=siAqYzlcEiU


## ClickHouse

- ClickHouse https://www.youtube.com/watch?v=HRh5setqGCU 
	- RT data warehouse
		- internet scale event data, very fast aggregations, very resource efficient, less expensive
		- low latency 100 ms, high concurrency
	- main use cases
		- fraud detection, eccommerce
		- sentiment analysis
		- sales and marketing analytics
		- customer usage data, billing usage data
		- low latency, high concurrency: B2B SaaS 1/3
		- cloud DW: perf, cheaper than Snowflake 1/3
		- observability, logging, tracing, metrics, Elasticsearch Logstash Kibana 1/3
- ClickHouse bad at joins https://www.youtube.com/watch?v=1xvFZskEp1o
	- StarRocks good at RT joins, cost based query optimizer
	- Clickhouse bad at RT joins, good for RT log search, rule based query optimizer 
![Screenshot_20240620-155335_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/baf6af95-fdfd-4909-8f9b-5fd6f9c3572a)
![Screenshot_20240620-155342_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4d87720-36bc-49e5-a9c4-6cd85cc54be7)
![Screenshot_20240620-155351_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8965b522-2ba9-487a-a273-6864213f5f2c)
![Screenshot_20240620-155356_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7771ba48-da75-4d40-b1c5-5def7789415f)
![Screenshot_20240620-155416_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fca6e407-4baa-474e-8c39-fb62758817db)
![Screenshot_20240620-155430_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/537cbbdc-6716-4cbf-a610-cf9ce1dd14c5)
![Screenshot_20240620-155436_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc05c366-0596-43ce-aba7-de67d3fc2c85)
![Screenshot_20240620-155442_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a7fb417f-ccc1-48e5-a54d-0d7be3626d6f)
![Screenshot_20240620-155445_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3ddd6b93-d4ec-4d7c-87f9-3978e576cefc)
![Screenshot_20240620-155452_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/009ec7d5-3dc6-4b48-8165-28e50f59a4a1)
![Screenshot_20240620-155458_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/aadee248-e9f3-4c56-b0e9-81ec02ebd4b2)
![Screenshot_20240620-155504_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/00ea382d-1179-4e97-87ab-300d8a414740)
![Screenshot_20240620-155520_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a20840f0-5c45-4b3d-9e14-b124e968a4d4)
![Screenshot_20240620-155523_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/278a91f6-cb24-4a31-bee5-03cf48ccc975)

## Firebolt

- Firebolt fastest RT cloud data warehouse https://www.youtube.com/watch?v=K0g4GUY7PMI
	- faster, cheaper than Snowflake
![Screenshot_20240620-161328_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fbb56250-63ea-48aa-b449-d13ae8343f98)
![Screenshot_20240620-161346_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/269536c7-b5dd-4f50-9236-cd94df745cd1)
![Screenshot_20240620-161358_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fa1d4102-a007-4976-812e-61140c134dd1)
![Screenshot_20240620-161419_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ce84079-ebb6-420e-bed2-5081e2ac6874)
![Screenshot_20240620-161434_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ed1c63ae-02d7-4a19-b956-ad3da2026de2)


## Materialize

## Tiny Bird + Snowflake

## Pinot / StarTree

- Apache Pinot / StarTree https://www.youtube.com/watch?v=F8Q_pGIH9yY
![Screenshot_20240621-154808_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9f6455ba-3cc2-43e7-83b1-2df50b8cd8fb)
![Screenshot_20240621-154846_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/41e06c92-dd6e-4c9a-8766-625afb81f6f9)
![Screenshot_20240621-154933_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/329182ec-36d2-4cf0-911d-c1aa0d0ff7b8)
![Screenshot_20240621-155015_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/df5088db-dd69-4599-993e-ae92703ca0d2)
![Screenshot_20240621-155033_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ea8332dd-ef3c-47c3-8f61-bf1c8f6b2bd6)
![Screenshot_20240621-155058_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4b6917b4-aaf4-4e0d-9a2d-9685998beb41)
![Screenshot_20240621-155135_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5a45f2c8-53b4-4d45-866c-0044ac86705f)
![Screenshot_20240621-155156_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/749f6d0c-bfa6-4b95-90f0-fecf996c2ac3)
![Screenshot_20240621-155200_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/385c51ba-d55e-4dfe-bd05-7e88576e391f)
![Screenshot_20240621-155215_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ffa98b6d-77d4-4fb1-9b9a-33ed280e62ec)
- Pinot Architecture https://www.youtube.com/watch?v=vYjef-KTuzY
![Screenshot_20240621-155801_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f40d6d17-02dc-40ae-a655-8a7458002f44)
![Screenshot_20240621-155819_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b2feab2c-c98f-4fcd-a186-703643a443b9)
![Screenshot_20240621-155828_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/13d14dd9-8dae-4c93-a54e-e4b57d9c41d2)
![Screenshot_20240621-155902_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e46f463d-957d-4916-858a-44dd28a4ea8e)
![Screenshot_20240621-155942_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e619b096-e1fc-4933-92ea-1e33c4922e6e)
![Screenshot_20240621-155950_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1b080d9b-3193-4799-a4b6-df7978d0187c)
![Screenshot_20240621-160014_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b4e5974-c484-488f-9497-38a181e61899)
![Screenshot_20240621-160045_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee7c466f-9d20-4ec7-9ae2-77b006d10cf0)
![Screenshot_20240621-160120_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8bc779ec-063f-47b1-af53-df8dc9bf5a0a)
![Screenshot_20240621-160129_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/99a30dd5-5c8f-49d7-87c3-8d19aa410cc7)
![Screenshot_20240621-160142_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2caae1f0-2efe-4851-a062-932e8ec1053e)
![Screenshot_20240621-160239_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/12e990b3-342f-481a-928d-ccb15b40a12e)
![Screenshot_20240621-160249_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/594bc3bf-33ec-4946-bd22-23268571b7ab)
![Screenshot_20240621-160304_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8da8cdbd-6ae0-4fbf-8bb4-2f05126e5f52)
![Screenshot_20240621-160310_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b862b8c-b05b-43ba-b84c-b8e281c84010)
![Screenshot_20240621-160324_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75ec2692-1ca2-4591-ad5d-261eeae76100)
![Screenshot_20240621-160330_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fdcb3292-5394-47b5-8b5e-3be1dff966d8)
![Screenshot_20240621-160344_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/39579a85-e325-431f-97b0-bf711f133bcf)
![Screenshot_20240621-160355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1042384d-78ce-42ed-8a1e-ae7115dfb52e)
![Screenshot_20240621-160412_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9fa1aa9c-1dc1-4a63-a80d-2702d45968c1)
![Screenshot_20240621-160438_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/13749ca6-eba0-4b35-ada9-4f46f8785be3)
![Screenshot_20240621-160448_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6a577648-3f9b-4f67-916e-be290050ef57)
![Screenshot_20240621-160455_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3c095ba3-3f58-41ea-be16-7148f12bb4db)
![Screenshot_20240621-160515_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/43c9df67-a599-414b-ba12-9abb48ed3be0)

## Druid / Imply

- Druid older technology trying to modernize https://www.youtube.com/watch?v=4qP_z8n8in0
![Screenshot_20240620-171956_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/71cf93e8-739b-4174-95bc-dced43b3a9d7)
![Screenshot_20240620-171959_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/96560803-433d-4ae7-b84b-79fc60e629fa)
- Druid still behind? https://www.youtube.com/watch?v=wgJaB_PuHO4
![Screenshot_20240620-172640_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f9fdf6f9-c52c-49ce-96ab-4e12d746a737)
![Screenshot_20240620-172748_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b17ce331-2bf3-4410-8210-d42c5895fa17)
![Screenshot_20240620-172802_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8e4202ff-0842-491b-b7ba-212ee5e06692)
![Screenshot_20240620-172822_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dc153468-9aa2-4463-9ea2-7d148a60ac6e)
![Screenshot_20240620-172828_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/591fac46-6e5f-477c-b9f3-5915dd4efa3b)

