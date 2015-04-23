from a10sdk.common.A10BaseClass import A10BaseClass


class Isis(A10BaseClass):
    
    """Class Description::
    IS-IS Routing for IP.

    Class isis supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param tag: {"description": "ISO routing area tag", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/ip/router/isis`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "isis"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/ip/router/isis"
        self.DeviceProxy = ""
        self.tag = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


