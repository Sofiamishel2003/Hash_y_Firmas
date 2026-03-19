import hashlib


def test_sha256_deterministico():
    texto = "MediSoft-v2.1.0".encode("utf-8")
    h1 = hashlib.sha256(texto).hexdigest()
    h2 = hashlib.sha256(texto).hexdigest()
    assert h1 == h2

def test_efecto_avalancha_basico():
    a = hashlib.sha256(b"MediSoft-v2.1.0").digest()
    b = hashlib.sha256(b"medisoft-v2.1.0").digest()
    bits = sum(bin(x ^ y).count("1") for x, y in zip(a, b))
    assert bits > 80