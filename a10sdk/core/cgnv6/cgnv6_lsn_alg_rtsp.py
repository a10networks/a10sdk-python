from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "streams-created", "streams-freed", "stream-creation-failure", "ports-allocated", "ports-freed", "port-allocation-failure", "unknown-client-port-from-server", "data-session-created", "data-session-freed", "no-session-mem", "ha-sent", "ha-rcv", "smp-inserted", "smp-removed", "smp-reused", "nat-pool-standby", "smp-deleted", "control-closed", "data-session-exists", "data-session-creation-failure", "rtp-reversed", "rtcp-reversed", "cross-cpu-sent", "cross-cpu-rcv", "cross-cpu-no-session", "cross-cpu-created", "cross-cpu-rcv-failure", "data-free-smp-retry-lookup", "data-free-smp-not-found", "ha-streams-sent", "ha-streams-rcv", "ha-stream-incompatible", "ha-stream-exists", "ha-port-allocation-failure", "ha-data-session-sent", "ha-data-session-rcv", "ha-data-no-smp", "ha-control-closed", "ha-data-exists", "ha-extension-failure", "ha-stream-smp-reused", "ha-stream-smp-acquire-failure", "smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'streams-created': Streams Created; 'streams-freed': Streams Freed; 'stream-creation-failure': Stream Creation Failures; 'ports-allocated': Stream Client Ports Allocated; 'ports-freed': Stream Client Ports Freed; 'port-allocation-failure': Stream Client Port Allocation Failures; 'unknown-client-port-from-server': Server Replies With Unknown Client Ports; 'data-session-created': Data Session Created; 'data-session-freed': Data Session Freed; 'no-session-mem': Data Session Creation Failures; 'ha-sent': HA Sent; 'ha-rcv': HA RCV; 'smp-inserted': SMP Session Inserted; 'smp-removed': SMP Session Removed; 'smp-reused': SMP Session Reused; 'nat-pool-standby': New Session NAT Pool Standby; 'smp-deleted': New Session SMP Already Deleted; 'control-closed': New Session Closed; 'data-session-exists': New Session Already Exists; 'data-session-creation-failure': New Data Session Creation Failure; 'rtp-reversed': RTP Reverse Creation; 'rtcp-reversed': RTCP Reverse Creation; 'cross-cpu-sent': Cross CPU Sent; 'cross-cpu-rcv': Cross CPU Received; 'cross-cpu-no-session': Cross CPU No Session Found; 'cross-cpu-created': Cross CPU Creation; 'cross-cpu-rcv-failure': Cross CPU Receive Failure; 'data-free-smp-retry-lookup': Data Session Free SMP Retry Lookup; 'data-free-smp-not-found': Data Session Free SMP Not Found; 'ha-streams-sent': HA Streams Sent; 'ha-streams-rcv': HA Streams Received; 'ha-stream-incompatible': HA Incompatible Streams Received; 'ha-stream-exists': HA Stream Already Exists; 'ha-port-allocation-failure': HA Stream Port Allocation Failure; 'ha-data-session-sent': HA Data Session Sent; 'ha-data-session-rcv': HA Data Session Received; 'ha-data-no-smp': HA Data Session SMP Not Found; 'ha-control-closed': HA New Data Control Session Closed; 'ha-data-exists': HA New Data Session Already Exists; 'ha-extension-failure': HA Conn Extension Failure; 'ha-stream-smp-reused': HA SMP Session Reused; 'ha-stream-smp-acquire-failure': HA SMP Session Acquire Failure; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rtsp(A10BaseClass):
    
    """    :param rtsp_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable RTSP ALG for LSN; ", "format": "enum"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "streams-created", "streams-freed", "stream-creation-failure", "ports-allocated", "ports-freed", "port-allocation-failure", "unknown-client-port-from-server", "data-session-created", "data-session-freed", "no-session-mem", "ha-sent", "ha-rcv", "smp-inserted", "smp-removed", "smp-reused", "nat-pool-standby", "smp-deleted", "control-closed", "data-session-exists", "data-session-creation-failure", "rtp-reversed", "rtcp-reversed", "cross-cpu-sent", "cross-cpu-rcv", "cross-cpu-no-session", "cross-cpu-created", "cross-cpu-rcv-failure", "data-free-smp-retry-lookup", "data-free-smp-not-found", "ha-streams-sent", "ha-streams-rcv", "ha-stream-incompatible", "ha-stream-exists", "ha-port-allocation-failure", "ha-data-session-sent", "ha-data-session-rcv", "ha-data-no-smp", "ha-control-closed", "ha-data-exists", "ha-extension-failure", "ha-stream-smp-reused", "ha-stream-smp-acquire-failure", "smp-app-type-mismatch"], "type": "string", "description": "'all': all; 'streams-created': Streams Created; 'streams-freed': Streams Freed; 'stream-creation-failure': Stream Creation Failures; 'ports-allocated': Stream Client Ports Allocated; 'ports-freed': Stream Client Ports Freed; 'port-allocation-failure': Stream Client Port Allocation Failures; 'unknown-client-port-from-server': Server Replies With Unknown Client Ports; 'data-session-created': Data Session Created; 'data-session-freed': Data Session Freed; 'no-session-mem': Data Session Creation Failures; 'ha-sent': HA Sent; 'ha-rcv': HA RCV; 'smp-inserted': SMP Session Inserted; 'smp-removed': SMP Session Removed; 'smp-reused': SMP Session Reused; 'nat-pool-standby': New Session NAT Pool Standby; 'smp-deleted': New Session SMP Already Deleted; 'control-closed': New Session Closed; 'data-session-exists': New Session Already Exists; 'data-session-creation-failure': New Data Session Creation Failure; 'rtp-reversed': RTP Reverse Creation; 'rtcp-reversed': RTCP Reverse Creation; 'cross-cpu-sent': Cross CPU Sent; 'cross-cpu-rcv': Cross CPU Received; 'cross-cpu-no-session': Cross CPU No Session Found; 'cross-cpu-created': Cross CPU Creation; 'cross-cpu-rcv-failure': Cross CPU Receive Failure; 'data-free-smp-retry-lookup': Data Session Free SMP Retry Lookup; 'data-free-smp-not-found': Data Session Free SMP Not Found; 'ha-streams-sent': HA Streams Sent; 'ha-streams-rcv': HA Streams Received; 'ha-stream-incompatible': HA Incompatible Streams Received; 'ha-stream-exists': HA Stream Already Exists; 'ha-port-allocation-failure': HA Stream Port Allocation Failure; 'ha-data-session-sent': HA Data Session Sent; 'ha-data-session-rcv': HA Data Session Received; 'ha-data-no-smp': HA Data Session SMP Not Found; 'ha-control-closed': HA New Data Control Session Closed; 'ha-data-exists': HA New Data Session Already Exists; 'ha-extension-failure': HA Conn Extension Failure; 'ha-stream-smp-reused': HA SMP Session Reused; 'ha-stream-smp-acquire-failure': HA SMP Session Acquire Failure; 'smp-app-type-mismatch': SMP ALG App Type Mismatch; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Change LSN RTSP ALG Settings.

    Class rtsp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/rtsp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rtsp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/rtsp"
        self.DeviceProxy = ""
        self.rtsp_value = ""
        self.sampling_enable = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


