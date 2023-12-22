import re


def text_to_html(text: str):
    text = text.replace('\n', '<br>')
    pattern = r'\*\*(.*?)\*\*'
    return re.sub(pattern, lambda x: f'<h3>{x.group(1)}</h3>', text)
