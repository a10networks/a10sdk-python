from a10sdk.common.A10BaseClass import A10BaseClass


class Dns(A10BaseClass):
    
    """Class Description::
    DNS Global Options.

    Class dns supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'none': No action (default); 'drop': Drop query; 'reject': Send refuse response; 'ignore': Send empty response; ", "format": "enum", "default": "none", "type": "string", "enum": ["none", "drop", "reject", "ignore"], "optional": true}
    :param logging: {"description": "'none': No logging (default); 'query': DNS Query; 'response': DNS Response; 'both': Both DNS Query and Response; ", "format": "enum", "default": "none", "type": "string", "enum": ["none", "query", "response", "both"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/dns`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns"
        self.a10_url="/axapi/v3/gslb/dns"
        self.DeviceProxy = ""
        self.action = ""
        self.logging = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


