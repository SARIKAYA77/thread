from flask import Flask
import m


app = Flask(__name__)

@app.route('/')
def my_function():
   result = m.start_check()

   result = '\r\n'.join(result)
   return result