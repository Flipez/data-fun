import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

csv_file_path = "data/subway_only_dedup.csv"
parquet_file_path = "data/subway_only_dedup.parquet"

df = pd.read_csv(csv_file_path)
table = pa.Table.from_pandas(df)
pq.write_table(table, parquet_file_path)