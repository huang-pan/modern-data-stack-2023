# Snowflake vs Databricks

![snowflake](https://github.com/user-attachments/assets/98d95dd8-78af-4029-9805-f174d1e29a56)

## Snowflake vs Databricks conferences
- 2024 https://www.youtube.com/watch?v=F1UJ6rS7GHU
- https://www.linkedin.com/posts/ethanaaron_after-a-month-of-conversations-about-databricks-activity-7205932220249690114-1e_J/
1. Databricks users think in terms of raw data in storage, not SQL tables. The word parquet has come up on every call I've had, and EVERY person I've spoken with is comfortable working with files and formats like Parquet. (Customers on Snowflake, BigQuery, etc. tend to be less technical on average)
2. Databricks has done a great job of educating users on the medallion architecture. Regardless of the technology you use, I highly recommend spending time thinking in terms of Bronze, Silver, Gold layers in your data architecture. Here's a great resource to learn more: https://lnkd.in/eXBRcghS
3. Databricks is more than just BI. Databricks customers want access to raw data in storage because they want to run different types of workloads on their data. BI and analytics is one use case, but teams are running ML pipelines, python scripts, and data science workloads on the same underlying data.
4. Databricks takes the concept of 'separation of compute and storage' to a whole different level. Although Snowflake pioneered the concept, most customers that use Databricks truly view data storage and compute as different parts of their tech stack. Data is stored in blob storage (S3, GCS, Azure blob), and Databricks is effectively just a compute layer that interfaces with external storage. That way their data is truly portable.
5. Databricks is going to be a great destination for Portable's 1300+ ELT connectors. Our team is actively building support for Databricks and other data lake and lakehouse architectures. We're already seeing a ton of demand for a no-code way to get data from applications into Databricks.
6. The Databricks platform is powerful, but also takes some additional knowledge to get started vs. a data warehouse. Warehouses work out of the box with nothing more than SQL and some setup configuration. Databricks has more concepts to learn, but once you learn them, the platform is extremely powerful.
7. Azure is a lot more common in the Databricks client base.
8. As much as I hear about a war between Snowflake vs. Databricks, I think we're still in the early stages. Both companies are trying to enter the other company's space from a technology perspective. But we're not there yet. They are each currently well positioned in different parts of the market, and their clients are using them in different ways.
- Snowflake vs Databricks Deep Dive https://www.youtube.com/watch?v=U1DgEbK6glw
![Screenshot_20240627-131430_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2d079021-e914-4274-a53c-cea0862c9b91)
![Screenshot_20240627-131454_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5b4607fc-4210-426f-bf7c-8be619f4d192)
