def render_template(type: int, file: str) -> str:
    """
    This code will wrap a template around the main html code in the center.
    """
    with open(file, "r") as f:
        return f.read()
