from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home(): return "Alive and well. \U0001f6e0\uFE0F \n :D"

def run(): app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t =Thread(target=run)
  t.start()