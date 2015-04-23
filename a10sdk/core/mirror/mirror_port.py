from a10sdk.common.A10BaseClass import A10BaseClass


class MirrorPort(A10BaseClass):
    
    """Class Description::
    Enable a port to act as Mirror Port.

    Class mirror-port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ethernet: {"optional": true, "type": "number", "description": "Ethernet port as mirror port (Port Value)", "format": "interface"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param mirror_index: {"description": "Mirror index", "format": "number", "type": "number", "maximum": 4, "minimum": 1, "optional": false}
    :param mirror_dir: {"description": "'input': Mirror incoming packets to this port; 'output': Mirror outgoing packets to this port; 'both': Mirror both incoming and outgoing packets to this port; ", "format": "enum", "default": "both", "type": "string", "enum": ["input", "output", "both"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/mirror-port/{mirror_index}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "mirror_index"]

        self.b_key = "mirror-port"
        self.a10_url="/axapi/v3/mirror-port/{mirror_index}"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.uuid = ""
        self.mirror_index = ""
        self.mirror_dir = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


