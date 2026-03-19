import hashlib
import requests

PASSWORDS = ["admin", "123456", "hospital", "medisoft2024"]


def sha256_hex(texto: str) -> str:
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def sha1_hex(texto: str) -> str:
    return hashlib.sha1(texto.encode("utf-8")).hexdigest().upper()


def consultar_hibp(password: str) -> int:
    sha1 = sha1_hex(password)
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    headers = {"User-Agent": "UVG-Lab-Hashes"}

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    for line in response.text.splitlines():
        sufijo_api, count = line.split(":")
        if sufijo_api.strip().upper() == suffix:
            return int(count)

    return 0


def main():
    print("=" * 120)
    print(f"{'Password':15} {'SHA-256':66} {'SHA-1(HIBP)':45} {'Filtraciones'}")
    print("=" * 120)

    for password in PASSWORDS:
        sha256 = sha256_hex(password)
        sha1 = sha1_hex(password)
        count = consultar_hibp(password)

        print(f"{password:15} {sha256:66} {sha1:45} {count}")


if __name__ == "__main__":
    main()