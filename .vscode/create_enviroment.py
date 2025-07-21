from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Environment

# Add your Azure subscription details here
subscription_id = "6bc62e78-9b6b-43f6-ac00-5606b77589e1"
resource_group = "productivity-rg"
workspace_name = "productivity-ws"

# Create the MLClient instance — this is REQUIRED before using it
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id,
    resource_group,
    workspace_name
)

env = Environment(
    name="prod-env",
    image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04",
    conda_file="./env.yml",
    description="Env for productivity model",
)

# Create or update environment in Azure
ml_client.environments.create_or_update(env)
print("Environment created/updated successfully!")