# Util functions made by Fabrizio1663
def underline(text: str) -> str:
    return f'__{text}__'


def bold(text: str) -> str:
    return f'**{text}**'


def italic(text: str) -> str:
    return f'*{text}*'


def codestring(text: str) -> str:
    return f'`{text}`'


def codeblock(text: str, lang: str = 'py') -> str:
    return f'```{lang}\n{text}```'


def spoiler(text: str) -> str:
    return f'||{text}||'


def array_to_string(array: list, iterable: str = '\n') -> str:
    return f'{iterable}'.join(array)


def clean_code(content: str) -> str:
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


def paginate(text: str) -> list[str]:
    last = 0
    pages: list[str] = []
    for curr in range(0, len(text)):
        if curr % 1930 == 0:
            pages.append(text[last:curr])
            last = curr
            appd_index = curr
    if appd_index != len(text) - 1:
        pages.append(text[last:curr])
    return list(filter(lambda a: a != "", pages))