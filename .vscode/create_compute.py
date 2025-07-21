from xmlrpc import client
from azure.ai.ml.entities import AmlCompute

cpu_cluster = AmlCompute(
    name="prod-compute",
    size="Standard_DS11_v2",
    min_instances=0,
    max_instances=2
)

client.begin_create_or_update(cpu_cluster)