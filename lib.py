def remove_spaces(text: str):
    table = str.maketrans({
        '\u3000': '',
        ' ': '',
        '\t': '',
        '　': ''
    })
    return text.translate(table)
