import hashlib

TEXTOS = ["MediSoft-v2.1.0", "medisoft-v2.1.0"]


def hash_text(texto: str, algoritmo: str) -> str:
    if algoritmo == "md5":
        return hashlib.md5(texto.encode("utf-8")).hexdigest()
    elif algoritmo == "sha1":
        return hashlib.sha1(texto.encode("utf-8")).hexdigest()
    elif algoritmo == "sha256":
        return hashlib.sha256(texto.encode("utf-8")).hexdigest()
    elif algoritmo == "sha3_256":
        return hashlib.sha3_256(texto.encode("utf-8")).hexdigest()
    else:
        raise ValueError(f"Algoritmo no soportado: {algoritmo}")


def contar_bits_distintos(hash1_hex: str, hash2_hex: str) -> int:
    b1 = bytes.fromhex(hash1_hex)
    b2 = bytes.fromhex(hash2_hex)
    xor_result = bytes(a ^ b for a, b in zip(b1, b2))
    return sum(bin(byte).count("1") for byte in xor_result)


def main():
    algoritmos = [
        ("MD5", "md5", 128),
        ("SHA-1", "sha1", 160),
        ("SHA-256", "sha256", 256),
        ("SHA3-256", "sha3_256", 256),
    ]

    print("=" * 120)
    print(f"{'Texto':20} {'Algoritmo':12} {'Bits':6} {'Hex Len':8} {'Hash'}")
    print("=" * 120)

    resultados = {}

    for texto in TEXTOS:
        resultados[texto] = {}
        for nombre, alg, bits in algoritmos:
            h = hash_text(texto, alg)
            resultados[texto][alg] = h
            print(f"{texto:20} {nombre:12} {bits:<6} {len(h):<8} {h}")

    sha256_a = resultados["MediSoft-v2.1.0"]["sha256"]
    sha256_b = resultados["medisoft-v2.1.0"]["sha256"]
    bits_cambiados = contar_bits_distintos(sha256_a, sha256_b)

    print("\n" + "=" * 120)
    print("ANÁLISIS")
    print("=" * 120)
    print(f"SHA-256 original : {sha256_a}")
    print(f"SHA-256 alterado : {sha256_b}")
    print(f"Bits diferentes  : {bits_cambiados}")
    print("Propiedad demostrada: efecto avalancha.")


if __name__ == "__main__":
    main()