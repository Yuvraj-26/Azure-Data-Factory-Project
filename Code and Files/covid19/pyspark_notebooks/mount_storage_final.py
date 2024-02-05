# Databricks notebook source
# MAGIC %md
# MAGIC ## Mount the following data lake storage gen2 containers
# MAGIC 1. raw
# MAGIC 2. processed
# MAGIC 3. lookup

# COMMAND ----------

# MAGIC %md
# MAGIC ### Set-up the configs
# MAGIC #### Please update the following 
# MAGIC - application-id
# MAGIC - service-credential
# MAGIC - directory-id

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "<application-id>",
           "fs.azure.account.oauth2.client.secret": "<service-credential>",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<directory-id>/oauth2/token"}

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the raw container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://raw@azure33covidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/azure33covidreportingdl/raw",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the processed container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://processed@azure33covidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/azure33covidreportingdl/processed",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Mount the lookup container
# MAGIC #### Update the storage account name before executing

# COMMAND ----------

dbutils.fs.mount(
  source = "abfss://lookup@azure33covidreportingdl.dfs.core.windows.net/",
  mount_point = "/mnt/azure33covidreportingdl/lookup",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Test if Directory Mounted Successfully
# MAGIC #### Check lookup, raw, and processed file info and file paths

# COMMAND ----------

dbutils.fs.ls("/mnt/azure33covidreportingdl/lookup")

# COMMAND ----------

dbutils.fs.ls("/mnt/azure33covidreportingdl/raw")

# COMMAND ----------

dbutils.fs.ls("/mnt/azure33covidreportingdl/processed")
