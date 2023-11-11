def get_html_from_markdown_single_code(message: str) -> str:
    return message[message.index('```html') + 7:message.index('\n```\n')]
