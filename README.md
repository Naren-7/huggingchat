# 😁 HuggingChat - Asistente de Inteligencia Artificial

Asistente de inteligencia artificial basado en el API de HuggingChat. Permite chatear con un modelo de lenguaje de manera sencilla y rápida desde tu ¡TERMINAL! 🤯

## Uso

### 1. **Requisitos**

Asegúrate de tener las siguientes bibliotecas instaladas:

```bash
pip install -r requirements.text
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




- **Configuración para Windows**

    Primero, establece la ruta del directorio del proyecto como una variable:

    ```bash
    $chat = 'Ruta_del_directorio'
    ```

    Agrega esta ruta al PATH del sistema para que puedas ejecutar el programa desde cualquier ubicación:

    ```bash
    $env:Path += ";$chat"
    ```

    Comprueba que la ruta este correctamente en el PATH.
     ```bash
       $env:Path
    ```
 


### 4. **Ejecución del Proyecto**

Desde la línea de comandos, puedes ejecutar el programa en cualquier ubicación:

```bash
python main.py
```

## Nota

Asegúrate de mantener tus credenciales seguras y no compartirlas con nadie. ¡Disfruta chateando con tu asistente de inteligencia artificial!