"""Plotly Dash HTML layout override.
The header matches the header in the file header.html"""

html_layout = """
<!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%css%}
        </head>
        <body class="dash-template">
            <header>
              <div class="nav-wrapper">
                <a href="/">
                    <img src="/static/img/logo.png" class="logo" />
                    <h1>Dash-Flask Demo App</h1>
                  </a>
                <nav>
                </nav>
            </div>
            </header>
            {%app_entry%}
            <footer>
                {%config%}
                {%scripts%}
                {%renderer%}
            </footer>
        </body>
    </html>
"""
