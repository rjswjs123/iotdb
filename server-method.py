import uuid
from threading import Thread
import copy
import logging
from datetime import datetime
import time
from math import sin
import sys

from opcua.ua import NodeId, NodeIdType

sys.path.insert(0, "..")

try:
    from IPython import embed
except ImportError:
    import code

    def embed():
        myvars = globals()
        myvars.update(locals())
        shell = code.InteractiveConsole(myvars)
        shell.interact()

from opcua import ua, uamethod, Server


class SubHandler(object):
    """
    Subscription Handler. To receive events from server for a subscription
    """

    def datachange_notification(self, node, val, data):
        print("Python: New data change event", node, val)

    def event_notification(self, event):
        print("Python: New event", event)


# method to be exposed through server

def func(parent, variant):
    ret = False
    if variant.Value % 2 == 0:
        ret = True
    return [ua.Variant(ret, ua.VariantType.Boolean)]


# method to be exposed through server
# uses a decorator to automatically convert to and from variants

@uamethod
def multiply(parent, x, y):
    print("multiply method call with parameters: ", x, y)
    return x * y


class VarUpdater(Thread):
    def __init__(self, var):
        Thread.__init__(self)
        self._stopev = False
        self.var = var

    def stop(self):
        self._stopev = True

    def run(self):
        while not self._stopev:
            v = sin(time.time() / 10)
            self.var.set_value(v)
            time.sleep(0.1)


if __name__ == "__main__":
    # optional: setup logging
    logging.basicConfig(level=logging.WARN)
    #logger = logging.getLogger("opcua.address_space")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.internal_server")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.binary_server_asyncio")
    # logger.setLevel(logging.DEBUG)
    #logger = logging.getLogger("opcua.uaprocessor")
    # logger.setLevel(logging.DEBUG)

    # now setup our server
    server = Server()

    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    server.set_server_name("FreeOpcUa Example Server")
    # # set all possible endpoint policies for clients to connect through
    # server.set_security_policy([
    #             ua.SecurityPolicyType.NoSecurity,
    #             ua.SecurityPolicyType.Basic256Sha256_SignAndEncrypt,
    #             ua.SecurityPolicyType.Basic256Sha256_Sign])

    # setup our own namespace
    uri = "http://examples.freeopcua.github.io"
    idx = server.register_namespace(uri)

    # create directly some objects and variables
    myobj = server.nodes.objects.add_object(idx, "MyObject")
    myvar = myobj.add_variable(idx, "MyVariable", 6.7)
    multiply_node = myobj.add_method(idx, "multiply", multiply,
                                     [ua.VariantType.Int64, ua.VariantType.Int64], [ua.VariantType.Int64])

    # # import some nodes from xml
    # server.import_xml("custom_nodes.xml")

    # # creating a default event object
    # # The event object automatically will have members for all events properties
    # # you probably want to create a custom event type, see other examples
    # myevgen = server.get_event_generator()
    # myevgen.event.Severity = 300

    # starting!
    server.start()

    try:
        embed()
    finally:

        server.stop()