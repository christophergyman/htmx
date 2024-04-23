from flask import Flask, render_template
import markdown

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/post")
def post():
    return render_template('post.html')


@app.route("/convert_markdown", methods=["GET"])
def convert_markdown():
    #   markdown path
    markdown_path = "/home/chezu/Documents/github/htmx/src/static/why-make-a-website.md"
    # read markdown line by line
    with open(markdown_path, "r", encoding="utf-8") as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    return html


if __name__ == "__main__":
    app.run()
