from a10sdk.common.A10BaseClass import A10BaseClass


class DeleteOper(A10BaseClass):
    
    """    :param filename: {"minLength": 1, "maxLength": 255, "type": "string", "optional": true, "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    .

    Class delete-oper supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/delete-oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "delete-oper"
        self.a10_url="/axapi/v3/pki/delete-oper"
        self.DeviceProxy = ""
        self.filename = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


