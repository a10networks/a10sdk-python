# A10 Networks Python Client SDK

A10 github repos:

- [a10sdk-python](https://github.com/a10networks/a10sdk-python) - Full featured AxAPI client.
- [acos-client](https://github.com/a10networks/acos-client) - Alternate AxAPI client.

## Usage

In order to get a session ID for continued use we need to create a `DeviceProxy` object. The DeviceProxy class requires the hostname/IP, port, username, and password.

```python
from a10sdk.common.device_proxy import DeviceProxy
dp = DeviceProxy(host="10.48.5.181", port=443, username="admin", password="a10")
```

#### Example setting up an SLB:

To utilize the sdk you must import the modules for the objects you would like to manage.

```python
from a10sdk.core.slb.slb_virtual_server import VirtualServer
vs = VirtualServer(name='s1', ip_address="1.1.1.1", DeviceProxy=dp)
vs.create()
```

## Contributing

1. Fork it ( http://github.com/a10networks/a10sdk-python/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
