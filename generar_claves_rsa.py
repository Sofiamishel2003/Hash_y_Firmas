from Crypto.PublicKey import RSA


def main():
    key = RSA.generate(2048)

    with open("medisoft_priv.pem", "wb") as f:
        f.write(key.export_key())

    with open("medisoft_pub.pem", "wb") as f:
        f.write(key.publickey().export_key())

    print("Claves generadas correctamente")


if __name__ == "__main__":
    main()