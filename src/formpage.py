import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

def init_app(server):
    # add route
    @server.route('/formpage/', methods=['GET','POST'])
    def formpage():
        if request.method == 'POST':
            # validate scenario name
            scenarioname = request.values.get('scenarioname')
            scenarioname = scenarioname.replace(' ', '-')

            # read existing scenario names
            lookup_df = pd.read_csv('data/lookup_scenario.csv', sep="|")
            scenariodesc = lookup_df['ScenarioDesc'].tolist()
            scenarioids = lookup_df['ScenarioID'].tolist()

            if scenarioname not in scenariodesc:
                scenarioid = max(scenarioids) + 1
                
                inflationrate = request.values.get('inflationrate')
                interestrate = request.values.get('interestrate')
                startingcash = request.values.get('startingcash')
                startingdebt = request.values.get('startingdebt')

                # create dataframe
                d = [{'Parameter': 'Inflation Rate', 'Value': inflationrate},
                    {'Parameter': 'Interest Rate', 'Value': interestrate},
                    {'Parameter': 'Starting Cash', 'Value': startingcash},
                    {'Parameter': 'Starting Debt', 'Value': startingdebt}]
                
                new_df = pd.DataFrame(d)
                new_df['ScenarioID'] = scenarioid

                # concat new data
                old_df = pd.read_csv('data/scenario_parameters.csv', sep="|")
                combined_df = pd.concat([new_df, old_df])
                combined_df.to_csv('data/scenario_parameters.csv', sep="|", index=False)

                # concat new data
                old_lookup_df = pd.read_csv('data/lookup_scenario.csv', sep="|")
                new_lookup_df = pd.DataFrame({'ScenarioID': [scenarioid], 'ScenarioDesc': [scenarioname]})
                combined_lookup_df = pd.concat([new_lookup_df, old_lookup_df])
                combined_lookup_df.to_csv('data/lookup_scenario.csv', sep="|", index=False)

            else:
                print("Scenario name has been taken")


        # Collect default values from dataframe
        df = pd.read_csv('data/scenario_parameters.csv', sep="|")
        val_inflationrate = df.loc[df['Parameter'] == 'Inflation Rate']['Value'].values[0]
        val_interestrate = df.loc[df['Parameter'] == 'Interest Rate']['Value'].values[0]
        val_startingcash = df.loc[df['Parameter'] == 'Starting Cash']['Value'].values[0]
        val_startingdebt = df.loc[df['Parameter'] == 'Starting Debt']['Value'].values[0]

        # Instantiate form, set defaults
        form = ParameterForm()
        form.scenarioname.data = "Default"
        form.inflationrate.data = val_inflationrate
        form.interestrate.data = val_interestrate
        form.startingcash.data = val_startingcash
        form.startingdebt.data = val_startingdebt

        return render_template(
            "formpage.html",
            title="Form Page",
            template="home-template",
            form=form
        )

    return server


class ParameterForm(FlaskForm):
    scenarioname = StringField('Scenario Name', validators=[DataRequired()])
    inflationrate = FloatField('Inflation Rate', validators=[DataRequired()])
    interestrate = FloatField('Interest Rate', validators=[DataRequired()])
    startingcash = FloatField('Starting Cash', validators=[DataRequired()])
    startingdebt = FloatField('Starting Debt', validators=[DataRequired()])
    submit = SubmitField('Submit')