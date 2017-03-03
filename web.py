from flask import Flask
app = Flask(__Name__)

@app.route('/')
def inde():
  return 'Hello World'
