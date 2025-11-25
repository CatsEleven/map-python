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
    response = supabase.table("near-miss-log").select("*").execute()
    logs = response.data  # list of dict

    return render_template("adult.html", logs=logs)


if __name__ == '__main__':
    app.run(debug=True)