# Data Contracts

## Data Contracts

In its simplest form Data Contract is an agreement between Data Producers and Data Consumers on what the Data being produced should look like, what SLAs it should meet and the semantics of it.
Data Contract should hold the following non-exhaustive list of metadata:
- Schema of the Data being Produced.
- Schema Version - Data Sources evolve, Producers have to ensure that it is possible to detect and react to schema changes. Consumers should be able to process Data with the old Schema.
- SLA metadata - Quality: is it meant for Production use? How late can the data arrive? How many missing values could be expected for certain fields in a given time period?
- Semantics - what entity does a given Data Point represent. Semantics, similar to schema, can evolve over time.
- Lineage - Data Owners, Intended Consumers.

Some Purposes of Data Contracts:
- Ensure Quality of Data in the Downstream Systems.
- Prevent Data Processing Pipelines from unexpected outages.
- Enforce Ownership of produced data closer to where it was generated.
- Improve scalability of your Data Systems.
- Reduce intermediate Data Handover Layer.

![data_contract](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/ee07a579-af1a-48e2-a9f8-d192fe031848)

1. Schema changes are implemented in a git repository, once approved - they are pushed to the Applications generating the Data and a central Schema Registry.
2. Applications push generated Data to Kafka Topics. Separate Raw Data Topics for CDC streams and Direct emission.
3. A Flink Application(s) consumes Data from Raw Data streams and validates it against schemas in the Schema Registry.
4. Data that does not meet the contract is pushed to Dead Letter Topic.
5. Data that meets the contract is pushed to Validated Data Topic.
6. Applications that need Real Time Data consume it directly from Validated Data Topic or its derivatives.
7. Data from the Validated Data Topic is pushed to object storage for additional Validation.
8. On a schedule Data in the Object Storage is validated against additional SLAs and is pushed to the Data Warehouse to be Transformed and Modeled for Analytical purposes.
9. Consumers and Producers are alerted to any SLA breaches.
10. Data that was Invalidated in Real Time is consumed by Flink Applications that alert on invalid schemas. There could be a recovery Flink App with logic on how to fix invalidated Data.

## Data Quality

- https://blog.det.life/mastering-data-quality-10-essential-checks-with-real-world-examples-and-7-best-practices-fa303f2ae42b

## Technical Debt

10 categories of tech debt:
In order of prevalence…
1. Outstanding migrations
2. Missing or incomplete documentation
3. Poor test quality or coverage
4. Poorly designed code
5. Dead or unused code
6. Code that's not aligned to current standards
7. Lack of needed expertise on a team, resulting in code that's difficult to maintain
8. Problematic dependencies
9. Incomplete migrations or upgrades
10. Out-of-date release process
