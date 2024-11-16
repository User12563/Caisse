def calculate(wallet, articles, carte_de_fidelite):
    total = sum(articles)
    if carte_de_fidelite == 'oui':
        total *= 0.9
    
    reste = wallet - total if wallet > total else 0
    manque = total - wallet if total > wallet else 0

    print(f"Total des articles : {total:.2f} €")
    print(f"Reste : {reste:.2f} €")
    print(f"Manque : {manque:.2f} €")
    print(f"Carte de fidélité : {carte_de_fidelite}")

if __name__ == "__main__":
    wallet = float(input("Montant dans le portefeuille : "))
    articles = []
    
    while True:
        article = input("Prix de l'article (ou appuyez sur Entrée pour terminer) : ")
        if article == "":
            break
        try:
            articles.append(float(article))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    carte_de_fidelite = input("Avez-vous une carte de fidélité ? (oui/non) : ").lower()
    calculate(wallet, articles, carte_de_fidelite)
