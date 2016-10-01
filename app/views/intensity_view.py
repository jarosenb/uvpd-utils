from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify, make_response

from app.forms import IntensityForm
from app.lib.intensity.scrub_intensity_input import scrub_intensity_input
from app import app



@app.route('/', methods=['GET', 'POST'])
def intensity():
    form = IntensityForm()

    if request.method == 'GET':
        return render_template('intensity/intensity.html', form=form)

    if form.validate_on_submit():
        result=scrub_intensity_input(form)
        return render_template('intensity/intensity.html', form=form, result=result)

    return render_template('intensity/intensity.html', form=form, val = form.validate_on_submit())

if __name__ == '__main__':
    app.run(debug=True)