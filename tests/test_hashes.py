import os
import sys
import tempfile
from pathlib import Path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from explorar_hashes import hash_text, contar_bits_distintos
from generar_manifiesto import hash_file
from password_argon2_demo import hash_password, verify_password
from hmac_demo import sign_message, verify_message



def test_sha256_deterministico():
    texto = "MediSoft-v2.1.0"
    h1 = hash_text(texto, "sha256")
    h2 = hash_text(texto, "sha256")
    assert h1 == h2


def test_efecto_avalancha():
    h1 = hash_text("MediSoft-v2.1.0", "sha256")
    h2 = hash_text("medisoft-v2.1.0", "sha256")
    bits = contar_bits_distintos(h1, h2)
    assert bits > 80


def test_sha256_longitud_hex():
    h = hash_text("MediSoft-v2.1.0", "sha256")
    assert len(h) == 64


def test_hash_archivo_cambia_si_cambia_contenido():
    with tempfile.TemporaryDirectory() as tmp:
        ruta = Path(tmp) / "archivo.txt"
        ruta.write_text("hola", encoding="utf-8")
        h1 = hash_file(str(ruta))

        ruta.write_text("hola mundo", encoding="utf-8")
        h2 = hash_file(str(ruta))

        assert h1 != h2


def test_hmac_valido_e_invalido():
    key = b"clave_super_secreta_123456789012"
    msg = "hola"
    sig = sign_message(msg, key)
    assert verify_message(msg, sig, key) is True
    assert verify_message("hola2", sig, key) is False


def test_argon2_verifica_password():
    stored = hash_password("medisoft2024")
    ok, _ = verify_password(stored, "medisoft2024")
    bad, _ = verify_password(stored, "incorrecta")
    assert ok is True
    assert bad is False