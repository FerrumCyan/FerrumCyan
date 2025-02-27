import base64

def encrypt_string(string):
    string_bytes = string.encode('utf-8')
    base64_bytes = base64.b64encode(string_bytes)
    return base64_bytes.decode('utf-8')

def decrypt_string(string):
    base64_bytes = string.encode('utf-8')
    string_bytes = base64.b64decode(base64_bytes)
    return string_bytes.decode('utf-8')

string = input('请输入要加密的字符串：')
encrypted_string = encrypt_string(string)

print(f'原始字符串：{string}')
print(f'加密后的字符串：{encrypted_string}')
