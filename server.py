from flask import Flask, render_template, Response


app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html", lunch="짬뽕")


@app.route("/seoul")
def print_seoul():
    
    import sqlite3
    import pandas as pd

    conn = sqlite3.connect("../daily_weather.db")

    sql = """
    SELECT *
    FROM Seoul
    """

    df = pd.read_sql(sql, conn)
    dataframe = df.to_html()

    conn.close()

    return render_template("seoul.html", dataframe=dataframe)

@app.route("/plot")
def print_plot():

    import matplotlib.pyplot as plt
    import sqlite3
    import pandas as pd
    import io

    conn = sqlite3.connect("../daily_weather.db")

    sql = """
    SELECT *
    FROM Seoul
    """

    df = pd.read_sql(sql, conn)

    conn.close()

    plt.plot(df["id"], df["temp"], marker="o")

    img = io.BytesIO()
    plt.savefig(img, format="png")

    return Response(img.getvalue(), mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



