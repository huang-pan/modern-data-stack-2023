# Real Time Data Warehouses

## RT OLAP

## Rockset

- Rockset replicates AWS DynamoDB tables https://www.youtube.com/watch?v=JGIzdFHZVXs
	- Rockset search and analytics DB https://www.youtube.com/watch?v=xGaUJTHuehQ
 	- Essentially makes a low latency copy of data source using 
		- converged indicies: row based index, column based index, inverted (document) index
- Rockset product overview https://www.youtube.com/watch?v=4nEQpISidw4
![Screenshot_20240620-104355_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0baab291-2d40-4db4-9efc-8ed3b2820df8)
- Rockset architecture https://www.youtube.com/watch?v=msW8nh5TTwQ
![Screenshot_20240620-115528_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8cd2eb60-95ca-4e0d-950d-0bd92ec6f27d)
![Screenshot_20240620-115550_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/4cb73583-4b99-475a-9efe-c48a65875721)


## ClickHouse
- ClickHouse
	- https://www.youtube.com/watch?v=HRh5setqGCU 
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

## Firebolt

## Materialize

## Tiny Bird + Snowflake
