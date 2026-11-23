# Agent PDF Parser

## Description

This project has been created for a school project in the context of a course on AI security and architecture.

Its goal was to create a pipeline involving AI agents to parse, store and extract information from PDF documents, as well as being able to query them with MCP tools.

## Choices

- Python for code : I chose Python because I already had written a very simple prompting loop and therefore knew how to use the intended cloud-served LLM. That choice is also motivated by the language being easy to code in, and most importantly easy to read and debug.

- Gemma12b as the LLM : This was suggested by the teachers when we started the project and available on the cloud resources they gave us.

## Bricks

### PDF to md

This brick consists in parsing PDF files found in the `bronze/raw` folder into md files saved into the `bronze/parsed` folder. 
The bronze layer now includes a loader component that allows us to load and send data to the S3 bucket.

### md to parquet

This brick is also part of the bronze layer. Its goal is to compile the md files found in the `bronze/parsed`folder into a parquet database file saved into the `silver` folder. 

## Use project

To use the project, launch `main-pipeline.py` and it should process every PDF and send the parquet file back to S3.
The upload currently doesn't work for me because of S3 authentication that I didn't have the time to solve.