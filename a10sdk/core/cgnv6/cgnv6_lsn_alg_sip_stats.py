from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param method_options: {"description": "SIP Method OPTIONS", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param method_invite: {"description": "SIP Method INVITE", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param method_publish: {"description": "SIP Method PUBLISH", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param method_unknown: {"description": "SIP Method UNKNOWN", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param method_update: {"description": "SIP Method UPDATE", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param method_subscribe: {"description": "SIP Method SUBSCRIBE", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param method_register: {"description": "SIP Method REGISTER", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param method_prack: {"description": "SIP Method PRACK", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param method_notify: {"description": "SIP Method NOTIFY", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param method_info: {"description": "SIP Method INFO", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param method_ack: {"description": "SIP Method ACK", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param method_refer: {"description": "SIP Method REFER", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param method_message: {"description": "SIP Method MESSAGE", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param method_bye: {"description": "SIP Method BYE", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param method_cancel: {"description": "SIP Method CANCEL", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.method_options = ""
        self.method_invite = ""
        self.method_publish = ""
        self.method_unknown = ""
        self.method_update = ""
        self.method_subscribe = ""
        self.method_register = ""
        self.method_prack = ""
        self.method_notify = ""
        self.method_info = ""
        self.method_ack = ""
        self.method_refer = ""
        self.method_message = ""
        self.method_bye = ""
        self.method_cancel = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Sip(A10BaseClass):
    
    """Class Description::
    Statistics for the object sip.

    Class sip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/sip/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/sip/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


