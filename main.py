from pathlib import Path

import explorar_hashes
import hibp_passwords
import generar_manifiesto
import verificar_paquete
import generar_claves_rsa
import firmar_manifiesto
import verificar_firma


def obtener_archivos_demo(carpeta: str = "archivos_demo") -> list[str]:
    ruta = Path(carpeta)
    if not ruta.exists():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta}")

    archivos = sorted(
        [str(p) for p in ruta.iterdir() if p.is_file()]
    )

    if len(archivos) < 5:
        raise ValueError("Se requieren al menos 5 archivos en archivos_demo.")

    return archivos


def main():
    print("\n" + "=" * 120)
    print("1. COMPARACIÓN DE ALGORITMOS HASH")
    print("=" * 120)
    explorar_hashes.main()

    print("\n" + "=" * 120)
    print("2. CONSULTA DE CONTRASEÑAS EN HIBP")
    print("=" * 120)
    hibp_passwords.main()

    print("\n" + "=" * 120)
    print("3. GENERACIÓN DE MANIFIESTO SHA-256")
    print("=" * 120)
    archivos = obtener_archivos_demo()
    generar_manifiesto.generar_manifiesto(archivos)

    print("\n" + "=" * 120)
    print("4. VERIFICACIÓN DE INTEGRIDAD DEL PAQUETE")
    print("=" * 120)
    verificar_paquete.verificar()

    print("\n" + "=" * 120)
    print("5. GENERACIÓN DE CLAVES RSA")
    print("=" * 120)
    generar_claves_rsa.main()

    print("\n" + "=" * 120)
    print("6. FIRMA DEL MANIFIESTO")
    print("=" * 120)
    firmar_manifiesto.firmar()

    print("\n" + "=" * 120)
    print("7. VERIFICACIÓN DE FIRMA")
    print("=" * 120)
    verificar_firma.verificar()

    print("\n" + "=" * 120)
    print("FLUJO COMPLETADO")
if __name__ == "__main__":
    main()