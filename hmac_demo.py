import hashlib
import hmac
import os

SECRET_KEY = os.urandom(32)


def sign_message(message: str, key: bytes) -> str:
    return hmac.new(key, message.encode("utf-8"), hashlib.sha256).hexdigest()


def verify_message(message: str, signature: str, key: bytes) -> bool:
    expected = sign_message(message, key)
    return hmac.compare_digest(expected, signature)


def insecure_prefix_mac(message: str, key: bytes) -> str:
    return hashlib.sha256(key + message.encode("utf-8")).hexdigest()


def main():
    payload = "user_id=42&action=transfer&amount=100"
    sig = sign_message(payload, SECRET_KEY)

    print("=" * 100)
    print("AUTENTICACIÓN DE MENSAJES CON HMAC-SHA256")
    print("=" * 100)
    print("Mensaje:", payload)
    print("Firma HMAC:", sig)
    print("Verificación correcta:", verify_message(payload, sig, SECRET_KEY))
    print(
        "Verificación con mensaje alterado:",
        verify_message("user_id=42&action=transfer&amount=9999", sig, SECRET_KEY)
    )

    print("\n" + "=" * 100)
    print("DEMOSTRACIÓN DEL PATRÓN INSEGURO H(secret || mensaje)")
    print("=" * 100)
    bad_sig = insecure_prefix_mac(payload, SECRET_KEY)
    print("Firma insegura:", bad_sig)
    print(
        "Conclusión: este patrón no debe usarse para autenticar mensajes; se debe usar HMAC."
    )


if __name__ == "__main__":
    main()