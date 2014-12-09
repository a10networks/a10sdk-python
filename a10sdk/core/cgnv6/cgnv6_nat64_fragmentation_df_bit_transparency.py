from a10sdk.common.A10BaseClass import A10BaseClass


class DfBitTransparency(A10BaseClass):
    
    """Class Description::
    Add an empty IPv6 fragmentation header if IPv4 DF bit is zero (default:disabled).

    Class df-bit-transparency supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param df_bit_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Add an empty IPv6 fragmentation header if IPv4 DF bit is zero; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/fragmentation/df-bit-transparency`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "df-bit-transparency"
        self.a10_url="/axapi/v3/cgnv6/nat64/fragmentation/df-bit-transparency"
        self.DeviceProxy = ""
        self.df_bit_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


