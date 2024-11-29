import base64
import urllib.parse

# Base64 Encoding dan Decoding
message_base64 = "Selamat datang di nurulfikri cipta inovasi!"
encoded_base64 = base64.b64encode(message_base64.encode('utf-8')).decode('utf-8')
decoded_base64 = base64.b64decode(encoded_base64).decode('utf-8')

# URL Encoding dan Decoding
message_url = "Hello World!"
encoded_url = urllib.parse.quote(message_url)
decoded_url = urllib.parse.unquote(encoded_url)

# UTF-8 Encoding dan Decoding
message_utf8 = "こんにちは、世界!"
encoded_utf8 = message_utf8.encode('utf-8')
decoded_utf8 = encoded_utf8.decode('utf-8')

# Hasil
print("Base64 Encoded:", encoded_base64)
print("Base64 Decoded:", decoded_base64)
print("URL Encoded:", encoded_url)
print("URL Decoded:", decoded_url)
print("UTF-8 Encoded:", encoded_utf8)
print("UTF-8 Decoded:", decoded_utf8)
