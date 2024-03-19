# Tarea 2.1. Expresiones Regulares

## ¿Que son las expresiones regulares?

Una expresión regular (también conocida como regex o regexp) es una secuencia de caracteres que define un patrón de búsqueda. Estos patrones se utilizan principalmente para buscar o reconocer cadenas de texto dentro de un conjunto más grande de datos. Las expresiones regulares son extremadamente versátiles y se emplean en diversas áreas, como procesamiento de texto, validación de formularios, búsqueda y reemplazo de texto, entre otros

## Importancia

La importancia de las expresiones regulares radica en su versatilidad y utilidad en diversas áreas. Algunos puntos clave de por qué son relevantes:
1. Búsqueda y filtrado de texto:
      - Las expresiones regulares permiten buscar patrones específicos dentro de grandes cantidades de texto. Por ejemplo, puedes usarlas para encontrar direcciones de correo electrónico, números de teléfono o palabras clave en un documento.
      - Son ampliamente utilizadas en motores de búsqueda, editores de texto, procesadores de datos y sistemas de filtrado.
2. Validación de datos:
      - Las expresiones regulares se emplean para verificar si una cadena de texto cumple con un formato específico. Por ejemplo, validar direcciones de correo electrónico, números de teléfono o códigos postales.
      - Son esenciales en formularios web para asegurar que los datos ingresados sean correctos y consistentes.
3. Manipulación de texto:
      - Las expresiones regulares permiten reemplazar, eliminar o modificar partes de una cadena de texto. Por ejemplo, cambiar formatos de fecha, eliminar espacios en blanco o sustituir palabras.
      - Son útiles en procesos de limpieza de datos y transformación de información.
4. Análisis de logs y archivos de texto:
      - En sistemas informáticos, las expresiones regulares se utilizan para extraer información relevante de archivos de registro (logs) o archivos de texto.
      - Ayudan a identificar patrones de errores, accesos o eventos específicos.
5. Programación y desarrollo de software:
      - Las expresiones regulares son una herramienta poderosa en programación. Se utilizan en lenguajes como Python, JavaScript, Java y otros.
      - Facilitan la búsqueda y manipulación de cadenas de texto en programas y scripts.
6. Lenguajes de consulta y bases de datos:
      - Algunas bases de datos y lenguajes de consulta (como SQL) admiten el uso de expresiones regulares para realizar búsquedas más avanzadas.
      - Puedes buscar patrones específicos en campos de texto o realizar operaciones más complejas.
  
## Casos de Uso

- Coincidiendo un nombre de usuario

 <img src="https://cdn.tutsplus.com/cdn-cgi/image/width=600/net/uploads/legacy/404_regularExpressions/images/username.jpg" width="50%" height="300">

 **Patrón:**
 /^[a-z0-9_-]{3,16}$/

 **Descripción:**
 Empezamos diciendole al analizador sintáctico que encuentre el principio de la cadena (^), seguido de cualquier letra minúscula (a-z), número (0-9), un carácter de subrayado o un guión. A continuación, {3,16} asegura que sean al menos 3 de esos caracteres, pero no más de 16. Por último, queremos el final de la cadena ($).

 **Cadena que coincide:**
 mi us3r_n4m3

 - Coincidencia de contraseña
 <img src="https://cdn.tutsplus.com/cdn-cgi/image/width=600/net/uploads/legacy/404_regularExpressions/images/password.jpg" width="50%" height="300">

 **Patrón:**
 /^[a-z0-9_-]{6,18}$/

**Descripción:**
La coincidencia de una contraseña es muy similar a la coincidencia de un nombre de usuario. La única diferencia es que en vez de 3 a 16 letras, números, guiones bajos o guiones, queremos 6 a 18 de ellos ({6,18}).

**Cadena que coincide:**
myp4ssw0rd
 
## Conclusión

En el mundo de la manipulación y el análisis de texto, las expresiones regulares son una herramienta poderosa y versátil, y aprender a usarlas puede mejorar significativamente la eficiencia y la precisión de una amplia gama de aplicaciones de procesamiento de texto.

## Referencias
- *Cabrera, E. (2024, 15 marzo). RegEx 101: Guía de supervivencia para entender y usar expresiones regulares. Eudris Cabrera Personal Site. https://eudriscabrera.com/blog/2022/regex-101.html*
- *Vasili. (2022, 23 octubre). 8 Expresiones regulares, que debes conocer. Code Envato Tuts+. https://code.tutsplus.com/es/8-regular-expressions-you-should-know--net-6149t*
