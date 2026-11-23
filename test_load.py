import load_bucket as lb

BRONZE_ZONE = "bronze/raw"
SILVER_ZONE = "silver/"
GOLD_ZONE = "gold/"

storage = ""

lb.download(storage,BRONZE_ZONE)