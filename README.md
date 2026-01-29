# Algoritmo de Fuerza Bruta Controlada

##  Descripción
Este proyecto implementa un algoritmo simple de fuerza bruta en Python con fines educativos, cuyo objetivo es demostrar la vulnerabilidad de las contraseñas débiles y la importancia de aplicar políticas de seguridad adecuadas.

El programa intenta adivinar una contraseña ingresada por el usuario probando todas las combinaciones posibles de caracteres a partir de un alfabeto que incluye letras mayúsculas, minúsculas, números y símbolos.

---

## Requisitos
- Python 3.x
- Editor de código (VSCode recomendado)
- Terminal o consola

---

## Cómo ejecutar el programa

# 1. Clonar el repositorio:
   ```
   git clone https://github.com/mateovivas453-dot/Algoritmo-simple-para-romper-contrase-as-fuerza-bruta-controlada.git

   ```

# 2. Ingresar al directorio del proyecto: con el comando 
 ```
cd  Algoritmo-simple-para-romper-contrase-as-fuerza-bruta-controlada

```
# 3. ejecutar el archivo con el comando :
 ```

python .\bruteforce.py

```

### Resulatados 

# 1. Ejecucion esperada :
<img width="698" height="84" alt="image" src="https://github.com/user-attachments/assets/bbda77dd-75bf-4948-88a1-e1429887f31c" />

Solicitud de una contraseña y la longitud de la misma.

# 2. Resultado del Ataque de Fuerza Bruta :
<img width="368" height="491" alt="image" src="https://github.com/user-attachments/assets/ecab6933-c082-4b9c-9e05-e962cf09caf4" />



##  Reflexión

Este proyecto me resultó útil porque me permitió comprender de forma práctica cómo funciona un ataque de fuerza bruta y por qué las contraseñas débiles representan un riesgo para la seguridad. Al ejecutar el código, pude observar cómo el algoritmo prueba combinaciones de manera secuencial y cómo incluso una contraseña corta puede requerir una gran cantidad de intentos.

El desarrollo de este programa me enseñó que la longitud de la contraseña y la variedad de caracteres utilizados influyen directamente en el tiempo de ejecución. A medida que aumento la longitud o incluyo mayúsculas, minúsculas, números y símbolos, el número de combinaciones posibles crece de forma exponencial.

Si la contraseña y la longitud son muy extensas, el algoritmo puede tardar horas, días o incluso años en encontrarla. Por esta razón, la fuerza bruta no es un método conveniente ni eficiente para el crackeo de contraseñas seguras, lo que refuerza la importancia de utilizar contraseñas largas y complejas para proteger la información.


