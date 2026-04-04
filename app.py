from flask import Flask, render_template, jsonify, request, send_file
import razorpay

app = Flask(__name__)

client = razorpay.Client(auth=("YOUR_KEY_ID", "YOUR_SECRET"))

# Home
@app.route("/")
def home():
    return render_template("index.html")

# Create order
@app.route("/create-order")
def create_order():
    order = client.order.create({
        "amount": 2000,
        "currency": "INR",
        "payment_capture": 1
    })
    return jsonify(order)

# Verify payment
@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    try:
        client.utility.verify_payment_signature(data)
        return jsonify({"status": "success"})
    except:
        return jsonify({"status": "failed"})

# 🔥 FILE ROUTES (IMPORTANT)
@app.route("/file1")
def file1():
    return send_file("SPGD.pdf")

@app.route("/file2")
def file2():
    return send_file("5 Mark(SPGD).pdf")

@app.route("/file3")
def file3():
    return send_file("10 Mark(SPGD).pdf")

# PDF page
@app.route("/pdf")
def pdf():
    return render_template("pdf.html")

if __name__ == "__main__":
    app.run(debug=True)