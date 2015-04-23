from a10sdk.common.A10BaseClass import A10BaseClass


class Monitor(A10BaseClass):
    
    """    :param data_cpu: {"description": "Monitor data CPU threshold (Threshold value in percentage, default 90)", "format": "number", "default": 90, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param conn_type0: {"description": "Conn resource type 0 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param buffer_usage: {"description": "Monitor IO buffer usage threshold (Threshold value)", "format": "number", "type": "number", "maximum": 4000000, "minimum": 60000, "optional": true}
    :param smp_type1: {"description": "SMP resource type 1 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param conn_type4: {"description": "Conn resource type 4 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param smp_type3: {"description": "SMP resource type 3 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param ctrl_cpu: {"description": "Monitor control CPU threshold (Threshold value in percentage, default 90)", "format": "number", "default": 90, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param warn_temp: {"description": "Monitor warning system temperature threshold (Threshold value in Celsius, default 68)", "format": "number", "default": 68, "optional": true, "maximum": 68, "minimum": 1, "type": "number"}
    :param smp_type2: {"description": "SMP resource type 2 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param memory: {"description": "Monitor memory usage threshold (Threshold value in percentage, default 95)", "format": "number", "default": 95, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param conn_type3: {"description": "Conn resource type 3 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param conn_type2: {"description": "Conn resource type 2 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param conn_type1: {"description": "Conn resource type 1 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param disk: {"description": "Monitor hard disk usage threshold (Threshold value in percentage, default 85)", "format": "number", "default": 85, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param smp_type0: {"description": "SMP resource type 0 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param smp_type4: {"description": "SMP resource type 4 (Threshold value, default 32767)", "format": "number", "default": 32767, "optional": true, "maximum": 256000000, "minimum": 32767, "type": "number"}
    :param buffer_drop: {"description": "Monitor buffer drop threshold (Threshold value)", "format": "number", "default": 4000, "optional": true, "maximum": 32767, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    System monitor configuration.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/monitor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "monitor"
        self.a10_url="/axapi/v3/monitor"
        self.DeviceProxy = ""
        self.data_cpu = ""
        self.conn_type0 = ""
        self.buffer_usage = ""
        self.smp_type1 = ""
        self.conn_type4 = ""
        self.smp_type3 = ""
        self.ctrl_cpu = ""
        self.uuid = ""
        self.warn_temp = ""
        self.smp_type2 = ""
        self.memory = ""
        self.conn_type3 = ""
        self.conn_type2 = ""
        self.conn_type1 = ""
        self.disk = ""
        self.smp_type0 = ""
        self.smp_type4 = ""
        self.buffer_drop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


