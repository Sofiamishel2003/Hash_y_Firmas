import hmac
import hashlib
import os

SECRET_KEY = os.urandom(32)


def sign_message(message: str, key: bytes) -> str:
    return hmac.new(
        key,
        message.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()


def verify_message(message: str, signature: str, key: bytes) -> bool:
    expected = sign_message(message, key)
    return hmac.compare_digest(expected, signature)


def main():
    payload = "user_id=42&action=transfer&amount=100"
    signature = sign_message(payload, SECRET_KEY)

    print("Mensaje original:", payload)
    print("Firma HMAC:", signature)
    print("Verificación correcta:", verify_message(payload, signature, SECRET_KEY))
    print(
        "Verificación alterada:",
        verify_message("user_id=42&action=transfer&amount=9999", signature, SECRET_KEY)
    )


if __name__ == "__main__":
    main()