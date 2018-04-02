Anonymising email addresses in a file by hashing.
------

Input file layout should be: 
1. contact number
2. email
3. segmentation

Usage: python3 hash.py <source> <output> <algorithm>[optional]

If the output file exists it is cleared before the input file is processed.
If anonymise is set (default) the first two columns are removed during
processing.

SHA256 is the default but all algorithms available to hashlib are supported:
* DSA
* DSA-SHA
* MD4
* MD5
* MDC2
* RIPEMD160
* SHA
* SHA1
* SHA224
* SHA256
* SHA384
* SHA512
* blake2b
* blake2s
* dsaEncryption
* dsaWithSHA
* ecdsa-with-SHA1
* md4
* md5
* mdc2
* ripemd160
* sha
* sha1
* sha224
* sha256
* sha384
* sha3_224
* sha3_256
* sha3_384
* sha3_512
* sha512
* shake_128
* shake_256
* whirlpool
