from flask import Flask, render_template

app = Flask(__name__)

analyses = [
    {
        "title": "Sick one",
        "html": r"<i>What up, son!</i>"
    },
    {
        "title": "An even sicker one",
        "html": r"<i>Yeah, this is indeed what is going down</i>"
    },
    {
        "title": "Casiopea",
        "html": r"Just good wholesome stuff."
    },
]

@app.route('/')
def hello_world():
    return render_template(
        "base.html",
        analysis_list=analyses
    )


if __name__ == '__main__':
    app.run()
