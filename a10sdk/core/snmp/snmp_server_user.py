from a10sdk.common.A10BaseClass import A10BaseClass


class User(A10BaseClass):
    
    """Class Description::
    Define a user who can access the SNMP engine.

    Class user supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param username: {"description": "Name of the user", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param auth_val: {"optional": true, "enum": ["md5", "sha"], "type": "string", "description": "'md5': Use HMAC MD5 algorithm for authentication; 'sha': Use HMAC SHA algorithm for authentication; ", "format": "enum"}
    :param group: {"description": "Group to which the user belongs", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param encpasswd: {"description": "Passphrase for encryption", "format": "password", "minLength": 8, "optional": true, "maxLength": 31, "type": "string"}
    :param passwd: {"description": "Password of this user", "format": "password", "minLength": 8, "optional": true, "maxLength": 31, "type": "string"}
    :param priv_pw_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)", "format": "encrypted"}
    :param v3: {"optional": true, "enum": ["auth", "noauth"], "type": "string", "description": "'auth': Using the authNoPriv Security Level; 'noauth': Using the noAuthNoPriv Security Level; ", "format": "enum"}
    :param pw_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)", "format": "encrypted"}
    :param priv: {"optional": true, "enum": ["des", "aes"], "type": "string", "description": "'des': DES encryption alogrithm; 'aes': AES encryption alogrithm;  (Encryption type)", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/user/{username}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "username"]

        self.b_key = "user"
        self.a10_url="/axapi/v3/snmp-server/user/{username}"
        self.DeviceProxy = ""
        self.username = ""
        self.auth_val = ""
        self.group = ""
        self.encpasswd = ""
        self.passwd = ""
        self.priv_pw_encrypted = ""
        self.v3 = ""
        self.pw_encrypted = ""
        self.priv = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


