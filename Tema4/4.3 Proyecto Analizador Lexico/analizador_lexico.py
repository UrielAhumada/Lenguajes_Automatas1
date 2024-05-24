import re

# Definir las expresiones regulares para cada tipo de token
token_specification = [
    ('pagina', r'\bhtml\b'),
    ('cabecera', r'\bhead\b'),
    ('titulo', r'\btitle\b'),
    ('cuerpo', r'\bbody\b'),
    ('e1', r'\bh1\b'),
    ('e2', r'\bh2\b'),
    ('e3', r'\bh3\b'),
    ('e4', r'\bh4\b'),
    ('e5', r'\bh5\b'),
    ('e6', r'\bh6\b'),
    ('p', r'\bp\b'),
    ('cont', r'\bdiv\b'),
    ('span', r'\bspan\b'),
    ('enlace', r'\ba\b'),
    ('imagen', r'\bimg\b'),
    ('src', r'\bsrc\b'),
    ('href', r'\bhref\b'),
    ('alt', r'\balt\b'),
    ('id', r'\bid\b'),
    ('clase', r'\bclass\b'),
    ('estilo', r'\bstyle\b'),
    ('ancho', r'\bwidth\b'),
    ('alto', r'\bheight\b'),
    ('titulo_atr', r'\btitle\b'),
    ('igual', r'='),
    ('comilla', r"'"),
    ('doble_comilla', r'"'),
    ('punto_y_coma', r';'),
    ('left_angle', r'<'),
    ('right_angle', r'>'),
    ('inicio_comentario', r'<!--'),
    ('fin_comentario', r'-->')
]

# Crear una expresión regular que agrupe todas las anteriores
token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
token_regex = re.compile(token_regex, re.IGNORECASE)  # Ignorar mayúsculas/minúsculas

def lex(characters):
    for match in re.finditer(token_regex, characters):
        kind = match.lastgroup
        value = match.group()
        yield kind, value

# Leer el archivo de entrada
with open('input.html', 'r', encoding='utf-8') as file:
    data = file.read()

# Realizar el análisis léxico
tokens = list(lex(data))

# Mostrar los tokens
for token in tokens:
    print(token)
