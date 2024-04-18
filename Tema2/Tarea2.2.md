## Tarea 2.2

## BOT: Cypherbot

## Expresion_saludo:
**re.compile(r"hello|hi|hey|hola", re.IGNORECASE):** Esta expresión regular busca saludos comunes en varios idiomas, como "hello", "hi", "hey" en inglés, y "hola" en español. El modificador re.IGNORECASE hace que la búsqueda sea insensible a mayúsculas y minúsculas.

## Expresion_estado:
**re.compile(r"(?:¿)?c[oó]mo est[aá]s\??", re.IGNORECASE)**: Esta expresión regular busca preguntas sobre el estado de ánimo, como "¿Cómo estás?" o "Cómo estás?", con diferentes formas de escribir "estás" y con o sin signo de interrogación al final.

## Expresion_hora:
**re.compile(r"dame la hora", re.IGNORECASE)**: Esta expresión regular busca la solicitud de la hora actual con la frase "dame la hora".

## Expresion_operacion:
**re.compile(r"cu[aá]nto es (\d+)\s*\+\s*(\d+)", re.IGNORECASE)**: Esta expresión regular busca preguntas que soliciten la suma de dos números, como "cuánto es [número] + [número]".

## Expresion_cantante_favorito:
**re.compile(r"cual es mi cantante favorito", re.IGNORECASE)**: Esta expresión regular busca la pregunta sobre mi cantante favorito.

## Expresion_estoy_bien:
**re.compile(r"estoy bien", re.IGNORECASE)**: Esta expresión regular busca la afirmación "estoy bien".

## Expresion_estoy_mal:
**re.compile(r"estoy mal", re.IGNORECASE)**: Esta expresión regular busca la afirmación "estoy mal".

## Ejecucion del bot

![Imagen de WhatsApp 2024-04-17 a las 21 29 13_fdbf67d8](https://github.com/UrielAhumada/Lenguajes_Automatas1/assets/160798678/646e9f3d-9d63-4a1f-a37a-445f24f3df2d)

![Imagen de WhatsApp 2024-04-17 a las 21 29 13_6a9d0645](https://github.com/UrielAhumada/Lenguajes_Automatas1/assets/160798678/656b8c36-9e62-46ca-b767-9ae4ecc26aef)

## Codigo

[Codigo BOT](Tema2/bot.py)
