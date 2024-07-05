# Stream Processing

## Stream processing frameworks: streaming ETL, streaming analytics, streaming databases

## Decodable
- https://www.decodable.co/
	- Managed alternative to Flink, connects to Kafka, etc, does streaming ETL
	- example connect to coinbase API https://www.youtube.com/live/77l0bzWlYPM
- Snowplow
	- Customer data augmentation in real time (structured behavioral data)

## Streaming system design
- https://www.linkedin.com/posts/nagarajulu_systemdesign-probablisticdatastructures-performace-activity-7096705093797875712-E7bv/
    - filter out streaming inputs
- Popular streaming technologies
	- https://www.youtube.com/watch?v=2zEYG2p0TRo
	- https://www.linkedin.com/pulse/spark-streaming-vs-flink-storm-kafka-streams-samza-choose-prakash
 	- https://blog.scottlogic.com/2018/07/06/comparing-streaming-frameworks-pt1.html
  	- https://www.youtube.com/watch?v=K-NYuwzpvEM
	- Flink
		- Flink real stream processing framework, lower latency, less throughput than Spark streaming, Java based
		- does both streaming and batch
		- but kinesis data analytics is based on Flink and is SQL based (streaming analytics)
		- https://tech.dream11.in/blog/navigating-the-streamverse-a-technical-odyssey-into-advanced-stream-processing-at-dream11 
	- Spark Streaming (streaming ETL, streaming analytics)
 		- https://youtu.be/qlJmjkgHZ88?si=pJ2KTB6NJiUExSzP
![streaming](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/47fa425d-04f7-445c-839e-1f00a4c0edf3)
	- Kafka (message bus)
		- Ksqldb: SQL on kafka streams (streaming ETL, streaming analytics)
		- Faust: python on kafka streams (streaming ETL, streaming analytics)
		- lower cost: redpanda.com
		- more scalable: Pulsar
	- Storm
		- lowest latency, but low level primitives (map reduce), no higher level abstractions
	- Trident
		- higher level abstractions on Storm
	- Protobuf: high performance serialized data
	- Avro: row based storage format
		- column based: Parquet, ORC, Delta Live Tables, Iceberg
        - https://blog.det.life/choosing-the-right-big-data-file-format-avro-vs-parquet-vs-orc-c868ffbe5a4e
	- https://streamingdata.substack.com/p/data-platforms-in-2030
- Spark vs Flink
![Screenshot_20230830-203252_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7ccebc36-fd78-4159-8de5-f8bc2f76890e)
![Screenshot_20230830-204839_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4d92304e-ac6f-495f-821a-629cfd45f379)
![Screenshot_20230830-203604_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/561c3812-8edb-4fe3-94c2-e1ba64d06b09)
- Storm / Trident / Samza / Spark Streaming
	- https://youtu.be/ZWez6hOpirY?si=Jn9nlbncR9gPr3Yl
 	- https://youtube.com/watch?v=6ZaMfEc9kbI&si=FQxLWXeHZTdqDWlp
![Screenshot_20230830-204959_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3b5afbd6-26bb-456b-b226-236dbb4ec91e)
![Screenshot_20230830-205203_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dfc0b4a1-df7e-4cbe-bec8-99982f563119)
![Screenshot_20230830-205253_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9c7cd265-750b-4fea-9998-227c7a985323)
![Screenshot_20230830-205418_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2c72e73e-5d73-427f-9e22-194dc2b32517)
![Screenshot_20230830-205540_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/633487c4-143a-4863-a433-cd5b130f8d48)
![Screenshot_20230830-205602_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1c4c4648-6484-43a9-b4e7-8d41da713334)
![Screenshot_20230830-205644_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75219c18-d24c-439f-a4bd-3aa6414a9d70)
![Screenshot_20230830-210142_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2ec8cf33-48ab-42ee-bf86-2825d496e180)
![Screenshot_20230830-192134_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/abf57c17-d04d-490b-b2eb-a8d1c18ca62b)
- https://www.youtube.com/watch?v=5lFXI5333mg
![Screenshot_20240114-102804_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6b20e0f4-9716-4296-9fde-04f08c72572c)
- https://learn.glassflow.dev/blog/articles/choosing-between-a-streaming-database-and-a-stream-processing-framework-in-python
- Moirai: A Time Series Foundation Model for Universal Forecasting https://blog.salesforceairesearch.com/moirai/
- Apache Spark Vs. Apache Flink Vs. Apache Kafka Vs. Apache Storm! https://www.youtube.com/watch?v=V3Q3EkbEc_k

