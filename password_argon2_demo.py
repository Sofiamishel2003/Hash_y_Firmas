from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536,
    parallelism=4,
    hash_len=32,
    salt_len=16
)


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(stored_hash: str, password: str):
    try:
        ph.verify(stored_hash, password)

        if ph.check_needs_rehash(stored_hash):
            return True, hash_password(password)

        return True, None
    except VerifyMismatchError:
        return False, None


def main():
    password = "medisoft2024"
    stored_hash = hash_password(password)

    print("Hash generado con Argon2id:")
    print(stored_hash)

    ok, new_hash = verify_password(stored_hash, password)
    print("Verificación correcta:", ok)
    print("Rehash necesario:", new_hash is not None)

    ok2, _ = verify_password(stored_hash, "incorrecta")
    print("Verificación con contraseña incorrecta:", ok2)


if __name__ == "__main__":
    main()