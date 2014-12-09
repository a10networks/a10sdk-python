from a10sdk.common.A10BaseClass import A10BaseClass


class Vni(A10BaseClass):
    
    """Class Description::
    IP Address of the local tunnel end point.

    Class vni supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lif: {"description": "Logical interface binding the Provider Partition to the User Partition (logical interface number)", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}
    :param partition: {"description": "Name of the Partition with the L2 segment being extended (Name of the User Partition with the L2 segment being extended)", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param segment: {"description": "Id of the segment that is being extended", "format": "number", "type": "number", "maximum": 16777215, "minimum": 1, "optional": false}
    :param gateway: {"default": 0, "optional": true, "type": "number", "description": "This is a Gateway segment id", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address/vni/{segment}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "segment"]

        self.b_key = "vni"
        self.a10_url="/axapi/v3/overlay-tunnel/vtep/{id}/source-ip-address/vni/{segment}"
        self.DeviceProxy = ""
        self.lif = ""
        self.partition = ""
        self.segment = ""
        self.gateway = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


