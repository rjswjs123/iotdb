import sys
sys.path.insert(0, "..")
import logging
import time

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        vars = globals()
        vars.update(locals())
        shell = code.InteractiveConsole(vars)
        shell.interact()


from opcua import Client
from opcua import ua

if __name__ == "__main__":
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("KeepAlive")
    #logger.setLevel(logging.DEBUG)

    client = Client("opc.tcp://localhost:4840/freeopcua/server/")
    # client = Client("opc.tcp://admin@localhost:4840/freeopcua/server/") #connect using a user
    try:
        client.connect()

        # Client has a few methods to get proxy to UA nodes that should always be in address space such as Root or Objects
        root = client.get_root_node()

        # gettting our namespace idx
        uri = "http://examples.freeopcua.github.io"
        idx = client.get_namespace_index(uri)

        # Now getting a variable node using its browse path
        obj = root.get_child(["0:Objects", "{}:MyObject".format(idx)])

        # calling a method on server
        res = obj.call_method("{}:multiply".format(idx), 5, "abc")
        print("method result is: ", res)

        embed()
    finally:
        client.disconnect()