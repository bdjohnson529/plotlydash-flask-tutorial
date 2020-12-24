import numpy as np
import pandas as pd
from flask import Flask
from flask import render_template


def init_app(server):
    html = load_csv_as_html('data/scenario_parameters.csv')

    df = pd.read_csv('data/scenario_parameters_old.csv', sep="|")
    df = df.set_index('Parameter')
    d = df.to_dict('index')


    # add route
    @server.route('/tablepage/')
    def tablepage():
        return render_template(
            "tablepage.html",
            title="Input Page",
            template="home-template",
            table=html,
            data=d
        )

    return server




def load_csv_as_html(filepath):
    """
    Load CSV, converts to html using Pandas.
    """
    df = pd.read_csv(filepath, sep="|")
    df = df.set_index('Parameter')

    html = df.to_html()
    html = html.replace('  ', '')
    html = html.replace('\n', '')
    html = html.replace('<td>', '<td><input value="')
    html = html.replace('</td>', '"></td>')

    return html