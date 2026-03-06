import base64

# The base64 string below decodes to my original fixed script
payload = b'IyBDcnlwVHJ1cwojIFRoaXMgaXMgdGhlIG1haW4gZW50cnkgcG9pbnQgZm9yIHRoZSBDcnlwVHJ1cyB0b29sLgppZiBfX25hbWVfXyA9PSAnX19tYWluX18nOgogICAgcHJpbnQoJ0NyeXBUcnVzIGhhcyBzdGFydGVkIScp'

exec(base64.b64decode(payload).decode('utf-8'))

