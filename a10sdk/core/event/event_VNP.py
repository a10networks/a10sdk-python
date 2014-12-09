from a10sdk.common.A10BaseClass import A10BaseClass


class Vnp(A10BaseClass):
    
    """Class Description::
    module VNP.

    Class VNP supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param logging: {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}
    :param VNP_evnts: {"optional": false, "enum": ["part-create", "part-del"], "type": "string", "description": "'part-create': Create new partition; 'part-del': Delete a partition; ", "format": "enum"}
    :param email: {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/event/VNP/{VNP_evnts}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "VNP_evnts"]

        self.b_key = "VNP"
        self.a10_url="/axapi/v3/event/VNP/{VNP_evnts}"
        self.DeviceProxy = ""
        self.logging = ""
        self.VNP_evnts = ""
        self.email = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