## Message Bus vs Real Time Stream Processing vs RT OLAP
- https://blog.dataengineer.io/p/how-to-choose-between-batch-micro
- 10% data engineers know RT
- RT SP / OLAP requires DE to be on-call
- https://betterprogramming.pub/start-your-stream-processing-journey-with-just-4-lines-of-code-5863573268b9
<img width="1920" alt="Screenshot 2024-06-07 at 2 04 28 PM (2)" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e645e520-6c01-4510-afbf-e2bb43676d9a">
<img width="1792" alt="Screenshot 2024-06-05 at 11 04 46 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/08a17246-daf2-47ea-8ba3-8ad679b5aa8b">
<img width="1792" alt="Screenshot 2024-06-05 at 11 22 05 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1fb5d390-bec2-4a3f-a11c-9b0567e78bc7">
<img width="1792" alt="Screenshot 2024-06-04 at 3 15 35 PM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d3252b0b-5941-4893-819e-1064d448de4c">

## Apache Flink
- https://rmoff.net/2023/09/29/learning-apache-flink-s01e01-where-do-i-start/
	- Decodable: managed Flink
	- DeltaStream : serverless Flink https://www.youtube.com/watch?v=tuMp-zIBFyg
![Screenshot_20240620-154503_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d6533311-8094-43e1-99af-530d175dc8bd)
- Flink + Kafka https://www.youtube.com/watch?v=EsndjcspRA8
- Flink tech details https://www.youtube.com/watch?v=vZFpPMwQ1po
	- Flink older tech
	- Flink join postgres and kafka topic too complicated, requires pairs programming analyst and data engineer
<img width="1792" alt="Screenshot 2024-06-05 at 8 26 14 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/532bb0b1-6d56-4f98-8887-143e2cae951c">
- Flink used a lot more in China https://www.youtube.com/watch?v=ZsWa6XiBc-U&t=3840s

## Bytewax
- Apache Beam
	- https://engineering.linkedin.com/blog/2023/revolutionizing-real-time-streaming-processing--4-trillion-event
- Bytewax like python version of Apache Beam, is a stream processing framework https://www.youtube.com/watch?v=PmJnIe9Apc4
![Screenshot_20240621-160915_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/66b3a9b5-a8f4-4296-b39c-1b37b4857dfb)
![Screenshot_20240621-161106_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/51c77a4d-715d-4a0c-a784-113debeaafa7)
![Screenshot_20240621-161117_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/25da7399-f50e-466c-a559-a1f74d216681)
![Screenshot_20240621-161128_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6f312f28-53de-4685-bfab-a8cdd40118d6)

## RisingWave
- https://betterprogramming.pub/start-your-stream-processing-journey-with-just-4-lines-of-code-5863573268b9
- RisingWave tech details https://www.youtube.com/watch?v=6cKxLk6bpyY
	- RisingWave newer tech: stream processing (streaming ETL, streaming analytics) + streaming database
	- RisingWave, etc. Easier, more modern, is also a serving database
