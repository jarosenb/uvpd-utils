from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify, make_response

from app.forms import ChargeForm
from app.lib.chargestate.scrub_charge_input import scrub_charge_input
from app import app



@app.route('/chargestate', methods=['GET', 'POST'])
def chargestate():
    form = ChargeForm()

    if request.method == 'GET':
        return render_template('chargestate/chargestate.html', form=form)

    if form.validate_on_submit():
        result = scrub_charge_input(form)
        return render_template('chargestate/chargestate.html', form=form, result=result)




if __name__ == '__main__':
    app.run(debug=True)