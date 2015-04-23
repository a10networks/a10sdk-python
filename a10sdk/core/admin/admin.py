from a10sdk.common.A10BaseClass import A10BaseClass


class PrivilegeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param partition_name: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Partition Name", "format": "string"}
    :param privilege_partition: {"enum": ["partition-enable-disable", "partition-read", "partition-write"], "type": "string", "description": "'partition-enable-disable': Set per-partition enable/disable privilege; 'partition-read': Set per-partition read privilege; 'partition-write': Set per-partition write privilege; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "privilege-list"
        self.DeviceProxy = ""
        self.partition_name = ""
        self.privilege_partition = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Admin(A10BaseClass):
    
    """Class Description::
    System admin user configuration.

    Class admin supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trusted_host_acl_id: {"description": "ACL ID", "format": "number", "type": "number", "maximum": 99, "minimum": 1, "optional": true}
    :param trusted_host_addr: {"not": "access-list", "optional": true, "type": "string", "description": "Trusted IP Address for admin to login (IP address, a.b.c.d)", "format": "ipv4-address"}
    :param privilege_global: {"optional": true, "enum": ["read", "write"], "type": "string", "description": "'read': Set read privilege; 'write': Set write privilege; ", "format": "enum"}
    :param trusted_host: {"default": 0, "optional": true, "type": "number", "description": "Set trusted network administrator can login in", "format": "flag"}
    :param privilege_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"partition-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Partition Name", "format": "string"}, "privilege-partition": {"enum": ["partition-enable-disable", "partition-read", "partition-write"], "type": "string", "description": "'partition-enable-disable': Set per-partition enable/disable privilege; 'partition-read': Set per-partition read privilege; 'partition-write': Set per-partition write privilege; ", "format": "enum"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param access_list: {"description": "Specify an ACL to classify a trusted host", "format": "flag", "default": 0, "optional": true, "not": "trusted-host-addr", "type": "number"}
    :param unlock: {"default": 0, "optional": true, "type": "number", "description": "Unlock admin user", "format": "flag"}
    :param password_key: {"default": 0, "optional": true, "type": "number", "description": "Config admin user password", "format": "flag"}
    :param passwd_string: {"description": "Config admin user password", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param trusted_host_netmask: {"optional": true, "type": "string", "description": "Netmask, a.b.c.d", "format": "ipv4-netmask"}
    :param action: {"description": "'enable': Enable user; 'disable': Disable user; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param user: {"description": "System admin user name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/admin/{user}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "user"]

        self.b_key = "admin"
        self.a10_url="/axapi/v3/admin/{user}"
        self.DeviceProxy = ""
        self.trusted_host_acl_id = ""
        self.trusted_host_addr = ""
        self.privilege_global = ""
        self.trusted_host = ""
        self.privilege_list = []
        self.uuid = ""
        self.access = {}
        self.access_list = ""
        self.unlock = ""
        self.ssh_pubkey = {}
        self.password_key = ""
        self.passwd_string = ""
        self.trusted_host_netmask = ""
        self.action = ""
        self.password = {}
        self.user = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


