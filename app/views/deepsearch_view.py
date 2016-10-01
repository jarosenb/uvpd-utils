import os
from celery import Celery
from flask import Flask, request, render_template, session, flash, redirect, \
    url_for, jsonify, make_response

from app.forms import DeepSearchForm
from app import app, celery

import StringIO
import csv

from app.lib.worker import workertask
from app.lib.deepsearch.Search_result import SearchResult
from app.lib.deepsearch.scrub_deepsearch_input import scrub_deepsearch_input

@celery.task(bind=True)
def long_task(self, data):
    return SearchResult(self, data)


@app.route('/deepsearch', methods=['GET', 'POST'])
def index():
    form = DeepSearchForm()

    if request.method == 'GET':
        return render_template('deepsearch/deepsearch_input.html', form=form)

@app.route('/deepsearchcsv/<task_id>')
def deepsearchcsv(task_id):
    task = long_task.AsyncResult(task_id)
    result = task.info['result']
    mylist = result
    si = StringIO.StringIO()
    cw = csv.writer(si)
    cw.writerows(mylist)

    response = make_response(si.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=mycsv.csv'
    response.mimetype = 'text/csv'

    return response




@app.route('/longtask', methods=['POST'])
def longtask():
    form = DeepSearchForm(request.form)
    scrubbed = scrub_deepsearch_input(form)
    task = long_task.delay(scrubbed)
    return jsonify({}), 202, {'Location': url_for('taskstatus',
                                                  task_id=task.id),
                              'ResultStore': url_for('deepsearchcsv',
                                                     task_id=task.id)}


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)