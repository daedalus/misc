import docker
import sys

client = docker.DockerClient(base_url="tcp://%s:2375" % sys.argv[1])

nodes = client.nodes.list()
for node in nodes:
    try:
        print node.attrs["Status"]["Addr"]
    except:
        pass
