from prefect import Client
from fastapi import HTTPException

prefect_server = "http://20.185.237.231:4200/graphql"

client = Client(
    api_server = prefect_server
)

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
        raise HTTPException(status_code=404, detail="Flow not found")
 