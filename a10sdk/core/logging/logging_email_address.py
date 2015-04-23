from a10sdk.common.A10BaseClass import A10BaseClass


class EmailList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param email_address: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Email address information of recipients", "format": "email-addr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "email-list"
        self.DeviceProxy = ""
        self.email_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EmailAddress(A10BaseClass):
    
    """Class Description::
    Set the recipients address.

    Class email-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param email_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"email-address": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Email address information of recipients", "format": "email-addr"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/logging/email-address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "email-address"
        self.a10_url="/axapi/v3/logging/email-address"
        self.DeviceProxy = ""
        self.uuid = ""
        self.email_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


