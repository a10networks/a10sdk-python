from a10sdk.common.A10BaseClass import A10BaseClass


class CalcSha1(A10BaseClass):
    
    """    :param sha1_value: {"description": "Cleartext password", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Calculate sha1 value of a cleartext password.

    Class calc-sha1 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/dblb/{name}/calc-sha1`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "calc-sha1"
        self.a10_url="/axapi/v3/slb/template/dblb/{name}/calc-sha1"
        self.DeviceProxy = ""
        self.sha1_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


