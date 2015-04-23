from a10sdk.common.A10BaseClass import A10BaseClass


class Delete(A10BaseClass):
    
    """    :param private_key: {"description": "Private key file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ca: {"description": "CA certificate file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param cert_name: {"description": "Certificate file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param crl: {"description": "CRL file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delete SSL cert.

    Class delete supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/pki/delete`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "delete"
        self.a10_url="/axapi/v3/pki/delete"
        self.DeviceProxy = ""
        self.private_key = ""
        self.ca = ""
        self.cert_name = ""
        self.crl = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


