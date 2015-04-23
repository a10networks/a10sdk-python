from a10sdk.common.A10BaseClass import A10BaseClass


class SslModuleStats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_enabled_crypto_engines: {"type": "number", "description": "Number of enabled crypto engines", "format": "number"}
    :param requests_handled: {"type": "number", "description": "Number of requests handled", "format": "number"}
    :param ssl_modules_index: {"type": "number", "description": "SSL module index", "format": "number"}
    :param total_available_crypto_engines: {"type": "number", "description": "Number of available crypto engines", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ssl-module-stats"
        self.DeviceProxy = ""
        self.total_enabled_crypto_engines = ""
        self.requests_handled = ""
        self.ssl_modules_index = ""
        self.total_available_crypto_engines = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ssl_modules_count: {"type": "number", "description": "SSL module count", "format": "number"}
    :param max_ssl_contexts: {"type": "number", "description": "Maximum SSL contexts", "format": "number"}
    :param client_cert_auth_fail: {"type": "number", "description": "SSL client certificate authorization failed", "format": "number"}
    :param thales_hsm_status: {"enum": ["Enabled", "Disabled"], "type": "string", "description": "Thales HSM Status", "format": "enum"}
    :param current_serverside_connections: {"type": "number", "description": "Current serverside SSL connections", "format": "number"}
    :param failed_crypto: {"type": "number", "description": "Failed crypto operations", "format": "number"}
    :param total_reuse_server_ssl: {"type": "number", "description": "Total times of reusing SSL sessions(IDs) in server ssl", "format": "number"}
    :param hw_ring_full: {"type": "number", "description": "HW ring full", "format": "number"}
    :param current_clientside_connections: {"type": "number", "description": "Current clientside SSL connections", "format": "number"}
    :param total_clientside_connections: {"type": "number", "description": "Total clientside SSL connections", "format": "number"}
    :param clientssl_context_malloc_fail: {"type": "number", "description": "Total client ssl context malloc failures", "format": "number"}
    :param hw_context_alloc_fail: {"type": "number", "description": "HW Context Memory alloc failed", "format": "number"}
    :param ssl_memory_usage: {"type": "number", "description": "SSL memory usage", "format": "number"}
    :param hw_context_total: {"type": "number", "description": "HW Context Memory Total Count", "format": "number"}
    :param ssl_module_type: {"type": "string", "description": "SSL module", "format": "string"}
    :param curr_ssl_contexts: {"type": "number", "description": "Current SSL contexts in use", "format": "number"}
    :param server_cert_errors: {"type": "number", "description": "SSL server certificate errors", "format": "number"}
    :param total_reuse_client_ssl: {"type": "number", "description": "Total times of reusing SSL sessions(IDs) in client ssl", "format": "number"}
    :param failed_handshakes: {"type": "number", "description": "Failed SSL handshakes", "format": "number"}
    :param record_too_big: {"type": "number", "description": "Record too big", "format": "number"}
    :param config_module_type: {"type": "string", "description": "Number of SSL modules", "format": "string"}
    :param hw_context_usage: {"type": "number", "description": "HW Context Memory In Use", "format": "number"}
    :param total_serverside_connections: {"type": "number", "description": "Total serverside SSL connections", "format": "number"}
    :param ca_verification_failures: {"type": "number", "description": "SSL fail CA verification", "format": "number"}
    :param ssl_module_stats: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "total-enabled-crypto-engines": {"type": "number", "description": "Number of enabled crypto engines", "format": "number"}, "requests-handled": {"type": "number", "description": "Number of requests handled", "format": "number"}, "ssl-modules-index": {"type": "number", "description": "SSL module index", "format": "number"}, "total-available-crypto-engines": {"type": "number", "description": "Number of available crypto engines", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ssl_modules_count = ""
        self.max_ssl_contexts = ""
        self.client_cert_auth_fail = ""
        self.thales_hsm_status = ""
        self.current_serverside_connections = ""
        self.failed_crypto = ""
        self.total_reuse_server_ssl = ""
        self.hw_ring_full = ""
        self.current_clientside_connections = ""
        self.total_clientside_connections = ""
        self.clientssl_context_malloc_fail = ""
        self.hw_context_alloc_fail = ""
        self.ssl_memory_usage = ""
        self.hw_context_total = ""
        self.ssl_module_type = ""
        self.curr_ssl_contexts = ""
        self.server_cert_errors = ""
        self.total_reuse_client_ssl = ""
        self.failed_handshakes = ""
        self.record_too_big = ""
        self.config_module_type = ""
        self.hw_context_usage = ""
        self.total_serverside_connections = ""
        self.ca_verification_failures = ""
        self.ssl_module_stats = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SslStats(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ssl-stats.

    Class ssl-stats supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-stats/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-stats"
        self.a10_url="/axapi/v3/slb/ssl-stats/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


