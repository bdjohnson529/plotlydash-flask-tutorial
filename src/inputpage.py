from flask import Flask
from flask import render_template


def init_app(server):
    # add route
    @server.route('/inputpage/')
    def inputpage():
        return render_template(
            "inputpage.html",
            title="Input Page",
            template="home-template",
        )

    return server
