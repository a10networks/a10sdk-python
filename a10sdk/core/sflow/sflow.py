from a10sdk.common.A10BaseClass import A10BaseClass


class Sflow(A10BaseClass):
    
    """Class Description::
    Configure sFlow.

    Class sflow supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sflow"
        self.a10_url="/axapi/v3/sflow"
        self.DeviceProxy = ""
        self.source_address = {}
        self.agent = {}
        self.sampling = {}
        self.setting = {}
        self.polling = {}
        self.collector = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


