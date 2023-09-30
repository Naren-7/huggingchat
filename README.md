# 😁 HuggingChat - Asistente de Inteligencia Artificial

Asistente de inteligencia artificial basado en el API de HuggingChat. Permite chatear con un modelo de lenguaje de manera sencilla y rápida desde tu ¡TERMINAL! 🤯

## Uso

### 1. **Requisitos**

Asegúrate de tener las siguientes bibliotecas instaladas:

```bash
pip install -r requirements.txt
```

### 2. **Configuración**

Abre el archivo [`env.py`](/env.py) y agrega tus credenciales de con los que te registrates en  [Hugichat](https://huggingface.co/chat/):

```python
email = "tu_correo@example.com"
passwd = "tu_contraseña_secreta"
```

### 3. **Agregar la PAHT (OPCIONAL)**
Para ejecutar el programa desde cualquier ubicación en Mac, Windows o Linux, primero, agrega el directorio del proyecto al PATH. 

- **En Mac o Linux:**

    Abre tu archivo de perfil de shell (`~/.bashrc`, `~/.zshrc`, etc.) y agrega la siguiente línea al final del archivo:

    ```bash
    export PATH=$PATH:/ruta/al/directorio/del/proyecto
    ```

    Reemplaza `/ruta/al/directorio/del/proyecto` con la ruta real hacia el directorio del proyecto.




- En Windows:

    Agrega la ruta del directorio del proyecto a la variable de entorno PATH siguiendo estos pasos:

    1. Busca "Editar variables de entorno del sistema" en la barra de búsqueda de Windows.
    2. Haz clic en "Variables de entorno..."
    3. En la sección "Variables de sistema", busca la variable PATH y haz clic en "Editar..."
    4. Agrega la ruta completa al directorio del proyecto, por ejemplo, C:\ruta\al\directorio\del\proyecto.
 


### 4. **Ejecución del Proyecto**

Desde la línea de comandos, puedes ejecutar el programa en cualquier ubicación:

```bash
python main.py
```

## Nota

Asegúrate de mantener tus credenciales seguras y no compartirlas con nadie. ¡Disfruta chateando con tu asistente de inteligencia artificial!
