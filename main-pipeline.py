import pdf2md as p2m
import md2parquet as m2p
import load_bucket as lb
import test_parser as tp

BRONZE_RAW_ZONE = "bronze/raw"
BRONZE_PARSED_ZONE = "bronze/parsed"
SILVER_ZONE = "silver/"
GOLD_ZONE = "gold/"

storage = ""

lb.download(storage,BRONZE_RAW_ZONE)

tp.parse(BRONZE_RAW_ZONE,BRONZE_PARSED_ZONE)

m2p.mdtoparquet(BRONZE_PARSED_ZONE,f"{SILVER_ZONE}factures-caroline.parquet")

lb.upload(SILVER_ZONE,f"{storage}silver")

