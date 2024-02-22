
def header(text, level=1):
    """Create a Markdown header."""
    return f"{'#' * level} {text}\n"

def bold(text):
    """Make text bold."""
    return f"**{text}**"

def italic(text):
    """Make text italic."""
    return f"*{text}*"

def link(text, url):
    """Create a link."""
    return f"[{text}]({url})"

def unordered_list(items):
    """Create an unordered list."""
    return '\n'.join(f"- {item}" for item in items) + '\n'

def ordered_list(items):
    """Create an ordered list."""
    return '\n'.join(f"{i + 1}. {item}" for i, item in enumerate(items)) + '\n'

def code_block(code, language=''):
    """Create a code block."""
    return f"```{language}\n{code}\n```\n"

def blockquote(text):
    """Create a blockquote."""
    return f"> {text}\n"

def horizontal_rule():
    """Create a horizontal rule."""
    return "---\n"

def image(alt_text, url, title=''):
    """Embed an image."""
    title_attr = f' "{title}"' if title else ''
    return f"![{alt_text}]({url}{title_attr})\n"

def strikethrough(text):
    """Strike through text."""
    return f"~~{text}~~"

def table(headers, rows):
    """Generate a table. Assumes all rows have the same number of columns as the headers list."""
    header_row = '| ' + ' | '.join(headers) + ' |'
    separator_row = '| ' + ' | '.join(['---'] * len(headers)) + ' |'
    data_rows = '\n'.join('| ' + ' | '.join(row) + ' |' for row in rows)
    return f"{header_row}\n{separator_row}\n{data_rows}\n"

def inline_code(code):
    """Format inline code."""
    return f"`{code}`"

def footnote(text, identifier):
    """Add a footnote. Identifier must be unique for each footnote in the document."""
    return f"{text}[^{identifier}]\n\n[^{identifier}]: "


