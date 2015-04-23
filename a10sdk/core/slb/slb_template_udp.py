from a10sdk.common.A10BaseClass import A10BaseClass


class Udp(A10BaseClass):
    
    """Class Description::
    L4 UDP switch config.

    Class udp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param short: {"description": "Short lived session", "format": "flag", "default": 0, "optional": true, "not": "immediate", "type": "number"}
    :param qos: {"description": "QOS level (number)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param name: {"description": "Fast UDP Template Name", "format": "string-rlx", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param age: {"optional": true, "minimum": 1, "type": "number", "maximum": 31, "format": "number"}
    :param stateless_conn_timeout: {"description": "Stateless Current Connection Timeout value (5 - 120 seconds) (idle timeout in second, default 120)", "format": "number", "default": 120, "optional": true, "maximum": 120, "minimum": 5, "type": "number"}
    :param idle_timeout: {"description": "Idle Timeout value (default 120 seconds) (idle timeout in second, default 120)", "format": "number", "default": 120, "optional": true, "maximum": 2097151, "minimum": 1, "type": "number"}
    :param re_select_if_server_down: {"default": 0, "optional": true, "type": "number", "description": "re-select another server if service port is down", "format": "flag"}
    :param immediate: {"description": "Immediate Removal after Transaction", "format": "flag", "default": 0, "optional": true, "not": "short", "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/udp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "udp"
        self.a10_url="/axapi/v3/slb/template/udp/{name}"
        self.DeviceProxy = ""
        self.short = ""
        self.qos = ""
        self.name = ""
        self.age = ""
        self.stateless_conn_timeout = ""
        self.idle_timeout = ""
        self.re_select_if_server_down = ""
        self.immediate = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


