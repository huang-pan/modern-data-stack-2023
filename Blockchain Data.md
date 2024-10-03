# Blockchain Data

## Coinbase Lakehouse Architecture
- https://www.youtube.com/watch?v=3Z9jSCaHnYg
	- Coinbase open lakehouse arch: S3, iceberg
 	- https://www.youtube.com/watch?v=3Z9jSCaHnYg&t=869s
	- starrocks / celerdata RT OLAP, duckdb
	- puppygraph: graphDB on iceberg
![Screenshot_20240618-160542_YouTube](https://github.com/user-attachments/assets/0f3510e5-cdf0-4718-aa8f-bcaea6715695)

## Real Time blockchain data
- https://www.meetup.com/streaming-stories/events/297191788
- Crypto Fintech meets Real Time data https://www.youtube.com/watch?v=LftHdHUVk6s 
- Rising Wave, built on rust
	- Yingjun Wu, Founder and CEO
- Goldsky https://goldsky.com/
	- Yaroslav Tkachenko
	- crypto data, live streamed
	- flink, red panda, clickhouse
	- used by OP labs
- alchemy https://www.alchemy.com/ 
	- Odin Wang
	- web3 infrastructure
	- read / write to iceberg using flink
	- watch for node version upgrades for data quality
	- crypto node providers keep costs low: 1 GB ethernet
- superchain network https://www.superchain.network/ 
	- James Corbett
	- RT blockchain data, decentralized
	- for on chain analytics, trading systems
	- < 10 ms
	- buiding decentralized streaming system
	- connet output to kafka for customers
	- SQL interface, not streaming
	- data fusion, polars, arrow, not streaming
	- rising wave: streaming SQL
- RT data
	- < 10 seconds
	- not trading, IoT
	- block created every 12 seconds
	- spark not the best for streaming
	- stateful streaming hard to manage / do
		- long running system
		- how to do watermarks with blokchain data? use block number
			- flink: watermark is timestamp
	- batch job failure
		- recovery takes some time
	- stream job failure
		- recovery is faster
	- dynamic scaling
		- flink dynamic scaling not that great
	- bull run spiky workloads, Binance smart chain high TPS stopped
	- spark, flink, kafka can absorb spiky blockchain traffic
- red panda vs apache kafka
	- red panda c++, uses kakfa api protocol, everything works combatibility, cheaper than kafka
	- flink
	- cloud offering better for smaller teams
- flink
	- best features overall
	- java streaming apps
- RT OLAP
	- microbatching
	- mostly SQL based

## Blockchain Indexers

### SubQuery
- Open source blockchain indexer https://www.youtube.com/watch?v=7YGR6pBJ0wI 
![thumbnail (1)](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/56d66a50-a1aa-495d-997e-673d862d6fe5)

### HyperIndex / HyperSync
- Modern Blockchain Indexing: Syncing Millions Of Events In Seconds https://www.youtube.com/watch?v=ihXPtsLmbuY
- ![Screenshot_20240611-172718_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/8076d865-713a-4436-bd26-eefd15f9db7b)
- ![Screenshot_20240611-172642_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/88b2b0de-1314-4f62-ad3d-05ef736a5e79)
- ![Screenshot_20240611-172548_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/1f61c013-6a1e-4f7b-a3b3-ac29a47932cc)
- ![Screenshot_20240611-172445_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0d59d71d-4ffe-4faf-adfd-7f3018ea7b97)

### The Indexing Company
- https://www.youtube.com/watch?v=slFvVOAzgw8
- https://www.indexing.co/
	- https://console.indexing.co/features
	- they use TimescaleDB
- https://www.linkedin.com/company/indexing-co/people/ 7 people
![Screenshot_20240627-130646_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/c4d81fca-adbe-44b1-9abe-4991a4617999)
![Screenshot_20240627-130709_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/f7c2adfd-520c-4d6e-939c-3256a3a29088)
![Screenshot_20240627-130720_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/849a39a6-1fe9-41c0-9f10-be959b3adabb)

## Blockchain AI

### Blockchain and AI
- JPMorgan thought leadership https://www.youtube.com/watch?v=F5GzAkn_nJc
- https://github.com/huang-pan/modern-data-stack-2023/blob/main/Federated%20Learning.md#a-verifiable-federated-learning-scheme-based-on-zksnarks-and-blockchain
- Explore zkML with Nethermind https://www.youtube.com/watch?v=Ofxy2oSioCg
- Dfinity https://www.youtube.com/watch?v=MzvsST3rzjc
![Screenshot_20240824-205635_YouTube](https://github.com/user-attachments/assets/446c2338-0975-4f39-9a24-52f3667e7c49)
![Screenshot_20240824-205647_YouTube](https://github.com/user-attachments/assets/40bc59ca-dbe7-4fb3-ab50-f62b4837bba6)
![Screenshot_20240824-205710_YouTube](https://github.com/user-attachments/assets/bc6da6ae-f81f-4666-a6c9-e22303e647c8)
![Screenshot_20240824-205724_YouTube](https://github.com/user-attachments/assets/841cf0c0-5129-43db-a27b-160df4b38912)
![Screenshot_20240824-205732_YouTube](https://github.com/user-attachments/assets/6b47d487-e400-4ffa-b14a-97c2592d6bec)
![Screenshot_20240824-205753_YouTube](https://github.com/user-attachments/assets/3aa548de-09df-4490-99c1-47ecc5741745)
![Screenshot_20240824-205801_YouTube](https://github.com/user-attachments/assets/ab2c0980-7236-4e13-94eb-1b6c69a37d5a)

### Decentralized Storage
- https://www.youtube.com/watch?v=S3wkcIP7mEk 2024
- ![Screenshot_20240611-173226_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9596525e-aaae-4fd3-99b0-5182c532fe33)

### Decentralized Machine Learning
- https://www.youtube.com/watch?v=SyAdBo6vRAA 2024 flock.io decentralized training
- ![Screenshot_20240611-182845_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0a38d1eb-1b42-4ec5-a0b8-caa4058ffd96)

### Oasis Labs
- https://www.oasislabs.com/
	- PrivateSQL: A Privacy Layer for Data Collaboration and Analytics
	- Dawn Song is the founder of Oasis Labs and a professor in the Department of Electrical Engineering and Computer Science at the University of California at Berkeley.
	- Oasis Labs, which raised $45million from investors that include a16z crypto, Binance Labs, DCVC, Electric Capital, and Pantera in 2018
	- https://www.youtube.com/@OasisFoundation/videos lots going on at Oasis Labs
- https://www.youtube.com/watch?v=j8VQxfB1qXI
![Screenshot_20240819-201756_YouTube](https://github.com/user-attachments/assets/5648d833-5740-4f2e-a96e-b5d2f5b9146e)
![Screenshot_20240819-201803_YouTube](https://github.com/user-attachments/assets/198fb0e5-2166-4b47-8a89-829381fb9fd2)
![Screenshot_20240802-163828_YouTube](https://github.com/user-attachments/assets/7bc78dfc-20c2-4b06-a8c0-6562b27c1eb5)
![Screenshot_20240802-163841_YouTube](https://github.com/user-attachments/assets/ff0461d6-d2a7-41d7-80d3-9df28004d839)
![Screenshot_20240802-163901_YouTube](https://github.com/user-attachments/assets/59c73705-1448-4662-98dd-e5f124b5bbc7)
![Screenshot_20240802-163904_YouTube](https://github.com/user-attachments/assets/0bd04e17-c78e-4c7d-bb06-8f4cceb7ab48)
![Screenshot_20240802-163930_YouTube](https://github.com/user-attachments/assets/4ac2163d-af1e-4981-b10d-91b4835130d0)
![Screenshot_20240802-163933_YouTube](https://github.com/user-attachments/assets/66163b87-29a7-4348-8599-00932396d85d)
![Screenshot_20240802-163937_YouTube](https://github.com/user-attachments/assets/5bd78255-d115-47bb-81b5-8d22aeb21cd3)
![Screenshot_20240802-163944_YouTube](https://github.com/user-attachments/assets/f37b94ea-9704-4961-842a-6fe14e8699b8)
![Screenshot_20240802-164016_YouTube](https://github.com/user-attachments/assets/f2e32890-016d-4d10-8acd-5e05cd6b3cb7)
![Screenshot_20240802-164022_YouTube](https://github.com/user-attachments/assets/24875237-b6bd-43eb-8cb0-76f4bd5f9632)

### Shadow
- https://blog.shadow.xyz/how-shadow-works/
- Shadow unlocks custom onchain data that you can pull into your subgraph or database for enhanced indexing and analytics, with just a few lines of code.

### Nexus zkVM
- https://www.youtube.com/watch?v=nyxPyrunu3s
![Screenshot_20240818-172247_YouTube](https://github.com/user-attachments/assets/e3d57100-cfee-43e9-a694-ae6e688f8158)
![Screenshot_20240818-172314_YouTube](https://github.com/user-attachments/assets/c4910e62-af13-472e-aba4-e5b4f7277b8c)
![Screenshot_20240818-172407_YouTube](https://github.com/user-attachments/assets/5e448efe-5edd-4040-9827-5a1aa6b24f4f)
![Screenshot_20240818-172433_YouTube](https://github.com/user-attachments/assets/8c0ad9cb-9488-4117-bbd1-7aec3ae18a15)
![Screenshot_20240818-172438_YouTube](https://github.com/user-attachments/assets/c959c3b0-c330-47cc-b675-fd77f6c7df6a)
![Screenshot_20240818-172513_YouTube](https://github.com/user-attachments/assets/6fff710a-663a-4d7d-9bbe-1b71fd344ac4)

### Analyzing Costs of ZK Rollups
- https://www.youtube.com/watch?v=hETChbrP_BU
![Screenshot_20240729-100050_YouTube](https://github.com/user-attachments/assets/0c98f57e-11a0-4269-a42e-fa884b76b141)
![Screenshot_20240729-100109_YouTube](https://github.com/user-attachments/assets/4650fb42-6c73-4f39-b3de-4d8878d56f49)
![Screenshot_20240729-100126_YouTube](https://github.com/user-attachments/assets/0196d5a3-ef6e-4cd2-9927-1fc84e9f5c55)
![Screenshot_20240729-100211_YouTube](https://github.com/user-attachments/assets/aa2bab24-eb08-458b-bf6a-ee3ea8a55042)

## Misc
- Karpatkey On chain treasury management  https://www.youtube.com/watch?v=biaINiiaskQ
- The Future of Layer 2 Blockchains https://www.youtube.com/watch?v=1w3qk4ZGjeA
	- Xvm program in multiple languages instead of evm
 	- IVC inter vm communication protocol 
- Architecture of Scalable Blockchain Applications https://www.youtube.com/watch?v=eqLrTjuBs2g
	- BSV, 1m Transaction per second
- Glider: A new generation of blockchain tooling https://www.youtube.com/watch?v=pstplea5UYA
![Screenshot_20240729-093010_YouTube](https://github.com/user-attachments/assets/0b73b0e6-db2d-498e-acce-bc961b974cd0)

## Notes
- European DiD https://www.youtube.com/watch?v=ynNOCK61Lzw 
- 
- See blockchain university notes and lectures
- https://github.com/hyperledger/blockchain-explorer
- https://github.com/blockchain/?q=kotlin&type=&language=
- https://github.com/smartcontractkit
- 
- BTC https://github.com/bitcoinbook/bitcoinbook by Aantonop
	- Bitcoin core: stores blockchain on disk
	- Sha256 hash function: used by bitcoin
	- Nonce: number used once, increment
	- P2P
		- gossip protocol
	- BTC blocks store merkle trees of transactions
		- block size limits to ? MB?
	- transactions: input / output addresses
		- event based blockchain --> like event source microservices --> create state from events
		- transaction fees
	- mempool with UTXOs unspent transactions
	- miners pay themselves from coinbase
		- difficulty scaling periods
	- public + private key = transaction signature
		- Bitcoin uses Elliptic Curve Cryptography (ECC), ECC provides use of smaller sized keys than non-ECC techniques
	- Bitcoin scripting: like assembly language for CPUs, but for bitcoin
	- Elasticsearch: 30 GB BTC blockchain to 220 GB elasticsearch DB
- ETH
	- blockchain: Data structures are stored in Merkle Patricia tries (read this and this), usually inside a LevelDBstore (fast key value database)
	- https://medium.com/validitylabs/how-to-interact-with-the-ethereum-blockchain-and-create-a-database-with-python-and-sql-3dcbd579b3c0
		- get data from local node or hosted node (Infura)
	- unlike BTC, ETH has accounts that store account values
		- unifying utxo blockchains with account based blockchains (paper) https://eprint.iacr.org/2018/262.pdf 
	- Solidity programming language
	- Mix desktop IDE --> Remix online IDE
- Block data from node
	- https://bitcoindev.network/bitcoin-analytics-using-google-bigquery/
		- The bitcoin core client software currently stores various bits of data as on disk which has been optimised for the running and execution when hosting a bitcoin node. The structure in which this is data is stored however is in a normalised form and optimised for the running of the node, not for reporting purposes.
		- Although there are many ways in which we can extract and report on this data, this tutorial we will be looking into Google's denormalised data set which is frequently updated and has been optimised for reporting.
- GCP
	- Types of managed database services https://blog.yugabyte.com/new-to-google-cloud-databases-5-areas-of-confusion-that-you-better-be-aware-of/
		- Need for horizontal write scalability either in the same region or across multiple regions is the single driver for choosing Cloud Spanner over Cloud SQL. 
		- pick BigTable for single-region analytics use cases and Spanner for multi-region operational use cases.
	- https://cloud.google.com/bigtable
		- Bigquery to bigtable or Spanner using google dataflow https://cloud.google.com/dataflow
	- Bigquery https://cloud.google.com/solutions/bigquery-data-warehouse
		- How to guides https://cloud.google.com/bigquery/docs/how-to
			- automatically caches queries into temp tables https://cloud.google.com/bigquery/docs/cached-results
		- Project.dataset.table
		- monitoring https://cloud.google.com/bigquery/docs/monitoring
		- Designing schema: Follow these general guidelines to design the optimal schema for BigQuery:
			- Denormalize a dimension table that is larger than 10 gigabytes, unless you see strong evidence that data manipulation,  UPDATE and DELETE operation, costs outweigh the benefits of optimal queries.
			- Keep a dimension table that is smaller than 10 gigabytes normalized, unless the table rarely goes through UPDATEand DELETE operations.
			- Take full advantage of nested and repeated fields in denormalized tables.
		- BigQuery is essentially an analytical engine. It supports DML actions, but it isn't meant to be used as an online transaction processing (OLTP) store.
		- To speed up queries, avoid joins, create flattened tables (searchable columns)
		- BigQuery supports partitioning tables by date.
		- Has section on how to handle table schema updates, slowly changing dimension
		- Query optimization: Each time BigQuery executes a query, it executes a full-column scan. BigQuery doesn't use or support indexes. Because BigQuery performance and query costs are based on the amount of data scanned during a query, design your queries so that they reference only the columns that are relevant to the query. When using date-partitioned tables, ensure only the relevant partitions are scanned. You can achieve this by using partition filters based on PARTITIONTIME or PARTITIONDATE.
	- bigquery BI engine https://cloud.google.com/bi-engine/docs/introduction
		- BigQuery BI Engine is a fast, in-memory analysis service. By using BI Engine you can analyze data stored in BigQuery with sub-second query response time and with high concurrency.
		- only works with Google Data Studio
- Blockchain ETL
	- https://github.com/blockchain-etl
		- has Airflow DAGs, use with Cloud Composer
- Public blockchain datasets
	- https://cloud.google.com/blog/products/data-analytics/introducing-six-new-cryptocurrencies-in-bigquery-public-datasets-and-how-to-analyze-them?fbclid=IwAR1l8tsW8r5bXbyA7M7pz6yYXbUiGPA7np0czQxowN_whlBFgbACoXId8WU
		- THIS IS HOW GOOGLE STRUCTURES BLOCKCHAIN DATASETS!!!
			- standardized double entry booking system for many crypto blockchains
			- Bitcoin-like datasets (Bitcoin, Bitcoin Cash, Dash, Dogecoin, Litecoin and Zcash) together because they all have similar implementations, i.e., their source code is derived from Bitcoin’s. 
			- Similarly, we’re also releasing the Ethereum Classic dataset alongside the previously published Ethereum dataset, and Ethereum Classic is also using the same common schema.
		- A unified data ingest architecture
			- All datasets update every 24 hours via a common codebase, the Blockchain ETLingestion framework (built with Cloud Composer, previously described here), to accommodate a variety of Bitcoin-like cryptocurrencies. While this means higher latency for loading Bitcoin blocks into BigQuery, it also means that: We are able to ingest additional BigQuery datasets with less effort, meaning additional datasets can be onboarded more quickly in the future.
			- We can implement a low-latency loading solution once that can be used to enable real-time streaming transactions for all blockchains.
		- Unified schema and views
			- Since we provided the original Bitcoin dataset last year, we’ve learned how users want to access data, and restructured the dataset accordingly. Some of these changes address performance and convenience concerns, yielding faster and lower cost queries (commonly accessed nested data are denormalized; each table is partitioned by time).
		- Address classification
			- Blockchain transaction history can be aggregated by address and used to analyze user behavior. To motivate further exploration, we present a simple classifier that can detect Bitcoin mining pools.
		- google public dataset bigquery-public-data.crypto_bitcoin.transactions 
			- the language in the BigQuery table is a bit confusing- I added some more context in italics:
				- sender: input.addresses: Addresses which own the spent output (prior to transaction being mined)
				- receiver: output.addresses: Addresses which own this output (after the transaction is mined)
				- since the input addresses own the output prior to the transaction being mined, we label them as senders.  
				- similarly since the output addresses receive the output after the transaction is mined we label them as receivers. this helpful when unifying utxo blockchains with account based blockchains (paper) https://eprint.iacr.org/2018/262.pdf
			- in bigquery-public-data.crypto_bitcoin.transactions , transaction table represents arrows between transaction blocks
	- https://cloud.google.com/blog/products/gcp/bitcoin-in-bigquery-blockchain-analytics-on-public-data
		- dataset updates every 10 minutes.
		- biqquery UNNEST https://cloud.google.com/bigquery/docs/reference/standard-sql/arrays
	- https://bitcoindev.network/bitcoin-analytics-using-google-bigquery/
		- The bitcoin core client software currently stores various bits of data as on disk which has been optimised for the running and execution when hosting a bitcoin node. The structure in which this is data is stored however is in a normalised form and optimised for the running of the node, not for reporting purposes.
		- Although there are many ways in which we can extract and report on this data, this tutorial we will be looking into Google's denormalised data set which is frequently updated and has been optimised for reporting.
	- https://medium.com/google-cloud/analysing-1-2m-mainnet-contracts-in-20-seconds-using-eveem-and-bigquery-f69b6d66c7b2
- blockchain explorer
	- https://www.softwaretestinghelp.com/blockchain-explorer-tutorial/
		- Main use of explorer is for information verification
		- Above article shows how blockchain explorers work
			- Blockchain explorers work by using a database that holds all blockchain in a searchable format and tables. An explorer will, therefore, work with a node interface to first extract all the data in a given blockchain. Once it derives the data, it then stores it in easily searchable tables.
			- It will gather the latest transactions and blocks and arrange them according to the defined searchable categories – for instance, wallet addresses transaction IDs, rich lists, balances, etc
		- Blockchain explorers are the Google of cryptocurrencies and blockchain. They allow users to access different details related to transactions on specific wallet addresses and blockchains including amount transacted, sources and destination of funds, and status of the transactions.
		- They can be used to extract virtually any data related to transactions, wallets, and blockchains including rich lists and hidden messages.
		- #1) Explore the transaction history of any wallet address: This allows us to audit any wallet address and improves transparency on a blockchain.
		- #2) Explore receiving addresses and change addresses: In addition to the transaction receiving address, you can see the change address, which is an output that returns crypto to the spender to prevent too much of the input value from going to the transaction fees. This also improves the transparency of transactions.
		- #3) Explore the largest transaction of the day: This is supported by some explorers.
		- #4) Explore Mempool status: This allows us to explore the unconfirmed transactions on a blockchain including their details.
		- #5) Explore double-spend incidents: Some explorers support the discovery of how many double-spend transactions are taking place in a blockchain.
		- #6) Explore orphaned and stale blocks: These are blocks that are not attached to the longest blockchain even after mining and their parent blockchain is unknown. Stale blocks are those whose parents are known but still aren’t attached to the longest known chain. Some explorers allow us to see how many of these blocks were realized in a blockchain.
		- #7) Explore the pool or person who found or mined a particular block: Different individuals and mining pools (groups that combine their computing resources to mine crypto) compete to mine blocks in any given blockchain and explorers allow us to find who successfully mined a given block defined by its height.
		- #8) Explore genesis blocks: You can find the block that was mined first on a given chain, by whom as well as its other data.
		- #9) Allows users to see fees of transactions, blockchain difficulty, hash rate, and other data.
	- https://thegraph.com
		- ETH Graph DB / GraphQL blockchain explorer
	- https://medium.com/alethio/the-future-of-alethio-c4fd511e4c03  Under the Codefi Data, the following APIs are available:
		- Fundamental API — Query low-level blockchain data and state as well as token balances, transactions and DeFi charts. This API is an updated version of the former Alethio API. Read the documentation here
		- DeFi Graph API — Query current and historical metrics across all lending protocols including rates, locked value, originations, collateralization ratios and more. Read the documentation here
		- DeFi Score API — Query DeFi Score and associated risk metrics on all the DeFi Lending Protocols. Used for display in your wallet/dapp, research, or media content. Read the documentation here
- Smart contract analyzer
	- ETH https://medium.com/google-cloud/analysing-1-2m-mainnet-contracts-in-20-seconds-using-eveem-and-bigquery-f69b6d66c7b2
- Onchain Capital allocation: DAOs, decentralized funds, etc. https://www.youtube.com/watch?v=tP_DXc0SkdQ
