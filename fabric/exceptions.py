"""
Custom Fabric exception classes.

Most are simply distinct Exception subclasses for purposes of message-passing (though typically still in actual error situations.)
"""

class NetworkException(Exception):
    pass
