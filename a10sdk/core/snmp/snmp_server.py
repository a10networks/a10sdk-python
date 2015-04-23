from a10sdk.common.A10BaseClass import A10BaseClass


class SnmpServer(A10BaseClass):
    
    """Class Description::
    Configure SNMP engine parameters.

    Class snmp-server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param view_list: {"minItems": 1, "items": {"type": "view"}, "uniqueItems": true, "array": [{"required": ["viewname", "oid"], "properties": {"mask": {"description": "Hex octets, separated by '.', mask of oid", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "type", "type": "string"}, "oid": {"description": "MIB view family name or oid", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "type": {"description": "'included': MIB family is included in the view; 'excluded': MIB family is excluded from the view; ", "format": "enum", "type": "string", "enum": ["included", "excluded"], "not": "mask", "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "viewname": {"description": "Name of the view", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/view/{viewname}+{oid}"}
    :param group_list: {"minItems": 1, "items": {"type": "group"}, "uniqueItems": true, "array": [{"required": ["groupname"], "properties": {"read": {"description": "specify a read view for the group (read view name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "groupname": {"description": "Name of the group", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "v3": {"optional": true, "enum": ["auth", "noauth", "priv"], "type": "string", "description": "'auth': group using the authNoPriv Security Level; 'noauth': group using the noAuthNoPriv Security Level; 'priv': group using SNMPv3 authPriv security level; ", "format": "enum"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/group/{groupname}"}
    :param user_list: {"minItems": 1, "items": {"type": "user"}, "uniqueItems": true, "array": [{"required": ["username"], "properties": {"username": {"description": "Name of the user", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "auth-val": {"optional": true, "enum": ["md5", "sha"], "type": "string", "description": "'md5': Use HMAC MD5 algorithm for authentication; 'sha': Use HMAC SHA algorithm for authentication; ", "format": "enum"}, "group": {"description": "Group to which the user belongs", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "encpasswd": {"description": "Passphrase for encryption", "format": "password", "minLength": 8, "optional": true, "maxLength": 31, "type": "string"}, "passwd": {"description": "Password of this user", "format": "password", "minLength": 8, "optional": true, "maxLength": 31, "type": "string"}, "priv-pw-encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)", "format": "encrypted"}, "v3": {"optional": true, "enum": ["auth", "noauth"], "type": "string", "description": "'auth': Using the authNoPriv Security Level; 'noauth': Using the noAuthNoPriv Security Level; ", "format": "enum"}, "pw-encrypted": {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED passphrase string)", "format": "encrypted"}, "priv": {"optional": true, "enum": ["des", "aes"], "type": "string", "description": "'des': DES encryption alogrithm; 'aes': AES encryption alogrithm;  (Encryption type)", "format": "enum"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/user/{username}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "snmp-server"
        self.a10_url="/axapi/v3/snmp-server"
        self.DeviceProxy = ""
        self.enable = {}
        self.slb_data_cache_timeout = {}
        self.view_list = []
        self.community = {}
        self.contact = {}
        self.host = {}
        self.disable = {}
        self.location = {}
        self.group_list = []
        self.user_list = []
        self.engineID = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


