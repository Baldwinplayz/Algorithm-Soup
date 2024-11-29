from home_template import *

def render_template(type: int, file: str, title: str) -> str:
    """
    This code will wrap a template around the main html code in the center.
    """
    if type == 0:
        with open(file, "r") as f:
            return home_template(f.read(), title)
    with open(file) as f:
        return f.read()
