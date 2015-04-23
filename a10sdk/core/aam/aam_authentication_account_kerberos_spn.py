from a10sdk.common.A10BaseClass import A10BaseClass


class KerberosSpn(A10BaseClass):
    
    """Class Description::
    AD domain account associated with a SPN.

    Class kerberos-spn supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param account: {"description": "Specify domain account for SPN", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param realm: {"description": "Specify Kerberos realm", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param name: {"description": "Specify AD account name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.)", "format": "encrypted"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param password: {"default": 0, "optional": true, "type": "number", "description": "Specify password of domain account", "format": "flag"}
    :param service_principal_name: {"description": "Specify service principal name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param secret_string: {"description": "Password of AD account", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/account/kerberos-spn/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "kerberos-spn"
        self.a10_url="/axapi/v3/aam/authentication/account/kerberos-spn/{name}"
        self.DeviceProxy = ""
        self.account = ""
        self.realm = ""
        self.name = ""
        self.encrypted = ""
        self.uuid = ""
        self.password = ""
        self.service_principal_name = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


