from flask import render_template, request
import math
from eapp import app, dao


@app.route('/')
def index():
    categories = dao.load_categories()
    products = dao.load_products(
        kw=request.args.get('kw'),
        cate_id=request.args.get('category_id'),
        page=int(request.args.get('page', 1))
    )


    # kw =
    # if kw:
    #     products = [p for p in products if p['name'].find(kw) >= 0]
    page_size = app.config['PAGE_SIZE']
    return render_template('index.html', products=products ,
                           page =math.ceil(dao.count_products()/page_size))

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')


if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)

@app.context_processor
def common_responses():
    return {
        'categories':dao.load_categories()
    }
if __name__ == '__main__':
    with app.app_context():
        from eapp import admin
        app.run(debug=True)