from prefect import Client
from fastapi import HTTPException

# Replace with Prefect server host:port
prefect_server = "http://20.25.85.193:4200/graphql"

client = Client(
    api_server = prefect_server
)

# Get the flow id of latest version using flow name
def prefect_flow(name):
    try: 
        flowId_by_name = '''
            query flowByName($name: String)
            {
                flow(
                    where: {
                        name: {_eq: $name}
                    },
                    order_by: {version: desc},
                    limit: 1,
                )
                {
                    id
                }
            }
        '''

        id = client.graphql(flowId_by_name, variables={'name': name})
        flow_run = client.create_flow_run(flow_id = id['data']['flow'][0]['id'])
        return flow_run
    
    except:
        # If flow name doesn't exist, return HTTP 404
        raise HTTPException(status_code=404, detail="Flow not found")
 