# Laboratorio: Hashes y Firmas Digitales

## Autor
Sofía Velásquez

Universidad del Valle de Guatemala  
Cifrados de Información — 2026  

---

## Descripción del proyecto

Este laboratorio implementa mecanismos de seguridad aplicados al escenario de MediSoft S.A., empresa que distribuye software médico crítico.

Se desarrollan dos capas principales de protección:

1. **Integridad de distribución**  
   Uso de SHA-256 para verificar que los archivos descargados no han sido alterados.

2. **Autenticación y seguridad de usuarios**  
   Uso de Argon2id para almacenamiento seguro de contraseñas y HMAC-SHA256 para autenticación de mensajes.

Además, se implementa un sistema completo de firma digital usando RSA para garantizar la autenticidad del manifiesto de hashes.

---

## Objetivos cumplidos

- Propiedades de funciones hash (determinismo, avalancha, etc.)
- Uso correcto de algoritmos según el contexto
- Verificación de integridad con SHA-256
- Uso de firma digital (RSA)
- Uso de Argon2id con salt
- Uso de HMAC-SHA256
- Suite de pruebas con pytest

---

## Requisitos

- Python 3.10+
- requests
- pycryptodome
- argon2-cffi
- pytest

---

## Instalación

```bash
pip install requests pycryptodome argon2-cffi pytest
````

---

## Ejecución

### Flujo completo

```bash
python main.py
```

### Ejecución individual

```bash
python explorar_hashes.py
python hibp_passwords.py
python generar_manifiesto.py archivos_demo/*.txt
python verificar_paquete.py
python generar_claves_rsa.py
python firmar_manifiesto.py
python verificar_firma.py
python password_argon2_demo.py
python hmac_demo.py
pytest -v
```

---

## Estructura del proyecto

```
Hash_y_Firmas/
├── archivos_demo/
├── tests/
├── explorar_hashes.py
├── hibp_passwords.py
├── generar_manifiesto.py
├── verificar_paquete.py
├── generar_claves_rsa.py
├── firmar_manifiesto.py
├── verificar_firma.py
├── password_argon2_demo.py
├── hmac_demo.py
├── main.py
├── SHA256SUMS.txt
├── SHA256SUMS.sig
├── medisoft_priv.pem
├── medisoft_pub.pem
```

---

## Respuestas a preguntas

### 1. Efecto avalancha

Se compararon:

* `MediSoft-v2.1.0`
* `medisoft-v2.1.0`

El número de bits cambiados en SHA-256 es alto (120 bits).
![Resultado].(imagenes/explorar_hashes.png)

**Conclusión:**
Un cambio mínimo produce una gran diferencia en el hash → efecto avalancha.

---

### 2. Seguridad de MD5

MD5 produce hashes de 128 bits.

**Problemas:**

* Espacio de salida pequeño
* Colisiones conocidas
* Ataques prácticos existentes

**Conclusión:**
MD5 es inseguro para integridad en sistemas modernos.

---

### 3. Contraseñas y HIBP

Se evaluaron contraseñas comunes:

* `admin`
* `123456`
* `hospital`
* `medisoft2024`
  
![Resultado].(imagenes/generacion_claves.png)

Las primeras aparecen millones de veces en filtraciones.

**Conclusión:**
SHA-256 directo es inseguro para contraseñas por las coincidencias que encontramos en el mundo, cómo las personas utilizamos contraseñas similares, no sería muy dificil al ver esto.

---

### 4. Verificación de integridad

El sistema detecta modificaciones en archivos mediante SHA-256.

#### Prueba realizada:

* Se modificó un byte en un archivo
* Resultado: `ALTERADO`


**Conclusión:**
SHA-256 detecta cualquier cambio en los datos.

---

### 5. Firma digital

Se firmó el archivo `SHA256SUMS.txt` con RSA.

#### Prueba:

* Se modificó el manifiesto
* Resultado: `FIRMA INVÁLIDA`

![Resultado].(imagenes/test_firma.png)

**Conclusión:**
La firma garantiza autenticidad e integridad del manifiesto.

---

### 6. Pregunta clave del laboratorio

#### ¿Por qué la firma sigue siendo válida si se altera un archivo del paquete?

Porque la firma protege el archivo:

```
SHA256SUMS.txt
```

NO protege directamente los archivos del paquete.

---

#### ¿Qué pasa al ejecutar verificar_paquete.py?

![Resultado].(imagenes/test_paquetes.png)

* Detecta el archivo alterado
* Marca el sistema como `COMPROMETIDO`

---

### 7. Argon2id

Se implementó almacenamiento seguro de contraseñas:

* Salt automático
* Costos de memoria y tiempo
* Protección contra ataques de fuerza bruta

**Conclusión:**
Argon2id es el estándar moderno recomendado.

---

### 8. HMAC-SHA256

Se implementó autenticación segura de mensajes.

También se mostró el patrón inseguro:

```
H(secret || mensaje)
```

**Problema:**
Vulnerable a ataques criptográficos (ej. length extension)

**Conclusión:**
Se debe usar HMAC en lugar de hashes simples.

---

## Pruebas

```bash
pytest -v
```
![Resultado].(imagenes/test_hashes.png)

Todas las pruebas pasan correctamente.
