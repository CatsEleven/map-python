from flask import Flask, render_template
from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/adult')
def adult():
    response = supabase.table("near-miss-log").select("*").execute()
    logs = response.data  

    return render_template("adult.html", logs=logs)


@app.route('/child')
def child():
    response = supabase.table("near-miss-log").select("*").execute()
    logs = response.data  

    return render_template("child.html", logs=logs)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
