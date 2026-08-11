from kubernetes import client, config


class KubernetesService:

    def __init__(self):

        config.load_kube_config()

        self.v1 = client.CoreV1Api()

        self.apps = client.AppsV1Api()

    def get_pods(self):

        pods = self.v1.list_pod_for_all_namespaces()

        result = []

        for pod in pods.items:

            result.append({

                "name": pod.metadata.name,

                "namespace": pod.metadata.namespace,

                "status": pod.status.phase,

                "node": pod.spec.node_name

            })

        return result

    def get_nodes(self):

        nodes = self.v1.list_node()

        result = []

        for node in nodes.items:

            result.append({

                "name": node.metadata.name,

                "status": node.status.conditions[-1].type

            })

        return result
