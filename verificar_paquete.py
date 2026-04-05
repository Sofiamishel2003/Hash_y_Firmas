import hashlib
import hmac
import os
import sys


def hash_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cargar_manifiesto(manifiesto="SHA256SUMS.txt"):
    esperados = {}
    with open(manifiesto, "r", encoding="utf-8") as f:
        for line in f:
            partes = line.strip().split()
            if len(partes) >= 2:
                esperados[partes[1]] = partes[0]
    return esperados


def verificar(manifiesto="SHA256SUMS.txt", carpeta="archivos_demo"):
    esperados = cargar_manifiesto(manifiesto)

    print("=" * 100)
    print(f"{'Archivo':25} {'Estado'}")
    print("=" * 100)

    todo_ok = True

    for nombre, esperado in esperados.items():
        ruta = os.path.join(carpeta, nombre)

        if not os.path.exists(ruta):
            print(f"{nombre:25} FALTA")
            todo_ok = False
            continue

        actual = hash_file(ruta)

        if hmac.compare_digest(actual, esperado):
            print(f"{nombre:25} OK")
        else:
            print(f"{nombre:25} ALTERADO")
            todo_ok = False

    print("=" * 100)
    print("RESULTADO:", "ÍNTEGRO" if todo_ok else "COMPROMETIDO")


if __name__ == "__main__":
    verificar()