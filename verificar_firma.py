from Crypto.PublicKey import RSA
from Crypto.Signature import pss
from Crypto.Hash import SHA256


def verificar():
    with open("medisoft_pub.pem", "rb") as f:
        key = RSA.import_key(f.read())

    with open("SHA256SUMS.txt", "rb") as f:
        data = f.read()

    with open("SHA256SUMS.sig", "rb") as f:
        sig = f.read()

    h = SHA256.new(data)

    try:
        pss.new(key).verify(h, sig)
        print("FIRMA VÁLIDA")
    except:
        print("FIRMA INVÁLIDA")


if __name__ == "__main__":
    verificar()