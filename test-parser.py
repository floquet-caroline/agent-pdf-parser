import os
import glob
import pdf2md

INPUT_ZONE = "bronze/raw"
OUTPUT_ZONE = "bronze/parsed"

# Get all files from input zone as a list
pdf_files = glob.glob(os.path.join(INPUT_ZONE, "p*.pdf"))


for file_path in pdf_files:
    # For each file get its name to name the md file afterwards
    file_name = os.path.basename(file_path).split(".")[0]
    # Actually parse the pdf file
    content = pdf2md.parse_pdf_with_endpoints(file_path)
    # Write the md file
    output_path = f"{OUTPUT_ZONE}/{file_name}.md"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[{file_path}] Succesfully parsed to {output_path}")



