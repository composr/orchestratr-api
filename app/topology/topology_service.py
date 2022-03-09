import requests

from topology_models import Topology

class TopologyService:

    def __init__(self, namespace: str):
        #fetch the Topology
        self._fetch_topology(namespace)

    def _fetch_topology(namespace: str):
        requests.get(url = "foo.bar")
