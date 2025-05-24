from flask import Flask, request, jsonify  
app = Flask(__name__)  

@app.route('/chat', methods=['POST'])  
def chat():  
    data = request.json  
    user_message = data.get('message', '')  
    # Aqui você integra o DeepSeek depois!  
    return jsonify({"response": f"Olá! Recebi: {user_message}"})  

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=10000)  
