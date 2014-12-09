from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param method_info: {"description": "Method INFO", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param stat_request: {"description": "Request Received", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param method_publish: {"description": "Method PUBLISH", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param method_unknown: {"description": "Method Unknown", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param method_message: {"description": "Method MESSAGE", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param method_subscribe: {"description": "Method SUBSCRIBE", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param method_invite: {"description": "Method INVITE", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param method_register: {"description": "Method REGISTER", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param method_prack: {"description": "Method PRACK", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param method_port_config: {"description": "Method OPTIONS", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param method_notify: {"description": "Method NOTIFY", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param method_ack: {"description": "Method ACK", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param method_refer: {"description": "Method REFER", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param stat_response: {"description": "Response Received", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param method_update: {"description": "Method UPDATE", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param method_bye: {"description": "Method BYE", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param method_cancel: {"description": "Method CANCEL", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.method_info = ""
        self.stat_request = ""
        self.method_publish = ""
        self.method_unknown = ""
        self.method_message = ""
        self.method_subscribe = ""
        self.method_invite = ""
        self.method_register = ""
        self.method_prack = ""
        self.method_port_config = ""
        self.method_notify = ""
        self.method_ack = ""
        self.method_refer = ""
        self.stat_response = ""
        self.method_update = ""
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
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/sip/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sip"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/sip/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


