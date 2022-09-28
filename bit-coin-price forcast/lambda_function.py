import json
import boto3
def lambda_handler(event, context):
    client = boto3.client("sagemaker")
    client.start_notebook_instance(NotebookInstanceName="ariq-test2")
    return {"res":"d"}
    
  
