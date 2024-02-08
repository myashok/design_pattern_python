import json
from hashlib import md5
def _get_otp_digest(otp: str):
    return md5(str(otp).encode()).hexdigest()
print(_get_otp_digest("250571"))