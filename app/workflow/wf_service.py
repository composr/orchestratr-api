from prefect import Client
from fastapi import HTTPException
from config import settings

client = Client(
    api_server = settings.prefect_server
)

# Get the flow id of latest version using flow name
def prefect_flow(project_name, flow_name):
    try: 
        project_id_by_name = '''
            query project_by_name($project_name: String)
            {
                project(
                    where: {
                        name: {_eq: $project_name}
                    }
                )
                {
                    id
                }
            }
        '''
    except:
        raise HTTPException(status_code=404, detail="Project not found")

    try:
        flow_id_by_name = '''
            query flow_by_name($name: String, $project_id: uuid)
            {
                flow(
                    where: {
                        name: {_eq: $name},
                        project_id: {_eq: $project_id}
                    },
                    order_by: {version: desc},
                    limit: 1,
                )
                {
                    id
                }
            }
        '''

        project_id = client.graphql(project_id_by_name, variables={'project_name': project_name})        
        id = client.graphql(flow_id_by_name, variables={'name': flow_name, 'project_id': project_id['data']['project'][0]['id']})
        flow_run = client.create_flow_run(flow_id = id['data']['flow'][0]['id'])

        return flow_run
    
    except:
        raise HTTPException(status_code=404, detail="Project or Flow not found")
 