- RisingWave vs Flink https://www.slideshare.net/slideshow/battle-of-the-stream-processing-titans-flink-versus-risingwave-258323520/258323520
- RisingWave intro https://www.youtube.com/watch?v=oTL6DbfkBB0
![Screenshot_20240703-180904_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ae1f3fec-d590-4b9a-9ecf-42b0cacdd8d7)
![Screenshot_20240703-180949_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/19e56ab6-6802-401a-88ed-e0b006e88c20)
![Screenshot_20240703-181004_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f5e3859b-74b8-4870-88f4-3d6091962c60)
![Screenshot_20240703-181005_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b00eecba-185d-4024-b114-031002d8825f)
![Screenshot_20240703-181025_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/337b94d3-5f95-4841-811f-37de2f027b4f)
![Screenshot_20240703-181056_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75367f50-ac13-499d-af71-15818c4f1b4b)
![Screenshot_20240703-181138_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/98837b32-1a43-4922-9117-a52c4e4c8881)
![Screenshot_20240703-181147_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2d02c904-be3c-4af5-8044-7e23ec069ed3)
![Screenshot_20240703-181149_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7eb4fb73-84f7-4709-8803-da4fb5cb7fb2)
![Screenshot_20240703-181222_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/fead1056-1572-436b-b68f-beaeb174c015)
![Screenshot_20240703-181243_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/24acdf0e-512b-419d-b699-77fa53789889)
![Screenshot_20240703-181247_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7a8bdd5f-e6f7-4ae8-b9ab-ba3876554189)
![Screenshot_20240703-181258_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9c70e6ca-339e-46bd-b4fa-2020fe1e4667)
![Screenshot_20240703-181320_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a33ab82b-fc6a-467b-b49a-5206cb85a4d4)
![Screenshot_20240703-181333_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/74f19cad-926c-48d8-b68e-faa4199f5329)
![Screenshot_20240703-181346_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/883280d6-d816-4a8b-82ac-c74ba681a384)
![Screenshot_20240703-181359_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/768fad1e-61eb-4299-b944-430f31eb55cb)
![Screenshot_20240703-181411_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/26f260bd-a67c-480c-a965-71b7631bec0d)
![Screenshot_20240703-181417_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5de6b77a-4762-486a-bcde-7952df7d8a5c)
![Screenshot_20240703-181447_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2e3ceea3-09fc-4d22-9c12-566c9d2d6ccd)
![Screenshot_20240703-181458_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6d8a7a7c-903b-47a8-a223-b8ebfba3e71e)
![Screenshot_20240703-181509_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/79e128f7-cd77-499d-9481-b30632192365)
![Screenshot_20240703-181538_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/82a5e4fc-2707-43c5-b171-1666d72e8b3d)
- RisingWave -> StarRocks / CelerData https://www.youtube.com/watch?v=c1pcWcSkZzU
![Screenshot_20240621-164305_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3b77f926-fcac-4d8e-aae0-4b68a11217ee)
![Screenshot_20240621-164329_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ef786125-16d2-4e70-baf7-9c14498bedc4)
![Screenshot_20240621-164349_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b6c56895-13b5-48c1-88b7-106c00a858d8)
![Screenshot_20240621-164431_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/17eca03d-9f16-4a11-aff9-7ec3d1bcb644)
![Screenshot_20240621-164449_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5ea815d7-5df7-4487-99cf-b91d4a7fde3c)
![Screenshot_20240621-164502_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a8124b78-3695-4b88-b40f-71009c8822a7)
![Screenshot_20240621-164514_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a493579a-6e6d-490c-8422-b5f2c77c2d37)
![Screenshot_20240621-164529_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2a355ced-39e3-4b7c-b812-78b853db3e51)

## Quix
- Quix python streaming dataframes https://www.youtube.com/live/cjhBCLRa48Q
![Screenshot_20240628-165536_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d6673edc-0abf-4499-9296-e1350942db96)
![Screenshot_20240628-165548_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/228aae5b-b049-42f4-bb57-c8d9cd3e995f)
![Screenshot_20240628-165650_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2c041679-61dd-4fbb-82c9-1cf6d7fabf18)
![Screenshot_20240628-165658_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ec5e3756-ad63-4ce8-8084-b237eed81413)
![Screenshot_20240628-165807_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2b4627bd-38e1-4374-b687-fab2d775e5d1)
![Screenshot_20240628-165910_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/92a0fb7b-9bbe-4c12-bd7b-8a12453ffde8)
![Screenshot_20240628-165915_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8ed2172d-901f-40da-9086-fa4fde4b611d)
![Screenshot_20240628-165928_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8633ebcb-77d0-4cbc-9cf4-78cff94c744f)
