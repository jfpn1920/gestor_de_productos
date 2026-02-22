## 👋 ¡Bienvenidos usuarios a mi proyecto! gestor de productos

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en desarrollar un sistema básico de gestión de productos en Python, el cual permite administrar productos junto con su respectivo precio utilizando un diccionario como estructura principal de almacenamiento.

El programa permite agregar nuevos productos, modificar precios existentes y visualizar todos los productos registrados. La interacción se realiza mediante un menú en consola que facilita la gestión de la información de forma clara y organizada.

Este proyecto simula el funcionamiento elemental de un sistema de inventario, reforzando la importancia de validar datos correctamente, especialmente cuando se trabaja con valores numéricos como precios. Además, promueve una estructura modular del código mediante el uso de funciones independientes para cada operación, lo que mejora la legibilidad, el mantenimiento y la escalabilidad.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar el uso de **diccionarios** para almacenar productos y precios.
- Aplicar **funciones** para dividir responsabilidades dentro del programa.
- Utilizar **condicionales** para validar información ingresada por el usuario.
- Implementar **bucles** para mantener la ejecución continua del sistema.
- Validar entradas numéricas utilizando manejo de excepciones.
- Diseñar un sistema interactivo basado en menú.

#
### 🧠 Temas que se a aplicado
- Diccionarios (`clave: valor`)
- Funciones
- Bucles `while`
- Bucles `for`
- Condicionales `if / else`
- Validaciones de datos
- Manejo de excepciones (`try / except`)
- Conversión de tipos (`float`)
- Formateo de números (`:.2f`)
- Manipulación de cadenas (`strip()`, `lower()`, `capitalize()`)

#
### ⚙️ Funcionamiento
1. Agregar producto  
2. Modificar producto  
3. Mostrar productos  
4. Salir  

### Agregar producto
Permite ingresar el nombre de un producto y su precio, el sistema valida que:
- El producto no exista previamente.
- El precio sea un número válido.
- El precio sea mayor que cero.
- Si las condiciones se cumplen, el producto se almacena en el diccionario.

### Modificar producto
- Permite actualizar el precio de un producto existente.  
- Se valida que el producto esté registrado y que el nuevo precio sea válido.

### Mostrar productos
- Muestra todos los productos registrados junto con su precio formateado a dos decimales.
- El programa se mantiene en ejecución hasta que el usuario seleccione la opción **Salir**.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```