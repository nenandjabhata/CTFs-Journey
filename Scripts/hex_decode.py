import binascii

hex_string = b'445c8be33f9ccda8bb2880a8b2d8ff6a1bfb41917d9e890026'
#hex_string = 'ca06b0957d60b42bdc367c108409677ab2a2e5d7aff28a26d4522de5ec82a7f4c05fb9d2b0f4d1e83279f39e997d6f28c33879ef67baf2e6e8c4f4770813d949'
byte_string = binascii.unhexlify(hex_string)
print(byte_string)
