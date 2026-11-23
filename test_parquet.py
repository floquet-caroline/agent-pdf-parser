import md2parquet

BRONZE_ZONE = "bronze/parsed"
SILVER_ZONE = "silver/"

parquet_file = "factures.parquet"

md2parquet.mdtoparquet(BRONZE_ZONE,f"{SILVER_ZONE}{parquet_file}")

