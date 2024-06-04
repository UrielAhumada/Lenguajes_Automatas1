import re

# Especificación de los tokens del analizador léxico
token_specification = [
    ('left_angle', r'<'),                  # Token para el símbolo de menor que
    ('right_angle', r'>'),                 # Token para el símbolo de mayor que
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
    ('inicio_comentario', r'<!--'),        # Token para el inicio de un comentario
    ('fin_comentario', r'-->'),            # Token para el fin de un comentario
    ('text', r'[^<>\s]+')                  # Token para texto
]

# Compilación de la especificación de tokens en una expresión regular
token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)
token_regex = re.compile(token_regex, re.IGNORECASE)

# Función para el análisis léxico
def lex(characters):
    for match in re.finditer(token_regex, characters):
        kind = match.lastgroup
        value = match.group()
        yield kind, value

# Clases para la representación del árbol sintáctico
class Node:
    def __init__(self, tag, attributes=None, children=None):
        self.tag = tag
        self.attributes = attributes or {}
        self.children = children or []

    def __repr__(self):
        return f"Node(tag='{self.tag}', attributes={self.attributes}, children={self.children})"

class TextNode:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"TextNode(text='{self.text}')"

# Clase del analizador sintáctico
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token_index = 0
        self.open_tags = []

    def parse(self):
        nodes = self._parse_nodes()
        if self.open_tags:
            raise SyntaxError("Error: Algunas etiquetas no tienen su correspondiente etiqueta de cierre.")
        return nodes

    def _parse_nodes(self):
        nodes = []
        while self.current_token_index < len(self.tokens):
            node = self._parse_node()
            if node:
                nodes.append(node)
            else:
                break  # Salir del bucle si no se puede parsear un nodo
        return nodes

    def _parse_node(self):
        token_type, token_value = self._current_token()
        if token_type == 'left_angle':
            self._advance()
            token_type, tag_name = self._current_token()
            self._advance()
            if token_value.startswith('!'):  # Si es un comentario, saltamos su contenido
                while self._current_token()[0] != 'fin_comentario':
                    self._advance()
                self._advance()  # Saltar token de fin de comentario
                return None
            attributes = self._parse_attributes()
            self._advance()  # Saltar '>'
            children = []
            while True:
                if self._current_token()[0] == 'left_angle':
                    if self._peek_next_token() and self._peek_next_token()[1] == '/':
                        break  # Se encontró una etiqueta de cierre
                    child = self._parse_node()
                    if child:
                        children.append(child)
                elif self._current_token()[0] == 'text':
                    child = self._parse_node()
                    if child:
                        children.append(child)
                else:
                    break
            self._advance()  # Saltar '</'
            self._advance()  # Saltar tag name
            self._advance()  # Saltar '>'
            return Node(tag_name, attributes, children)
        elif token_type == 'text':
            self._advance()
            return TextNode(token_value)
        else:
            self._advance()
            return None


    def _parse_attributes(self):
        attributes = {}
        while self._current_token()[0] in {'id', 'class', 'src', 'href', 'alt', 'style', 'width', 'height', 'title'}:
            attr_name = self._current_token()[1]
            self._advance()  # Saltar al '='
            self._advance()  # Saltar '='
            attr_value = self._current_token()[1]
            self._advance()  # Saltar el valor
            attributes[attr_name] = attr_value
        return attributes

    def _current_token(self):
        return self.tokens[self.current_token_index]

    def _advance(self):
        self.current_token_index += 1

    def _peek_next_token(self):
        if self.current_token_index + 1 < len(self.tokens):
            return self.tokens[self.current_token_index + 1]
        else:
            return None

# Ejecutar el analizador léxico y sintáctico
with open('input.html', 'r', encoding='utf-8') as file:
    data = file.read()

tokens = list(lex(data))
print("Tokens:")
for token in tokens:
    print(token)

# Ejecutar el analizador sintáctico
parser = Parser(tokens)
ast = parser.parse()

# Si no ocurrió un error durante el análisis, imprimir el árbol sintáctico
if ast is not None:
    print("AST:")
    for node in ast:
        print(node)
else:
    print("No se pudo generar el árbol sintáctico debido a errores de formato en las etiquetas.")
