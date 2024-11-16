from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    wallet = float(request.form['wallet'])
    articles = request.form.getlist('articles')
    articles = [float(article) for article in articles if article]
    total = sum(articles)
    reste = wallet - total if wallet > total else 0
    manque = total - wallet if total > wallet else 0
    carte_de_fidelite = request.form['carte_de_fidelite']
    if carte_de_fidelite == 'oui':
        total *= 0.9
    return render_template('result.html', total=total, reste=reste, manque=manque, carte_de_fidelite=carte_de_fidelite)

if __name__ == '__main__':
    app.run(debug=True)
