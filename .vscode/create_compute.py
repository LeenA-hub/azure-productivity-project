from azure.ai.ml.entities import AmlCompute
from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient

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

cpu_cluster = AmlCompute(
    name="prod-compute",
    size="Standard_DS11_v2",
    min_instances=0,
    max_instances=2
)

ml_client.begin_create_or_update(cpu_cluster)