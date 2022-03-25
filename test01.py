# Databricks notebook source
# MAGIC %python
# MAGIC  print('C:\some\name') 

# COMMAND ----------

# MAGIC %python
# MAGIC # pandas 사용하기
# MAGIC import numpy as np # numpy 도 함께 import
# MAGIC import pandas as pd
# MAGIC 
# MAGIC 
# MAGIC obj = pd.Series([4, 7, -5, 3])
# MAGIC obj

# COMMAND ----------

# MAGIC %python
# MAGIC # Data Frame 정의하기
# MAGIC # 이전에 DataFrame에 들어갈 데이터를 정의해주어야 하는데,
# MAGIC # 이는 python의 dictionary 또는 numpy의 array로 정의할 수 있다.
# MAGIC data = {'name': ['Beomwoo', 'Beomwoo', 'Beomwoo', 'Kim', 'Park'],
# MAGIC         'year': [2013, 2014, 2015, 2016, 2015],
# MAGIC         'points': [1.5, 1.7, 3.6, 2.4, 2.9]}
# MAGIC df = pd.DataFrame(data)
# MAGIC df

# COMMAND ----------

# MAGIC %python
# MAGIC df['penalty'] = 0.5

# COMMAND ----------

df

# COMMAND ----------

df['zeros'] = df['points']*df['penalty']

# COMMAND ----------

df

# COMMAND ----------

df.groupby(['name']).mean()

# COMMAND ----------

df.sum()

# COMMAND ----------


