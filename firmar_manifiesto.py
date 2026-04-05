from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256


def firmar():
    with open("medisoft_priv.pem", "rb") as f:
        key = RSA.import_key(f.read())

    with open("SHA256SUMS.txt", "rb") as f:
        data = f.read()

    h = SHA256.new(data)
    signature = pss.new(key).sign(h)

    with open("SHA256SUMS.sig", "wb") as f:
        f.write(signature)

    print("Manifiesto firmado")


if __name__ == "__main__":
    firmar()