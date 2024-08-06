from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy auction data
auctions = [
    {"id": 1, "name": "Antique Vase", "current_bid": 100, "description": "A beautiful antique vase from the 19th century."},
    {"id": 2, "name": "Vintage Watch", "current_bid": 200, "description": "A classic vintage watch with a leather strap."}
]

@app.route('/')
def index():
    return render_template('index.html', auctions=auctions)

@app.route('/auction/<int:item_id>')
def auction(item_id):
    item = next((item for item in auctions if item['id'] == item_id), None)
    if item is None:
        return "Item not found", 404
    return render_template('auction.html', item=item)

@app.route('/bid/<int:item_id>', methods=['POST'])
def bid(item_id):
    new_bid = int(request.form['bid_amount'])
    for item in auctions:
        if item['id'] == item_id:
            if new_bid > item['current_bid']:
                item['current_bid'] = new_bid
                # Here you might want to update the last bid time if you are tracking it
            else:
                return "Bid must be higher than the current bid.", 400
    return redirect(url_for('auction', item_id=item_id))

if __name__ == '__main__':
    app.run(debug=True)
