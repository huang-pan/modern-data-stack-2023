# Notebooks, Misc Data Tools

## Notebooks

- Hex
    - [https://www.linkedin.com/company/hex\-technologies/people/](https://www.linkedin.com/company/hex-technologies/people/) 91 people
- Deepnote
    - [https://www.linkedin.com/company/deepnote/people/](https://www.linkedin.com/company/deepnote/people/) 36 people
- Noteable: shut down 2024
    - [https://www.linkedin.com/company/noteable\-io/people/](https://www.linkedin.com/company/noteable-io/people/) 27 people

## ETL / reverse ETL tools
- Airbyte 101 https://www.youtube.com/live/2A50P2TqtUk
- https://www.linkedin.com/posts/oleg-agapov_lets-discuss-the-pricing-of-cloud-data-activity-7212918396848414720-wZJ5/
Let’s start with obvious and super popular choices:
☑️ Airbyte Cloud – $100 per 10GB synced, consumption-based.
☑️ Stitch - $180 per month, consumption-based.
☑️ Fivetran wants $2.6K for 20M rows on a Starter plan. Consumption-based. Wow 🤯!
Now let’s look at the alternatives suggested to me:
☑️ DoubleCloud – about $140/month for 20M rows. Consumption-based.
☑️ Estuary – about $200 per month for 8GB of data. Consumption-based.
☑️ Portable - $290/month, one source, no volume limits. Commit.
☑️ Hevo – $400 per month for 20M rows. Commit.
☑️ Omnata – about $420/month, supposedly no rows limits. Commit.
☑️ Polytomic - starts from $500/month, no idea about limits. Commit.
☑️ Streamkap – $6K per year ($500/month) for 100M rows. Commit.
☑️ CDATA - $9K per year ($750 per month), 100M rows/month. Commit.
☑️ Matilion - $2K/month for 20M batch rows, $5.4K/month for 14M CDC rows. Commit with additional consumption-based credits.

- https://www.linkedin.com/posts/jeff-skoldberg-141812111_this-story-is-becoming-more-and-more-common-activity-7211422236086337536-J9Q7/
    - If you are spending too much on Fivetran or frustrated with Airbyte, I believe Flow by Estuary offers best-in-class stability and simplicity while providing two advantages over the competition:
        1️⃣ Real time ingestion
        2️⃣ Lower cost of ownership
- https://www.linkedin.com/posts/rdmeyersf_bigquery-apacheiceberg-streamingetl-activity-7212123192855781376-lxPe/
    - Real-time analytics with Iceberg is here! Estuary now supports sub-second streaming at serious scale to Iceberg. Let the Iceberg benchmarks begin!
    - By real-time analytics I mean sub-second query and loading for Iceberg.
    - We’ve seen benchmarks showing that with DuckDB/Motherduck or Starburst that you can query a Terabyte in Iceberg with second-level performance (more info in the comments.)
    - With Estuary, you can now also load Iceberg with sub-second latency at massive scale!
    - Flow streams with <100ms latency to Iceberg and scales out horizontally with Iceberg to stream at any scale you need.
    - We’re not talking your typical ELT scale. One Estuary data pipeline already streams 7+ GB/sec peak in production with sub-second latency. That adds up to a Terabyte in a little over 2 minutes and 200+ Petabytes a year.

## Dataset marketplace

- https://datapm.io/
    - Example coinbase trading pair dataset https://www.youtube.com/live/_YltwetuPK0

## Latest Data Tools

- Cool channel doing demos of the latest data tools: [https://www.youtube.com/@demohub/videos](https://www.youtube.com/@demohub/videos)
- Jupyter AI https://www.marktechpost.com/2023/08/06/meet-jupyter-ai-a-new-open-source-project-that-brings-generative-artificial-intelligence-to-jupyter-notebooks-with-magic-commands-and-a-chat-interface/
- ***Data Tooling cost analysis***, etc.: https://medium.com/@hugolu87

## Netflix Data Engineering
- Netflix Data Engineering tech stack https://www.youtube.com/watch?v=QxaOlmv79ls
- data processing patterns https://www.youtube.com/watch?v=vuyjK2TFZNk
![Screenshot_20240620-185544_YouTube](https://github.com/user-attachments/assets/693c9694-cbc5-4bec-b7ab-9ed63640a090)
