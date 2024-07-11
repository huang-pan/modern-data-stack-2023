# Data Product, KPIs

## Running Data Teams

### Run a data team like a business
- https://www.linkedin.com/posts/ethanaaron_people-take-take-take-from-data-teams-activity-7184551839420325888-5W5K/
1. CEO best practice 👉 Have a board of advisors
- As a data team, you should find executives and business stakeholders you can talk to on a monthly or quarterly basis about how things are going, what's going well, and how you can improve.
2. Sales best practice 👉 Record your calls
- As a data team, you should be recording your video calls with stakeholders, so you can go back and find the exact things they were looking for. And quote them on how valuable it is.
3. Marketing best practice 👉 Stuff doesn't sell itself, you need to market it
- As a data team, it's common to focus on the technology and the deliverables. If you've spent any time with marketers, you'll realize that distribution channels and the narrative around why people should care about your deliverable is just as important (if not more important) than the actual deliverable. If you don't think about how to internally market your team and the your deliverables, start now.
4. Product best practice 👉 Ruthlessly say no to low-value stuff
- As a data team, you can't help every stakeholder, and you can't build every deliverable. And you shouldn't. Instead, think like a product manager and spend the majority of your time trying to find the highest value initiatives. If you get that correct, you can do less work, while having a larger impact.
5. Engineering best practice 👉 Don't repeat yourself
- As a data team, it's easy to keep doing the same thing for multiple people. Answering the same question, building the same dashboard, writing the same query. Every time you have a task in front of yourself, find a way to never have to do it again. If you don't know how - ask an engineer.
6. HR best practice 👉 The people matter. More than anything.
- As a data team, it's easy to get caught up in numbers and metrics, and forget that you're working in a company full of human beings. Allocate time to building relationships. To hear about someone's week. To actually connect with stakeholders you work with. It'll pay off in the long term, medium term, and short-term.
7. Finance best practice 👉 Think about economics. Please
- As a data team, you have to think about your team through the lens of a P&L. Your team has a cost (headcount + tooling + internal overhead) and your team creates value. The return on investment (the value created divided by the cost) should be a no brainer investment for your company. Every once in a while, take a step back and make sure that's the case. If not, find ways to increase the value you create, or reduce your costs.

