# Stream Processing

## Stream processing frameworks: streaming ETL, streaming analytics, streaming databases

Snowplow
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
	- ![Screenshot_20230830-203252_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/7ccebc36-fd78-4159-8de5-f8bc2f76890e)

	- ![Screenshot_20230830-204839_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4d92304e-ac6f-495f-821a-629cfd45f379)

	- ![Screenshot_20230830-203604_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/561c3812-8edb-4fe3-94c2-e1ba64d06b09)

- Storm / Trident / Samza / Spark Streaming
	- https://youtu.be/ZWez6hOpirY?si=Jn9nlbncR9gPr3Yl
 	- https://youtube.com/watch?v=6ZaMfEc9kbI&si=FQxLWXeHZTdqDWlp
	- ![Screenshot_20230830-204959_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3b5afbd6-26bb-456b-b226-236dbb4ec91e)

	- ![Screenshot_20230830-205203_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/dfc0b4a1-df7e-4cbe-bec8-99982f563119)

	- ![Screenshot_20230830-205253_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9c7cd265-750b-4fea-9998-227c7a985323)

	- ![Screenshot_20230830-205418_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2c72e73e-5d73-427f-9e22-194dc2b32517)

	- ![Screenshot_20230830-205540_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/633487c4-143a-4863-a433-cd5b130f8d48)

	- ![Screenshot_20230830-205602_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1c4c4648-6484-43a9-b4e7-8d41da713334)

	- ![Screenshot_20230830-205644_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/75219c18-d24c-439f-a4bd-3aa6414a9d70)

	- ![Screenshot_20230830-210142_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2ec8cf33-48ab-42ee-bf86-2825d496e180)

	- ![Screenshot_20230830-192134_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/abf57c17-d04d-490b-b2eb-a8d1c18ca62b)

- Apache Beam
	- https://engineering.linkedin.com/blog/2023/revolutionizing-real-time-streaming-processing--4-trillion-event
- https://www.youtube.com/watch?v=5lFXI5333mg
![Screenshot_20240114-102804_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6b20e0f4-9716-4296-9fde-04f08c72572c)
- https://learn.glassflow.dev/blog/articles/choosing-between-a-streaming-database-and-a-stream-processing-framework-in-python
- Moirai: A Time Series Foundation Model for Universal Forecasting https://blog.salesforceairesearch.com/moirai/
- Apache Spark Vs. Apache Flink Vs. Apache Kafka Vs. Apache Storm! https://www.youtube.com/watch?v=V3Q3EkbEc_k

## Message Bus vs Real Time Stream Processing vs RT OLAP

https://blog.dataengineer.io/p/how-to-choose-between-batch-micro
- 10% data engineers know RT
- RT SP / OLAP requires DE to be on-call

https://betterprogramming.pub/start-your-stream-processing-journey-with-just-4-lines-of-code-5863573268b9

<img width="1920" alt="Screenshot 2024-06-07 at 2 04 28 PM (2)" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/e645e520-6c01-4510-afbf-e2bb43676d9a">
<img width="1792" alt="Screenshot 2024-06-05 at 11 04 46 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/08a17246-daf2-47ea-8ba3-8ad679b5aa8b">
<img width="1792" alt="Screenshot 2024-06-05 at 11 22 05 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1fb5d390-bec2-4a3f-a11c-9b0567e78bc7">
<img width="1792" alt="Screenshot 2024-06-04 at 3 15 35 PM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/d3252b0b-5941-4893-819e-1064d448de4c">

RT Stream Processing
- Flink tech details https://www.youtube.com/watch?v=vZFpPMwQ1po
	- Flink older tech
	- Flink join postgres and kafka topic too complicated, requires pairs programming analyst and data engineer
<img width="1792" alt="Screenshot 2024-06-05 at 8 26 14 AM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/532bb0b1-6d56-4f98-8887-143e2cae951c">

## RisingWave
- RisingWave tech details https://www.youtube.com/watch?v=6cKxLk6bpyY
	- RisingWave newer tech
	- RisingWave, etc. Easier, more modern, is also a serving database 