import hashlib
import os
import sys


def hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def generar_manifiesto(paths, salida="SHA256SUMS.txt"):
    with open(salida, "w", encoding="utf-8") as out:
        for path in paths:
            if not os.path.isfile(path):
                print(f"[ADVERTENCIA] No existe: {path}")
                continue

            digest = hash_file(path)
            nombre = os.path.basename(path)
            out.write(f"{digest}  {nombre}\n")
            print(f"[OK] {nombre} -> {digest}")


if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Uso: python generar_manifiesto.py archivo1 archivo2 archivo3 archivo4 archivo5")
        sys.exit(1)

    generar_manifiesto(sys.argv[1:])