### 10 tactical best practices for data leaders
- https://www.linkedin.com/posts/ethanaaron_10-tactical-best-practices-for-data-leaders-activity-7210743681497079808-gaSe/
1. Meet with everyone on the leadership team 1:1 at least once a month -- it's the best way to identify high value initiatives
2. Never talk about data technology, infrastructure, or queries with people outside the data team -- they just don't care
3. Categorize metrics on dashboards into either 'output metrics' (which you can't directly control) or 'input metrics' (which you can directly control
4. For input metrics, every chart on every dashboard should have an owner immediately above the chart (i.e. Ethan is accountable for writing 10 mediocre LinkedIn posts per month)
5. Only maintain 5-10 dashboards as a company. If someone asks for dashboard 11, make sure one of the other 10 is deprecated before any work begins on the new dashboard
6. Get involved in strategy. Every quarter (maybe every year) your company adjusts its strategy (i.e. the big moves the company plans to make in order to gain leverage). These strategy changes lead to priorities changing and the relative importance of metrics and data assets changing. You should be the first to hear when a strategy shift is happening so you can help define the goals and traction metrics that align
7. Watch your costs. At least every week you should know how much money is being spent on data headcount and data technology. Every dollar should generate a significant and quantifiable return on investment (ROI) each year
8. Track value created. It's tough, I know. But you need to at least have back of the envelope metrics or testimonials from executives that demonstrate the value the data team is creating on the whole and from particular initiatives. This is ammo for raises, headcount planning, and technology budget (if you can justify the ROI)
9. Always ask yourself: 'If we did this in a spreadsheet would we really be THAT much worse off?' You'll find that if you let business users keep low value stuff in spreadsheets, the ROI of your team will skyrocket
10. Create two paths for data asset development. First, a production path that has a rigorous QA process and ensures production data assets can be trusted. Second, an ad hoc path that allows for faster iteration and allows teams to innovate quickly without having to wait in a long production development backlog

### Solid Data Engineering Foundations make Data Teams successful
- https://www.linkedin.com/pulse/data-science-hierarchy-needs-emmanuel-ogungbemi-phd/
![1649947427479](https://github.com/user-attachments/assets/13cd7f76-1e24-465c-a529-168acbd1a9d8)
- Foundations of Data Teams https://www.youtube.com/watch?v=rsxNvLs3yKo
![Screenshot_20240710-072131_YouTube](https://github.com/user-attachments/assets/61a797ca-4a24-4caa-979f-11d4151bd203)
![Screenshot_20240710-072146_YouTube](https://github.com/user-attachments/assets/586fd3bc-a7bd-4336-a9c8-7ed2e3560f19)

## Data Product
- https://moderndata101.substack.com/p/how-to-build-data-products-design
- https://moderndata101.substack.com/p/how-to-build-data-products-build
- https://moderndata101.substack.com/p/how-to-build-data-products-deploy
- https://moderndata101.substack.com/p/evolving-data-products
- https://moderndata101.substack.com/p/transitioning-to-a-data-product-ecosystem
- https://moderndata101.substack.com/p/data-pipelines-for-data-products
	- Data product is an autonomous, read-optimized, standardized data unit containing at least one dataset (Domain Dataset), created for satisfying user needs
 	- Both internal and external data products
	- An internal data product is an application that uses data to make the next action immediate (e.g. a dashboard)
- https://moderndata101.substack.com/p/the-go-to-metrics-for-data-products
	- Product = customer x business x technology
	- customer metrics: customer lifetime value, # new users, DAU / MAU, retention rate, etc.
	- business metrics: directly generated revenue, costs / time saved
 	- market metrics: # new opportunities / listings per month, etc. and how it affects the business
	- tech metrics: cycle time, deployment frequency
- https://www.datamesh-architecture.com/data-product-canvas
	- A Data Product Canvas is a visual framework that guides your team through the data product specification. We suggest to fill out this canvas collaboratively. In total, the Data Product Canvas consists of ten building blocks:
	- Domain
	- Data Product Name
	- Consumer and Use Case
	- Output Port
	- Metadata
	- Input Ports
	- Data Product Design
	- Observability
	- Ubiquitous Language
	- Classification
- Understand business requirements for upcoming data ingestion work (Securities data, Master data, Positions data etc.)
	- What’s the timeline to implement the pipeline?
	- What level of testing is required e.g., Source-to-Target reconciliation, Basic Data Quality vs Functional Testing)
	- What volume of data are we dealing with?
	- How will the data be consumed once it has been hosted in the Cloud Data Lake (AWS S3) and Warehouse (Snowflake)?
- Create a data pipeline spec that covers quality checks, assumptions, business metrics, and allows stakeholders to give feedback BEFORE you start coding
   	- stakeholders / end users / areas impacted
	- data
		- upstream / source
			- data contracts?
		- downstream
			- internal tools
			- external tools
			- KPIs / metrics
			- data science / ML
		- frequency
	- level of testing
	- implementation timeline
- Build data quality checks into your pipelines using data contracts such as write-audit-publish and write unit and integration tests to catch quality errors before they enter production
- Discover the power of data lake technologies Apache Iceberg. Proper schema evolution, partitioning, and parquet file format compression!
- Level up your SQL skills by having a four-hour crash course on GROUPING SETS, window functions, and cumulative table design

## KPIs
- Types of startup metrics
	- https://www.linkedin.com/posts/davidsymsmith_startupmetrics-performanceindicators-metrics-activity-7130177000257818625-R0U6/
- Data team advice
	- https://youtube.com/watch?v=6HLo36SjOdo&si=ymtFT7JhkUukQ5sl
		- Focus on metric deltas between time periods,  cohorts
		- Attend non data team meetings,  e.g. marketing, revenue driving 
- 1st level metrics, 2nd level metrics
	- https://www.kalungi.com/blog/10-marketing-kpis-every-b2b-saas-company-should-track
	- https://userpilot.com/blog/b2b-saas-metrics/
	- https://www.chargebee.com/blog/saas-kpis/ 
- Customer Lifetime Value = Average Revenue Per Customer / Churn Rate, Customer Acquisition Cost,
	- The CLV is the amount the customer spends every month (average revenue per customer, or ARPC for short) times the expected number of months they use our platform for. A clearer way of defining CLV is by dividing the ARPC by the churn rate (the percentage of users that stop using our platform each month)
 	- https://www.interviewquery.com/questions/marketing-channel-metrics
  	- 
![kpi](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b150e889-1832-41c3-a07b-05b40fbb0dc4)
