from pathlib import Path
import pandas as pd
import glob
import os

# Define the directory containing your .md files and the output parquet file path
# md_dir = Path("./markdown_files")
# output_parquet = "markdown_database.parquet"

#pdf_files = glob.glob(os.path.join(INPUT_ZONE, "p*.pdf"))

def mdtoparquet(md_input,parquet_output):
  # List to hold data for each markdown file
  data = []

  # Iterate through all .md files in the directory
  md_files = glob.glob(os.path.join(md_input,"*.md"))
  for file_path in md_files:
    # Read the content of the markdown file
    with open(file_path, "r", encoding="utf-8") as f:
      content = f.read()

    # Append a dictionary with metadata and content
    data.append({
        "filename": os.path.basename(file_path).split(".")[0],
        "filepath": str(file_path),
        "content": content,
    })

  # Convert the list of dictionaries into a Pandas DataFrame
  df = pd.DataFrame(data)

  # Save the DataFrame to a Parquet file
  df.to_parquet(parquet_output, engine="pyarrow", index=False)

  print(
      f"[{md_input}] Compiled {len(df)} Markdown files into '{parquet_output}'"
  )