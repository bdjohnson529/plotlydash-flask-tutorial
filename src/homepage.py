from flask import Flask
from flask import render_template


def init_app(server):
    @server.route("/")
    def homepage():
        """Landing page."""
        return render_template(
            "homepage.html",
            title="Dash-Flask Web Application",
            description="Embed Plotly Dash into your Flask applications.",
            template="home-template",
            body="This is a homepage served with Flask.",
        )

    return server