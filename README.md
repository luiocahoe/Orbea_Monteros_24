# Proyecto PEC4 - Análisis de Datos de Ciclistas

## Estructura del Proyecto

- **main.py**: Archivo principal que ejecuta todas las funciones.
- **src/**: Directorio que contiene la lógica del proyecto.
- **tests/**: Directorio que contiene los tests unitarios.
- **requirements.txt**: Archivo que lista las dependencias necesarias.
- **setup.py:** Archivo de configuración para la instalación del paquete.
- **LICENSE.txt:** Archivo que contiene la licencia del proyecto.

## Instrucciones para Ejecutar el Proyecto

### 1. Configuración del Entorno Virtual

Antes de ejecutar el proyecto, se debe crear y activar un entorno virtual para gestionar las dependencias de Python de manera aislada. Los pasos a seguir son:

1. **Acceder al Directorio del Proyecto**:
   Se debe acceder al directorio donde se encuentra el proyecto:

   ```bash
   cd /ruta/a/pec4
   ```

2. **Crear el Entorno Virtual**:
   Utilizando `venv`, se crea un entorno virtual, que se puede nombrar `venv` u otro nombre preferido:

   ```bash
   python3 -m venv venv
   ```

3. **Activar el Entorno Virtual**:
   Para activar el entorno virtual, se ejecuta:

   ```bash
   source venv/bin/activate
   ```

4. **Instalar las Dependencias**:
   Con el entorno virtual activo, se instalan las dependencias listadas en el archivo `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

### 2. Ejecución del Proyecto

Una vez configurado el entorno, se procede a ejecutar el proyecto siguiendo estos pasos:

* **Activar el Entorno Virtual**:
   Si no se ha activado previamente, se hace con el comando:

   ```bash
   source venv/bin/activate
   ```

* **Ejecutar Ejercicios**:

   - **Ejecutar Todos los Ejercicios**:
     Para ejecutar todos los ejercicios (del 1 al 5) de manera secuencial, se utiliza:

     ```bash
     python main.py
     ```

   - **Ejecutar un Ejercicio Específico**:
     Si se desea ejecutar un ejercicio en particular, se usa el parámetro `--ejercicio` seguido del número correspondiente. Por ejemplo, para ejecutar el ejercicio 3 (incluyendo los anteriores, 1 y 2):

     ```bash
     python main.py --ejercicio 3
     ```

     El número del ejercicio se puede cambiar para ejecutar cualquier otro entre el 1 y el 5.

### 3. Desactivación del Entorno Virtual

Cuando se concluyen las tareas en el proyecto, el entorno virtual se desactiva con:

```bash
deactivate
```

## Ejecución de Tests en `unittest`

### 1. Ejecutar Todos los Tests

Para ejecutar todas las pruebas ubicadas en el directorio `tests`, se emplea el comando:

```bash
python -m unittest discover tests
```

### 2. Ejecutar un Test Específico

Si se requiere ejecutar un test de un archivo en particular, se usa:

```bash
python -m unittest tests.test_select_club
```

### 3. Mostrar Resultados Detallados

Para ver resultados más detallados de las pruebas:

```bash
python -m unittest discover tests -v
```

## Ejecución de Tests en `unittest`

### 1. Ejecutar Todos los Tests

Para ejecutar todas las pruebas ubicadas en el directorio `tests`, se emplea el comando:

```bash
python -m unittest discover tests
```

### 2. Ejecutar un Test Específico

Si se requiere ejecutar un test de un archivo en particular, se usa:

```bash
python -m unittest tests.test_select_club
```

### 3. Mostrar Resultados Detallados

Para ver resultados más detallados de las pruebas:

```bash
python -m unittest discover tests -v
```

## Comprobar la Cobertura de los Tests

Para comprobar la cobertura de los tests, se usa la herramienta `coverage`:

1. **Ejecuta los tests con cobertura**:

   ```bash
   coverage run -m unittest discover tests
   ```

   Este comando ejecuta todos los tests y mide la cobertura del código.

2. **Genera un reporte de cobertura**:

   Para ver un reporte:

   ```bash
   coverage report
   ```

   Esto muestra el porcentaje de código cubierto por los tests. Aquí está el informe de cobertura de las pruebas más reciente:

   Name                          Stmts   Miss  Cover
-------------------------------------------------
src/__init__.py                   0      0   100%
src/anonymize.py                 10      0   100%
src/clean_club.py                10      0   100%
src/data_loader.py                3      0   100%
src/select_club.py                5      0   100%
src/time_grouping.py             25      2    92%
tests/test_anonymize.py          25      1    96%
tests/test_clean_club.py         10      1    90%
tests/test_data_loader.py        10      1    90%
tests/test_select_club.py        13      1    92%
tests/test_time_grouping.py      26      1    96%
-------------------------------------------------
TOTAL                           137      7    95%

La cobertura general del proyecto es del 95%.

## Comprobación de Calidad del Código con `pylint`

`pylint` es una herramienta que analiza el código Python para verificar su calidad, identificar errores y garantizar que siga las buenas prácticas de estilo.

### Ejecutar `pylint`

- **Para analizar todo el proyecto**:
  ```bash
  pylint src tests main.py
  ```

- **Para analizar un archivo específico** (por ejemplo, `main.py`):
  ```bash
  pylint src/clean_club.py
  ```

### Resultado

El código ha obtenido una calificación de 9.86/10 en pylint. Las advertencias sobre importaciones no utilizadas, como `Faker` en `tests/test_anonymize.py` y `matplotlib.pyplot` en `tests/test_time_grouping.py`, son en realidad necesarias.
