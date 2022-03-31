from prefect import task, Flow, Client
from python_terraform import *
from config import settings
from prefect.storage import Local, Azure
from prefect.run_configs import LocalRun

client = Client(
    api_server = settings.prefect_server
)

def temp_prefect_run(project_name, flow_name):
    @task
    def run_terraform():
        tf = Terraform(working_dir="C:\\Users\\stripathi\\OneDrive - CITIHUB INC\\Documents\\composr\\orchestratr-api\\app\\tempdelete")
        tf.init()
        tf.plan()
        tf.apply(skip_plan=True)

    with Flow(flow_name, storage=Local(), run_config=LocalRun(labels=['CH-US-STRI01'])) as f:      
        run_terraform()

    client.register(f, project_name)

    #f.storage = Local()

    #f.register(project_name=project_name)
    #storage=Azure(container="flows"),


    
