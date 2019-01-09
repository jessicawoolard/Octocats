import os

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    post_name = request.args.get('post')

    counter_file_name =  'NumberOfClicks'.format(post_name)

    print(counter_file_name)

    if os.path.exists(counter_file_name):
        counter_file = open(counter_file_name, 'r+')
    else:
        counter_file = open(counter_file_name, 'w+')

    post_count = counter_file.read()

    if not post_count:
        post_count = 0

    new_count = 1 + int(post_count)

    print(new_count)

    counter_file.seek(0)
    counter_file.write(str(new_count))
    counter_file.close()

    index_file = open('index.html', 'r')
    my_html = index_file.read()
    index_file.close()
    
    return my_html