from azure.identity import DefaultAzureCredential
from azure.ai.ml import MLClient
from azure.ai.ml.entities import AmlCompute
from azure.ai.ml.entities import Workspace
from azure.ai.ml.entities import WorkspaceKind


# Put your Azure details here:
subscription_id = "6bc62e78-9b6b-43f6-ac00-5606b77589e1"
resource_group = "productivity-rg"
workspace_name = "productivity-ws"

# This creates the ml_client instance — this MUST come BEFORE you use ml_client
ml_client = MLClient(
    DefaultAzureCredential(),
    subscription_id,
    resource_group,
    workspace_name
)
# Create a workspace
workspace = Workspace(
    name=workspace_name,
    location="canadacentral",  
    display_name="Productivity ML Workspace",
    description="Workspace for predicting productivity from daily data",
    tags={"project": "productivity-ml"},
)

ml_client.workspaces.begin_create(workspace)
