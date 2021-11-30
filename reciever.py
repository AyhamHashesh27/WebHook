# flask is a micro framework for a web server in python
# To install, from cmd: pip install flask
from flask import Flask, request, abort

app = Flask(__name__)

# URI of server that is listening
@app.route('/webhook', methods=['POST'])
def webhook():
  if request.method == 'POST':
    print(request.json)
    return 'SUCCESS', 200
  else:
    # Something bad happened
    abort(400)

if __name__ == '__main__':
  app.run()

# After running this reciever server: http://127.0.0.1:5000/webhook