from flask import request, Flask
import logging
from App import app

logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.before_request   
def before_request_callback():   
    app.logger.info("before request is working")
    

@app.after_request
def after_request_callback(response):
    response_value =response.get_data()
    app.logger.info('Info level log')
    app.logger.warning('Warning level log')
    app.logger.debug(response_value.decode("utf-8"))
    return response
    
