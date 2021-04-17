import base64


def base64ToBinary(base64_str):
    base64_bytes = base64_str.encode("ascii")

    return base64.b64decode(base64_bytes)


def binaryToBase64(binary_data):
    base64_bytes = base64.b64encode(binary_data)

    return base64_bytes.decode("ascii")
