from a10sdk.common.A10BaseClass import A10BaseClass


class Ftp(A10BaseClass):
    
    """Class Description::
    NAT64 FTP ALG (default: enabled).

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trans_epsv_to_pasv: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': disable; ", "format": "enum"}
    :param trans_eprt_to_port: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': disable; ", "format": "enum"}
    :param xlat_no_trans_pasv: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': enable; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ftp_enable: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable NAT64 FTP ALG; ", "format": "enum"}
    :param trans_lpsv_to_pasv: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': disable; ", "format": "enum"}
    :param trans_lprt_to_port: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': disable; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64/alg/ftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/nat64/alg/ftp"
        self.DeviceProxy = ""
        self.trans_epsv_to_pasv = ""
        self.trans_eprt_to_port = ""
        self.xlat_no_trans_pasv = ""
        self.uuid = ""
        self.ftp_enable = ""
        self.trans_lpsv_to_pasv = ""
        self.trans_lprt_to_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


