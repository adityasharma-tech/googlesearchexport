import os
import requests

from flask import Flask, send_file

app = Flask(__name__)

def raw_search_result(search_query):
    return requests.get(f'https://google.com')

@app.route('/s/<query>')
def search_route(query):
    return str(raw_search_result(query))

def main():
    app.run(port=int(os.environ.get('PORT', 8000)))

if __name__ == "__main__":
    main()
