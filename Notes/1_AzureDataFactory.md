# Azure-Data-Factory

Real world Data Engineering Project using Azure Data Factory, SQL, Data Lake, Databricks, HDInsight, CI/CD

## Azure Data Factory Definition
- A fully managed, serverless data integration solution for ingesting, preparing, and transforming all of your data at scale

## The Data Problem
- Businesses generated exponential volume of data from a variety of sources such as multi cloud platforms, on premises applications and SaaS Applications
- The rate of data arrival could be near real-time or in batches at regular intervals
- Generate data is in a variety of formats (structured, semi-structured, and unstructured)
- Businesses want this data to be ingested and processed quickly in a consistent manner
to gain insights from their data. Traditional data integration solutions struggle to handle this due to the lack of connectors and ability to scale elastically,

## Azure Data Factory
- Data Factory provides the ability to ingest data from many sources and provides connectors to 90+ sources, including support for ingesting data from Amazon S3 and Google Cloud Storage
- Data Factory also provides the ability to transform and analyse the data., if we need a transformation that's not available in Data Factory or is too complex to achieve in Data Factory, we can create transformations in external solutions such as Spark to run on HDInsight or Azure Databricks. We can then orchestrate these transformation from the Data Factory. We can create ML models in Azure ML or in Databricks, we can orchestrate those executions from Data Factory
- Data Factory is used to orchestrate the publishing of dashboards created in tools such as Power BI to the data consumers.

## Azure Data Factory Overview

- Full manages service - Microsoft handles management of the Data Factory, including provisioning VMs, installing the application, OS patches, scalability, availability, and security requirements
- Serverless - Compute environment can scale to any data size without infrastructure management
- Data integration service - connectors from multi-cloud to on-premises and SaaS solutions
- Data Transformation Service - Transformation of the data
- Data Orchestration Service - Orchestration of data pipelines and monitoring capabilities

## Data Factory Is Not
- Data Migration Tool - Data migration is the process of transferring data from one storage system or computing environment to another. For migration of data from one database to another, use Azure Data Migration service
- Data Streaming Service - Data Factory is optimised for loading and transforming data periodically. It is not designed to support streaming workloads. For data streaming use Azure pass services such as Azure Event Hubs – A real-time data streaming platform with native Apache Kafka support or Azure IoT Hub - a managed service hosted in the cloud that acts as a central message hub for communication between an IoT application and its attached devices, or external applications such as Spark Streaming, Kafka
- Suitable for Complex Data Transformations - better to perform complex transformations in Azure Databricks or HDInsight using Spark and use Data Factory to orchestrate the workflow
- Data Storage Solution - Data Factory does not store the data, but provides the compute required to process the data. Once processed the data is returned to a storage solution such as SQL Database or Data Lake or Azure Synapse Analytics or Cosmos DB  
