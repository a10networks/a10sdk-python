from a10sdk.common.A10BaseClass import A10BaseClass


class ActionCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param conform: {"default": 0, "type": "number", "description": "packets that conform the limitation", "format": "flag"}
    :param exceed: {"default": 0, "type": "number", "description": "packets that exceed the limitation", "format": "flag"}
    :param exceed_dscpenum: {"not": "exceed-dscpnum", "enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef"], "type": "string", "description": "'af11': af11; 'af12': af12; 'af13': af13; 'af21': af21; 'af22': af22; 'af23': af23; 'af31': af31; 'af32': af32; 'af33': af33; 'af41': af41; 'af42': af42; 'af43': af43; 'cs1': cs1; 'cs2': cs2; 'cs3': cs3; 'cs4': cs4; 'cs5': cs5; 'cs6': cs6; 'cs7': cs7; 'ef': ef; ", "format": "enum"}
    :param dscpnum: {"not": "dscpenum", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}
    :param fifo: {"default": 0, "type": "number", "description": "First-in-first-out queueing", "format": "flag"}
    :param exceed_set_dscp: {"default": 0, "not": "limit-drop", "type": "number", "description": "Set DSCP then forward the packet", "format": "flag"}
    :param bandwidth: {"default": 0, "not": "drop", "type": "number", "description": "Bandwidth reservation, and need bandwidth control enabled", "format": "flag"}
    :param interval: {"description": "Pertubation interval in seconds", "format": "number", "default": 10, "maximum": 60, "minimum": 1, "type": "number"}
    :param threshold: {"description": "Minimum packet threshold of the RED queue", "format": "number", "default": 4, "maximum": 512, "minimum": 1, "type": "number"}
    :param min: {"description": "Minimum bandwidth in Kbps", "minimum": 0, "type": "number", "maximum": 1000000000, "format": "number"}
    :param limit_dscpenum: {"not": "limit-dscpnum", "enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef"], "type": "string", "description": "'af11': af11; 'af12': af12; 'af13': af13; 'af21': af21; 'af22': af22; 'af23': af23; 'af31': af31; 'af32': af32; 'af33': af33; 'af41': af41; 'af42': af42; 'af43': af43; 'cs1': cs1; 'cs2': cs2; 'cs3': cs3; 'cs4': cs4; 'cs5': cs5; 'cs6': cs6; 'cs7': cs7; 'ef': ef; ", "format": "enum"}
    :param length: {"description": "Maximum number of packets in a FIFO", "format": "number", "default": 16, "maximum": 512, "minimum": 1, "type": "number"}
    :param mark: {"default": 0, "not": "drop", "type": "number", "description": "packet marking action", "format": "flag"}
    :param priority: {"description": "Queuing Priority", "minimum": 0, "type": "number", "maximum": 7, "format": "number"}
    :param tail: {"default": 0, "not": "red", "type": "number", "description": "Drop packets when the queue is full", "format": "flag"}
    :param policy: {"description": "Child policy name", "format": "string", "minLength": 1, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/qos/policy"}
    :param red: {"default": 0, "not": "tail", "type": "number", "description": "drop packets using random early drop algorithm", "format": "flag"}
    :param limit_drop: {"default": 0, "not": "exceed-set-dscp", "type": "number", "description": "Drop the packet that exceed limitation", "format": "flag"}
    :param max: {"description": "Maximum bandwidth in Kbps", "minimum": 0, "type": "number", "maximum": 1000000000, "format": "number"}
    :param dscp: {"default": 0, "type": "number", "description": "DSCP marking", "format": "flag"}
    :param sfq: {"default": 0, "type": "number", "description": "Statistical fair queueing", "format": "flag"}
    :param drop_method: {"default": 0, "type": "number", "description": "Bandwidth drop method", "format": "flag"}
    :param limit_dscpnum: {"not": "limit-dscpenum", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}
    :param dscpenum: {"not": "dscpnum", "enum": ["af11", "af12", "af13", "af21", "af22", "af23", "af31", "af32", "af33", "af41", "af42", "af43", "cs1", "cs2", "cs3", "cs4", "cs5", "cs6", "cs7", "ef"], "type": "string", "description": "'af11': af11; 'af12': af12; 'af13': af13; 'af21': af21; 'af22': af22; 'af23': af23; 'af31': af31; 'af32': af32; 'af33': af33; 'af41': af41; 'af42': af42; 'af43': af43; 'cs1': cs1; 'cs2': cs2; 'cs3': cs3; 'cs4': cs4; 'cs5': cs5; 'cs6': cs6; 'cs7': cs7; 'ef': ef; ", "format": "enum"}
    :param exceed_dscpnum: {"not": "exceed-dscpenum", "minimum": 1, "type": "number", "maximum": 63, "format": "number"}
    :param drop: {"default": 0, "not-list": ["limit", "mark", "bandwidth"], "type": "number", "description": "Drop packet action", "format": "flag"}
    :param bucket: {"description": "Number of hash buckets", "format": "number", "default": 16, "maximum": 64, "minimum": 1, "type": "number"}
    :param queue: {"default": 0, "type": "number", "description": "configure bandwidth queue type", "format": "flag"}
    :param limit_rate: {"description": "Rate limit in Kbps", "minimum": 0, "type": "number", "maximum": 1000000000, "format": "number"}
    :param limit: {"default": 0, "not": "drop", "type": "number", "description": "Rate limit action", "format": "flag"}
    :param sfq_length: {"description": "Maximum number of packets in a bucket", "format": "number", "default": 16, "maximum": 128, "minimum": 1, "type": "number"}
    :param set_dscp: {"default": 0, "type": "number", "description": "Set DSCP before forward the packet", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "action-cfg"
        self.DeviceProxy = ""
        self.conform = ""
        self.exceed = ""
        self.exceed_dscpenum = ""
        self.dscpnum = ""
        self.fifo = ""
        self.exceed_set_dscp = ""
        self.bandwidth = ""
        self.interval = ""
        self.threshold = ""
        self.A10WW_min = ""
        self.limit_dscpenum = ""
        self.length = ""
        self.mark = ""
        self.priority = ""
        self.tail = ""
        self.policy = ""
        self.red = ""
        self.limit_drop = ""
        self.A10WW_max = ""
        self.dscp = ""
        self.sfq = ""
        self.drop_method = ""
        self.limit_dscpnum = ""
        self.dscpenum = ""
        self.exceed_dscpnum = ""
        self.drop = ""
        self.bucket = ""
        self.queue = ""
        self.limit_rate = ""
        self.limit = ""
        self.sfq_length = ""
        self.set_dscp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "current-rate", "everage-rate", "peak-rate", "bytes", "packets", "dropped-bytes", "dropped-packets", "active-session", "total-session", "dropped-session", "conform-packets", "exceed-packets", "bandwidth-bytes", "bandwidth-packets", "bandwidth-queue-bytes", "bandwidth-queue-packets", "bandwidth-dropped-bytes", "bandwidth-dropped-packets", "bandwidth-red-dropped-bytes", "bandwidth-red-dropped-packets"], "type": "string", "description": "'all': all; 'current-rate': current-rate; 'everage-rate': everage-rate; 'peak-rate': peak-rate; 'bytes': bytes; 'packets': packets; 'dropped-bytes': dropped-bytes; 'dropped-packets': dropped-packets; 'active-session': active-session; 'total-session': total-session; 'dropped-session': dropped-session; 'conform-packets': conform-packets; 'exceed-packets': exceed-packets; 'bandwidth-bytes': bandwidth-bytes; 'bandwidth-packets': bandwidth-packets; 'bandwidth-queue-bytes': bandwidth-queue-bytes; 'bandwidth-queue-packets': bandwidth-queue-packets; 'bandwidth-dropped-bytes': bandwidth-dropped-bytes; 'bandwidth-dropped-packets': bandwidth-dropped-packets; 'bandwidth-red-dropped-bytes': bandwidth-red-dropped-bytes; 'bandwidth-red-dropped-packets': bandwidth-red-dropped-packets; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Class(A10BaseClass):
    
    """Class Description::
    Configure class in policy.

    Class class supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "current-rate", "everage-rate", "peak-rate", "bytes", "packets", "dropped-bytes", "dropped-packets", "active-session", "total-session", "dropped-session", "conform-packets", "exceed-packets", "bandwidth-bytes", "bandwidth-packets", "bandwidth-queue-bytes", "bandwidth-queue-packets", "bandwidth-dropped-bytes", "bandwidth-dropped-packets", "bandwidth-red-dropped-bytes", "bandwidth-red-dropped-packets"], "type": "string", "description": "'all': all; 'current-rate': current-rate; 'everage-rate': everage-rate; 'peak-rate': peak-rate; 'bytes': bytes; 'packets': packets; 'dropped-bytes': dropped-bytes; 'dropped-packets': dropped-packets; 'active-session': active-session; 'total-session': total-session; 'dropped-session': dropped-session; 'conform-packets': conform-packets; 'exceed-packets': exceed-packets; 'bandwidth-bytes': bandwidth-bytes; 'bandwidth-packets': bandwidth-packets; 'bandwidth-queue-bytes': bandwidth-queue-bytes; 'bandwidth-queue-packets': bandwidth-queue-packets; 'bandwidth-dropped-bytes': bandwidth-dropped-bytes; 'bandwidth-dropped-packets': bandwidth-dropped-packets; 'bandwidth-red-dropped-bytes': bandwidth-red-dropped-bytes; 'bandwidth-red-dropped-packets': bandwidth-red-dropped-packets; ", "format": "enum"}}}]}
    :param name: {"description": "class name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param precedence: {"description": "Precedence in the policy", "format": "number", "default": 10, "optional": true, "maximum": 10, "minimum": 0, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/qos/policy/{name}/class/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "class"
        self.a10_url="/axapi/v3/qos/policy/{name}/class/{name}"
        self.DeviceProxy = ""
        self.action_cfg = {}
        self.sampling_enable = []
        self.name = ""
        self.precedence = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


