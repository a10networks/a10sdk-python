from a10sdk.common.A10BaseClass import A10BaseClass


class SessionList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_id: {"type": "number", "format": "number"}
    :param connection_succeeded: {"type": "number", "format": "number"}
    :param sessions_dropped: {"type": "number", "format": "number"}
    :param retry: {"type": "number", "format": "number"}
    :param update_packet_sent: {"type": "number", "format": "number"}
    :param open_packet_received: {"type": "number", "format": "number"}
    :param protocol_info: {"type": "string", "format": "string"}
    :param keepalive_packet_received: {"type": "number", "format": "number"}
    :param update_packet_received: {"type": "number", "format": "number"}
    :param notify_packet_sent: {"type": "number", "format": "number"}
    :param open_packet_sent: {"type": "number", "format": "number"}
    :param state: {"type": "string", "format": "string"}
    :param keepalive_packet_sent: {"type": "number", "format": "number"}
    :param message_header_error: {"type": "number", "format": "number"}
    :param open_session_failed: {"type": "number", "format": "number"}
    :param notify_packet_received: {"type": "number", "format": "number"}
    :param open_session_succeeded: {"type": "number", "format": "number"}
    :param connection_failed: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "session-list"
        self.DeviceProxy = ""
        self.session_id = ""
        self.connection_succeeded = ""
        self.sessions_dropped = ""
        self.retry = ""
        self.update_packet_sent = ""
        self.open_packet_received = ""
        self.protocol_info = ""
        self.keepalive_packet_received = ""
        self.update_packet_received = ""
        self.notify_packet_sent = ""
        self.open_packet_sent = ""
        self.state = ""
        self.keepalive_packet_sent = ""
        self.message_header_error = ""
        self.open_session_failed = ""
        self.notify_packet_received = ""
        self.open_session_succeeded = ""
        self.connection_failed = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param session_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"session-id": {"type": "number", "format": "number"}, "connection-succeeded": {"type": "number", "format": "number"}, "sessions-dropped": {"type": "number", "format": "number"}, "retry": {"type": "number", "format": "number"}, "update-packet-sent": {"type": "number", "format": "number"}, "open-packet-received": {"type": "number", "format": "number"}, "protocol-info": {"type": "string", "format": "string"}, "keepalive-packet-received": {"type": "number", "format": "number"}, "update-packet-received": {"type": "number", "format": "number"}, "notify-packet-sent": {"type": "number", "format": "number"}, "open-packet-sent": {"type": "number", "format": "number"}, "state": {"type": "string", "format": "string"}, "keepalive-packet-sent": {"type": "number", "format": "number"}, "message-header-error": {"type": "number", "format": "number"}, "open-session-failed": {"type": "number", "format": "number"}, "notify-packet-received": {"type": "number", "format": "number"}, "optional": true, "open-session-succeeded": {"type": "number", "format": "number"}, "connection-failed": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.session_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Protocol(A10BaseClass):
    
    """Class Description::
    Operational Status for the object protocol.

    Class protocol supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/protocol/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "protocol"
        self.a10_url="/axapi/v3/gslb/protocol/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


