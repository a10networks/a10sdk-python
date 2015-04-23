from a10sdk.common.A10BaseClass import A10BaseClass


class BwList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_name: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Blacklist/whitelist Name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bw-list"
        self.DeviceProxy = ""
        self.file_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Delete(A10BaseClass):
    
    """    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete Configuration file.

    Class delete supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "delete"
        self.a10_url="/axapi/v3/delete"
        self.DeviceProxy = ""
        self.health_postfile = {}
        self.geo_location = {}
        self.bw_list = {}
        self.auth_portal_image = {}
        self.partition = {}
        self.debug_monitor = {}
        self.web_category = {}
        self.health_external = {}
        self.auth_portal = {}
        self.startup_config = {}
        self.local_uri_file = {}
        self.auth_saml_idp = {}
        self.cgnv6 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


