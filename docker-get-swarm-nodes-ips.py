import docker
import sys

client = docker.DockerClient(base_url=f"tcp://{sys.argv[1]}:2375")

nodes = client.nodes.list()
for node in nodes:
    try:
        print(node.attrs["Status"]["Addr"])
    except:
        pass
