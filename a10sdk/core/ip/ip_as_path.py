from a10sdk.common.A10BaseClass import A10BaseClass


class AsPath(A10BaseClass):
    
    """Class Description::
    Configure an AS-path list for BGP.

    Class as-path supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param access_list: {"description": "Specify an access list name (Regular expression access-list name)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param action: {"optional": false, "enum": ["deny", "permit"], "type": "string", "description": "'deny': Specify packets to reject; 'permit': Specify packets to forward; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param value: {"optional": false, "type": "string", "description": "A regular-expression to match the BGP AS paths", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/as-path/{access_list}+{action}+{value}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "access_list","action","value"]

        self.b_key = "as-path"
        self.a10_url="/axapi/v3/ip/as-path/{access_list}+{action}+{value}"
        self.DeviceProxy = ""
        self.access_list = ""
        self.action = ""
        self.uuid = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


