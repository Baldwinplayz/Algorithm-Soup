def home_template(html: str, title: str) -> str:
    return f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" type="text/css" href="/static/styles.css">
        <script src="/static/script.js"></script>
        <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    </head>
    <body>
        <div id="content">
            <div id="title_grid">
                <h1 id="PI" style="align-items: center; 
                    color: white;">
                    Π
                </h1> 
                <h1>
                    <a href="/" style="font-family: 'Courier New', Courier, monospace;">
                        <span style="color: rgb(55, 215, 236);">Algorithm</span>
                        <span style="color: rgb(241, 141, 34)">Soup</span>
                    </a>
                    <br>
                    <span style="font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif; 
                        color: rgb(76, 222, 180);
                        font-size: 16px;">
                        <i>Online Algorithms</i>
                    </span>
                </h1>
            </div>
            
            <hr></hr>

{html}

        </div>
        <p id="copy_right">
            © 2024 Baldwin Huang 
            <br>
            All rights reserved.
        </p>
    </body>
</html>
"""