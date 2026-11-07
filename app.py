from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    company_name = "Logistics A+"
    tagline = "Vững bước kho vận – Bứt phá tương lai"
    return render_template('index.html', company_name=company_name, tagline=tagline)

@app.route('/gioi-thieu')
def about():
    # Trang giới thiệu riêng khi click vào menu Giới thiệu
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
