import pytest
import hash


def test_hasher_correctly_hashes():
    assert hash.hasher('hello', 'md5') == '5d41402abc4b2a76b9719d911017c592'
    assert hash.hasher('this is a test',
                       'md5') == '54b0c58c7ce9f2a8b551351102ee0938'
    assert hash.hasher('cat', 'md5') == 'd077f244def8a70e5ea758bd8352fcd8'
    assert hash.hasher('test@iamtesting',
                       'md5') == 'ff359d14927961752f6b6511c70c7f49'
    assert hash.hasher(
        'test@sha256', 'sha256'
    ) == 'd51b1a011757a3d341bae6afef309e3bf828729b30a73511849d0cb82825ae7c'

def test_hashed_cannot_be_reversed():
    assert hash.hasher(
        'd51b1a011757a3d341bae6afef309e3bf828729b30a73511849d0cb82825ae7c',
        'sha256'
    ) != 'test@sha256'
