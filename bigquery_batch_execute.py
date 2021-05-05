#!/usr/bin/env python
# Author Dario Clavijo 2018

import sys
from google.cloud import bigquery
from google.cloud.bigquery import Dataset

client = bigquery.Client()

# dataset_ref = client.dataset('dataset_name')
# dataset = Dataset(dataset_ref)
# dataset.description = 'my dataset'
# dataset = client.create_dataset(dataset)  # API request


def query(SQL, table_dest):
    job_config = bigquery.QueryJobConfig()
    table_ref = client.dataset(dataset_id).table(table_dest)
    job_config.destination = table_ref
    job_config.write_disposition = bigquery.WriteDisposition.WRITE_APPEND
    query_job = client.query(
        SQL, location="US", job_config=job_config
    )  # ,useLegacySql=False)
    rows = list(query_job)
    print("rows affected: %d" % len(rows))


fp = open(sys.argv[1])
dataset_id = sys.argv[2]
table_dest = sys.argv[3]

tmp = ""
for line in fp:
    if line.find('"""') == -1:
        line = line.replace("REGEXP_MATCH", "REGEXP_CONTAINS")
        line = line.replace("regexp_match", "REGEXP_CONTAINS")
        # line = line.replace('[','`').replace(']','`')
        # line = line.replace(':','.')
        tmp += line

tmp = tmp.split(";")
for sql in tmp:
    if sql != "" and sql != "\n":
        sql = sql + ";"
        print(sql)
        query(sql, table_dest)
