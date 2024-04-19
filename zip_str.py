import zlib

long_text = 'itilfc02244 8 16 23 8 19 2 15 11 17 20 6 21 21 3 19 10 3 1 17 22 13 17 14 17 22 21 12 1 16'
print('long_text', len(long_text))

long_text_compressed = zlib.compress(long_text.encode('utf-8'))

print('long_text_compressed', len(long_text_compressed))
print(long_text_compressed)
import base64

long_text_compressed_b64 = base64.b64encode(long_text_compressed)

print('long_text_compressed_b64', len(long_text_compressed_b64))

decoded_b64_text = base64.b64decode(long_text_compressed_b64)
undompressed_text = zlib.decompress(decoded_b64_text).decode('utf-8')

print(undompressed_text)