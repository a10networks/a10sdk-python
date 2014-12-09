from a10sdk.common.A10BaseClass import A10BaseClass


class Synchronization(A10BaseClass):
    
    """Class Description::
    help Perform IGP synchronization.

    Class synchronization supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param network_synchronization: {"default": 0, "optional": true, "type": "number", "description": "Perform IGP synchronization", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/network/synchronization`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "synchronization"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/network/synchronization"
        self.DeviceProxy = ""
        self.network_synchronization = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


