from flask import Flask, render_template, jsonify

app = Flask(__name__)


JOBS = [
    {
        "id":1,
        "title":"Software Engineer",
        "location":"San Francisco, CA",
        "salary":"$100,000",
    },
    {
        "id":2,
        "title":"Product Manager",
        "location":"San Francisco, CA",
        "salary":"$200,000",
    },
    {
        "id":3,
        "title":"Data Scientist",
        "location":"San Francisco, CA",
        "salary":"$120,000",
    },
    {
        "id":4,
        "title":"Machine Learning Engineer",
        "location":"San Francisco, CA",
        "salary":"$150,000",
    }
]


@app.route("/")
def index():
    return render_template("home.html", jobs=JOBS)

@app.route("/jobs")
def list_jobs():
    return jsonify(JOBS)



if __name__ == "__main__":
    app.run(debug=True)