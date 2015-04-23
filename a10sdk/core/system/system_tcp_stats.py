from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "connattempt", "connects", "drops", "conndrops", "closed", "segstimed", "rttupdated", "delack", "timeoutdrop", "rexmttimeo", "persisttimeo", "keeptimeo", "keepprobe", "keepdrops", "sndtotal", "sndpack", "sndbyte", "sndrexmitpack", "sndrexmitbyte", "sndrexmitbad", "sndacks", "sndprobe", "sndurg", "sndwinup", "sndctrl", "sndrst", "sndfin", "sndsyn", "rcvtotal", "rcvpack", "rcvbyte", "rcvbadoff", "rcvmemdrop", "rcvshort", "rcvduppack", "rcvdupbyte", "rcvpartduppack", "rcvpartdupbyte", "rcvoopack", "rcvoobyte", "rcvpackafterwin", "rcvbyteafterwin", "rcvwinprobe", "rcvdupack", "rcvacktoomuch", "rcvackpack", "rcvackbyte", "rcvwinupd", "pawsdrop", "predack", "preddat", "persistdrop", "mturesent", "badrst", "finwait2_drops", "sack_recovery_episode", "sack_rexmits", "sack_rexmit_bytes", "sack_rcv_blocks", "sack_send_blocks", "ecn_shs", "ecn_rcwnd"], "type": "string", "description": "'all': all; 'connattempt': Connect initiated; 'connects': Connect established; 'drops': Connect dropped; 'conndrops': Embryonic connect dropped; 'closed': Connect closed; 'segstimed': Segs to get RTT; 'rttupdated': Update RTT; 'delack': Delayed acks sent; 'timeoutdrop': Conn dropped in rxmt timeout; 'rexmttimeo': Retransmit timeout; 'persisttimeo': Persist timeout; 'keeptimeo': Keepalive timeout; 'keepprobe': Keepalive probe sent; 'keepdrops': Connect dropped in keepalive; 'sndtotal': Total packet sent; 'sndpack': Data packet sent; 'sndbyte': Data bytes sent; 'sndrexmitpack': Data packet retransmit; 'sndrexmitbyte': Data byte retransmit; 'sndrexmitbad': Unnecessary packet retransmit; 'sndacks': Ack packet sent; 'sndprobe': Window probe sent; 'sndurg': URG packet sent; 'sndwinup': Window update packet sent; 'sndctrl': SYN|FIN|RST packet sent; 'sndrst': RST packet sent; 'sndfin': FIN packet sent; 'sndsyn': SYN packet sent; 'rcvtotal': Total packet received; 'rcvpack': Packet received; 'rcvbyte': Bytes received; 'rcvbadoff': Packet received with bad offset; 'rcvmemdrop': Packet dropped for lack of memory; 'rcvshort': Packet received too short; 'rcvduppack': Duplicate packet received; 'rcvdupbyte': Duplicate bytes received; 'rcvpartduppack': Packet with some duplicate data; 'rcvpartdupbyte': Dup. bytes in part-dup. packets; 'rcvoopack': Out-of-order packet received; 'rcvoobyte': Out-of-order bytes received; 'rcvpackafterwin': Packets with data after window; 'rcvbyteafterwin': Bytes rcvd after window; 'rcvwinprobe': Rcvd window probe packet; 'rcvdupack': Rcvd duplicate acks; 'rcvacktoomuch': Rcvd acks for unsent data; 'rcvackpack': Rcvd ack packets; 'rcvackbyte': Bytes acked by rcvd acks; 'rcvwinupd': Rcvd window update packets; 'pawsdrop': Segments dropped due to PAWS; 'predack': Hdr predict for acks; 'preddat': Hdr predict for data pkts; 'persistdrop': Timeout in persist state; 'mturesent': Resends due to MTU discovery; 'badrst': Ignored RST; 'finwait2_drops': Drop FIN_WAIT_2 connection after time limit; 'sack_recovery_episode': SACK recovery episodes; 'sack_rexmits': SACK rexmit segments; 'sack_rexmit_bytes': SACK rexmit bytes; 'sack_rcv_blocks': SACK received; 'sack_send_blocks': SACK sent; 'ecn_shs': ECN successful handshakes; 'ecn_rcwnd': ECN reduced the cwnd; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TcpStats(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "connattempt", "connects", "drops", "conndrops", "closed", "segstimed", "rttupdated", "delack", "timeoutdrop", "rexmttimeo", "persisttimeo", "keeptimeo", "keepprobe", "keepdrops", "sndtotal", "sndpack", "sndbyte", "sndrexmitpack", "sndrexmitbyte", "sndrexmitbad", "sndacks", "sndprobe", "sndurg", "sndwinup", "sndctrl", "sndrst", "sndfin", "sndsyn", "rcvtotal", "rcvpack", "rcvbyte", "rcvbadoff", "rcvmemdrop", "rcvshort", "rcvduppack", "rcvdupbyte", "rcvpartduppack", "rcvpartdupbyte", "rcvoopack", "rcvoobyte", "rcvpackafterwin", "rcvbyteafterwin", "rcvwinprobe", "rcvdupack", "rcvacktoomuch", "rcvackpack", "rcvackbyte", "rcvwinupd", "pawsdrop", "predack", "preddat", "persistdrop", "mturesent", "badrst", "finwait2_drops", "sack_recovery_episode", "sack_rexmits", "sack_rexmit_bytes", "sack_rcv_blocks", "sack_send_blocks", "ecn_shs", "ecn_rcwnd"], "type": "string", "description": "'all': all; 'connattempt': Connect initiated; 'connects': Connect established; 'drops': Connect dropped; 'conndrops': Embryonic connect dropped; 'closed': Connect closed; 'segstimed': Segs to get RTT; 'rttupdated': Update RTT; 'delack': Delayed acks sent; 'timeoutdrop': Conn dropped in rxmt timeout; 'rexmttimeo': Retransmit timeout; 'persisttimeo': Persist timeout; 'keeptimeo': Keepalive timeout; 'keepprobe': Keepalive probe sent; 'keepdrops': Connect dropped in keepalive; 'sndtotal': Total packet sent; 'sndpack': Data packet sent; 'sndbyte': Data bytes sent; 'sndrexmitpack': Data packet retransmit; 'sndrexmitbyte': Data byte retransmit; 'sndrexmitbad': Unnecessary packet retransmit; 'sndacks': Ack packet sent; 'sndprobe': Window probe sent; 'sndurg': URG packet sent; 'sndwinup': Window update packet sent; 'sndctrl': SYN|FIN|RST packet sent; 'sndrst': RST packet sent; 'sndfin': FIN packet sent; 'sndsyn': SYN packet sent; 'rcvtotal': Total packet received; 'rcvpack': Packet received; 'rcvbyte': Bytes received; 'rcvbadoff': Packet received with bad offset; 'rcvmemdrop': Packet dropped for lack of memory; 'rcvshort': Packet received too short; 'rcvduppack': Duplicate packet received; 'rcvdupbyte': Duplicate bytes received; 'rcvpartduppack': Packet with some duplicate data; 'rcvpartdupbyte': Dup. bytes in part-dup. packets; 'rcvoopack': Out-of-order packet received; 'rcvoobyte': Out-of-order bytes received; 'rcvpackafterwin': Packets with data after window; 'rcvbyteafterwin': Bytes rcvd after window; 'rcvwinprobe': Rcvd window probe packet; 'rcvdupack': Rcvd duplicate acks; 'rcvacktoomuch': Rcvd acks for unsent data; 'rcvackpack': Rcvd ack packets; 'rcvackbyte': Bytes acked by rcvd acks; 'rcvwinupd': Rcvd window update packets; 'pawsdrop': Segments dropped due to PAWS; 'predack': Hdr predict for acks; 'preddat': Hdr predict for data pkts; 'persistdrop': Timeout in persist state; 'mturesent': Resends due to MTU discovery; 'badrst': Ignored RST; 'finwait2_drops': Drop FIN_WAIT_2 connection after time limit; 'sack_recovery_episode': SACK recovery episodes; 'sack_rexmits': SACK rexmit segments; 'sack_rexmit_bytes': SACK rexmit bytes; 'sack_rcv_blocks': SACK received; 'sack_send_blocks': SACK sent; 'ecn_shs': ECN successful handshakes; 'ecn_rcwnd': ECN reduced the cwnd; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show TCP Statistics.

    Class tcp-stats supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/tcp-stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tcp-stats"
        self.a10_url="/axapi/v3/system/tcp-stats"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


