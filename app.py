from flask import Flask, jsonify

app = Flask(__name__)

# Data JSON dengan informasi tentang makanan
foods = [
    {
        "name": "Nasi Goreng",
        "description": "Nasi goreng Indonesia yang digoreng dengan bumbu dan kecap manis.",
        "carbohydrates": 45,
        "protein": 8,
        "calories": 350,
        "fat": 10,
        "ingredients": ["nasi", "bawang putih", "kecap manis", "telur", "ayam", "kecap asin"]
    },
    {
        "name": "Soto Ayam",
        "description": "Sup ayam khas Indonesia dengan kuah kuning yang lezat.",
        "carbohydrates": 20,
        "protein": 15,
        "calories": 250,
        "fat": 5,
        "ingredients": ["ayam", "bihun", "telur", "daun bawang", "bawang goreng", "jeruk nipis"]
    },
    {
        "name": "Gado-Gado",
        "description": "Salad Indonesia dengan saus kacang yang gurih.",
        "carbohydrates": 30,
        "protein": 10,
        "calories": 200,
        "fat": 8,
        "ingredients": ["sayuran rebus", "tempe", "tahu", "kentang", "telur", "saus kacang"]
    },
    {
        "name": "Rendang",
        "description": "Daging sapi yang dimasak dengan rempah-rempah khas Padang.",
        "carbohydrates": 5,
        "protein": 25,
        "calories": 400,
        "fat": 30,
        "ingredients": ["daging sapi", "santan", "bumbu rendang", "daun jeruk", "serai"]
    },
    {
        "name": "Bakso",
        "description": "Bola daging yang disajikan dengan kuah kaldu yang gurih.",
        "carbohydrates": 15,
        "protein": 20,
        "calories": 250,
        "fat": 10,
        "ingredients": ["daging sapi", "tepung tapioka", "bawang putih", "kaldu sapi", "mie"]
    },
    {
        "name": "Pempek",
        "description": "Makanan khas Palembang yang terbuat dari ikan dan sagu.",
        "carbohydrates": 35,
        "protein": 15,
        "calories": 300,
        "fat": 12,
        "ingredients": ["ikan tenggiri", "sagu", "cuka", "gula merah", "bawang putih"]
    },
    {
        "name": "Sate Ayam",
        "description": "Daging ayam yang ditusuk dan dibakar dengan bumbu kacang.",
        "carbohydrates": 10,
        "protein": 20,
        "calories": 220,
        "fat": 12,
        "ingredients": ["daging ayam", "bumbu kacang", "kecap manis", "bawang merah", "cabai"]
    },
    {
        "name": "Mie Goreng",
        "description": "Mie goreng dengan campuran sayuran dan daging.",
        "carbohydrates": 40,
        "protein": 10,
        "calories": 350,
        "fat": 15,
        "ingredients": ["mie", "sayuran", "daging ayam", "kecap manis", "bawang putih"]
    },
    {
        "name": "Nasi Uduk",
        "description": "Nasi yang dimasak dengan santan dan rempah-rempah.",
        "carbohydrates": 50,
        "protein": 8,
        "calories": 300,
        "fat": 10,
        "ingredients": ["nasi", "santan", "daun pandan", "serai", "bawang merah"]
    },
    {
        "name": "Ayam Goreng",
        "description": "Daging ayam yang digoreng hingga kering dan renyah.",
        "carbohydrates": 5,
        "protein": 25,
        "calories": 300,
        "fat": 20,
        "ingredients": ["daging ayam", "bumbu kuning", "tepung terigu", "minyak goreng"]
    }
]

@app.route('/api/foods', methods=['GET'])
def get_foods():
    return jsonify(foods)

if __name__ == '__main__':
    app.run(debug=True)
