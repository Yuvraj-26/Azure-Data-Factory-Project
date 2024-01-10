# Data Flows - Cases and Deaths Data Transformation


## Data Flows

- Code free data transformations
- Executed on Data Factory managed scaled-out Apache Spark clusters
- Benefits from Data factory scheduling and monitoring capabilities
- Data flow activities can be operationalized using existing Azure Data Factory scheduling, control, flow, and monitoring capabilities


Types:
- Data flow (mapping data flow ) - code free transformations at scale for fixed schema and known transformation logic upfront
- Wrangling Data Flow - code free data preparation at scale for visually exploring and preparing datasets

Limitations:
- Only available in some regions
- Limited set of connectors available
- Not suitable for very complex logic (complex design logic is difficult to maintain in Data factory, use Spark instead and execute using Data Factory)


Data Flow UI:
- Add Source to select dataset source
- Optimize is used for performance tuning and as Spark runs on distributed computing, partition options are crucial for performance.
- Use current partitioning means Data Factory will select the most suitable partition type based on the data source, however partition types can be set based on better understanding of the data
- Data Flow debug allows data preview as it flows through the Data Flow system (incurs charges due to use of Spark cluster)
- Transformations (joins, exists, lookup, union, etc), Schema modifiers (select, aggregate, surrogate key usually for fact/dimension models, pivot, windows etc), Raw modifiers (filter, sort, alter row), Destination (sink transformation)
- Data flows executed by building a pipeline and using Data Flow Activity
- Specify settings for Data Flow activities including clusters and integration run time and core count
- Specify any Parameters to be sent from pipeline to the Data Flow. For example, parameters sent from trigger to pipeline to data flow to allow parameters into our transformation actions
- Trigger or debug the pipeline and monitor

## Transform Cases and Deaths Data Requirements
- cases_deaths data file contains countries outside of Europe, filtering is required
- the country_code across files are 3 digit or 2 digit country codes or missing, therefore need to be standardised across files to allow joins on country codes and various reporting queries
- pivot the data based on the values in indicator and daily count columns to create confirmed cases and deaths column

<img src="Docs/transformation1.png">
