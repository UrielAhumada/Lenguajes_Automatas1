import re  # Importar el módulo de expresiones regulares

# Definir las expresiones regulares para cada tipo de token
token_specification = [
    ('pagina', r'\bhtml\b'),               # Token para la palabra clave 'html'
    ('cabecera', r'\bhead\b'),             # Token para la palabra clave 'head'
    ('titulo', r'\btitle\b'),              # Token para la palabra clave 'title'
    ('cuerpo', r'\bbody\b'),               # Token para la palabra clave 'body'
    ('e1', r'\bh1\b'),                     # Token para la etiqueta de encabezado 'h1'
    ('e2', r'\bh2\b'),                     # Token para la etiqueta de encabezado 'h2'
    ('e3', r'\bh3\b'),                     # Token para la etiqueta de encabezado 'h3'
    ('e4', r'\bh4\b'),                     # Token para la etiqueta de encabezado 'h4'
    ('e5', r'\bh5\b'),                     # Token para la etiqueta de encabezado 'h5'
    ('e6', r'\bh6\b'),                     # Token para la etiqueta de encabezado 'h6'
    ('p', r'\bp\b'),                       # Token para la palabra clave 'p'
    ('cont', r'\bdiv\b'),                  # Token para la palabra clave 'div'
    ('span', r'\bspan\b'),                 # Token para la palabra clave 'span'
    ('enlace', r'\ba\b'),                  # Token para la palabra clave 'a'
    ('imagen', r'\bimg\b'),                # Token para la palabra clave 'img'
    ('src', r'\bsrc\b'),                   # Token para el atributo 'src'
    ('href', r'\bhref\b'),                 # Token para el atributo 'href'
    ('alt', r'\balt\b'),                   # Token para el atributo 'alt'
    ('id', r'\bid\b'),                     # Token para el atributo 'id'
    ('clase', r'\bclass\b'),               # Token para el atributo 'class'
    ('estilo', r'\bstyle\b'),              # Token para el atributo 'style'
    ('ancho', r'\bwidth\b'),               # Token para el atributo 'width'
    ('alto', r'\bheight\b'),               # Token para el atributo 'height'
    ('titulo_atr', r'\btitle\b'),          # Token para el atributo 'title'
    ('igual', r'='),                       # Token para el operador '='
    ('comilla', r"'"),                     # Token para el símbolo de comilla simple
    ('doble_comilla', r'"'),               # Token para el símbolo de comilla doble
    ('punto_y_coma', r';'),                # Token para el símbolo de punto y coma
    ('left_angle', r'<'),                  # Token para el símbolo de menor que
    ('right_angle', r'>'),                 # Token para el símbolo de mayor que
    ('inicio_comentario', r'<!--'),        # Token para el inicio de un comentario
    ('fin_comentario', r'-->')             # Token para el fin de un comentario
]

# Crear una expresión regular que agrupe todas las anteriores
token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
token_regex = re.compile(token_regex, re.IGNORECASE)  # Ignorar mayúsculas/minúsculas

def lex(characters):  # Función para realizar el análisis léxico
    for match in re.finditer(token_regex, characters):
        kind = match.lastgroup  # Obtener el nombre del grupo coincidente
        value = match.group()   # Obtener el valor del token
        yield kind, value       # Generar el tipo de token y su valor

# Leer el archivo de entrada
with open('input.html', 'r', encoding='utf-8') as file:
    data = file.read()  # Leer el contenido del archivo

# Realizar el análisis léxico
tokens = list(lex(data))

# Mostrar los tokens
for token in tokens:
    print(token)  # Imprimir cada token encontrado
