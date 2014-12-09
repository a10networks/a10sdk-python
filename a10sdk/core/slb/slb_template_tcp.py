from a10sdk.common.A10BaseClass import A10BaseClass


class Tcp(A10BaseClass):
    
    """Class Description::
    L4 TCP switch config.

    Class tcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param initial_window_size: {"description": "Set the initial window size (number)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param alive_if_active: {"default": 0, "optional": true, "type": "number", "description": "keep connection alive if active traffic", "format": "flag"}
    :param qos: {"description": "QOS level (number)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param name: {"description": "Fast TCP Template Name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param reset_fwd: {"default": 0, "optional": true, "type": "number", "description": "send reset to server if error happens", "format": "flag"}
    :param half_open_idle_timeout: {"description": "TCP Half Open Idle Timeout (sec), default off (half open idle timeout in second, default off)", "format": "number", "type": "number", "maximum": 60, "minimum": 1, "optional": true}
    :param idle_timeout: {"description": "Idle Timeout value (default 120 seconds) (idle timeout in second, default 120)", "format": "number", "type": "number", "maximum": 2097151, "minimum": 1, "optional": true}
    :param force_delete_timeout: {"description": "The maximum time that a session can stay in the system before being delete (number (second))", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "not": "force-delete-timeout-100ms", "type": "number"}
    :param lan_fast_ack: {"default": 0, "optional": true, "type": "number", "description": "Enable fast TCP ack on LAN", "format": "flag"}
    :param insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert client ip into TCP option", "format": "flag"}
    :param reset_rev: {"default": 0, "optional": true, "type": "number", "description": "send reset to client if error happens", "format": "flag"}
    :param force_delete_timeout_100ms: {"description": "The maximum time that a session can stay in the system before being delete (number in 100ms)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "not": "force-delete-timeout", "type": "number"}
    :param half_close_idle_timeout: {"description": "TCP Half Close Idle Timeout (sec), default off (half close idle timeout in second, default off)", "format": "number", "type": "number", "maximum": 120, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/tcp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "tcp"
        self.a10_url="/axapi/v3/slb/template/tcp/{name}"
        self.DeviceProxy = ""
        self.initial_window_size = ""
        self.alive_if_active = ""
        self.qos = ""
        self.name = ""
        self.reset_fwd = ""
        self.half_open_idle_timeout = ""
        self.idle_timeout = ""
        self.force_delete_timeout = ""
        self.lan_fast_ack = ""
        self.insert_client_ip = ""
        self.reset_rev = ""
        self.force_delete_timeout_100ms = ""
        self.half_close_idle_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


