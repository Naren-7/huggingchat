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



### 3. **Crear Alias para Ejecutar el script (Opcional)**

Crear un alias te permite ejecutar el programa desde cualquier ubicación. En Mac y Linux, puedes editar tu archivo `.bashrc` o `.bash_profile`. Abre el archivo en un editor de texto y agrega el siguiente alias:

- **En Mac o Linux:**

  ```bash
  echo 'alias chatbot="python /ruta/al/directorio/del/proyecto/nombre_del_archivo.py"' >> ~/.bashrc
  source ~/.bashrc
  ```

  Reemplaza `/ruta/al/directorio/del/proyecto` con la ruta real hacia el directorio del proyecto y `nombre_del_archivo.py` con el nombre real de tu archivo Python.

- **En Windows (PowerShell):**

  ```powershell
   New-Alias chatbot chatbot  C:\ruta\al\directorio\del\proyecto\main.py
  ```

  **Hacer el alias permanente en PowerShell:**

  **Abre PowerShell como administrador.**

  **Abre o crea tu perfil de PowerShell:**

   ```powershell
   notepad $PROFILE
   ```

  **Agrega el alias al final del archivo:**

   ```powershell
   New-Alias chatbot 'C:\ruta\al\directorio\del\proyecto\nombre_del_archivo.py'
   ```

  **Guarda y cierra el archivo.**

  Reemplaza `C:\ruta\al\directorio\del\proyecto\nombre_del_archivo.py` con la ruta real hacia tu archivo Python.
  
  <br>
  <br>



A partir de este momento, podrás usar el alias `chatbot` en cualquier sesión de PowerShell para ejecutar tu archivo `main.py`. 
## 4. **Ejecución del Proyecto**

Desde cualquier ubicación, puedes simplemente escribir `chatbot` en la línea de comandos para ejecutar el programa:

```bash
chatbot
```

## Nota

Asegúrate de mantener tus credenciales seguras y no compartirlas con nadie. ¡Disfruta chateando con tu asistente de inteligencia artificial!
