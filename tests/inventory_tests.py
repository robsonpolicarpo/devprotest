from main.inventory.list_products import sort_list


def test_list_products_by_name():
    prods = [
        {"name": "Product C", "price": 100, "stock": 5},
        {"name": "Product A", "price": 200, "stock": 3},
        {"name": "Product B", "price": 50, "stock": 1}
    ]

    sorted_list = sort_list(prods, 'name')
    assert sorted_list[0].get('name') == 'Product A'
    assert sorted_list[1].get('name') == 'Product B'
    assert sorted_list[2].get('name') == 'Product C'

    sorted_list = sort_list(prods, 'name', False)
    assert sorted_list[0].get('name') == 'Product C'
    assert sorted_list[1].get('name') == 'Product B'
    assert sorted_list[2].get('name') == 'Product A'


def test_list_products_by_price():
    prods = [
        {"name": "Product C", "price": 100, "stock": 5},
        {"name": "Product A", "price": 200, "stock": 3},
        {"name": "Product B", "price": 50, "stock": 1}
    ]

    sorted_list = sort_list(prods, 'price')
    assert sorted_list[0].get('price') == 50
    assert sorted_list[1].get('price') == 100
    assert sorted_list[2].get('price') == 200

    sorted_list = sort_list(prods, 'price', False)
    assert sorted_list[0].get('price') == 200
    assert sorted_list[1].get('price') == 100
    assert sorted_list[2].get('price') == 50


def test_list_products_by_stock():
    prods = [
        {"name": "Product C", "price": 100, "stock": 5},
        {"name": "Product A", "price": 200, "stock": 3},
        {"name": "Product B", "price": 50, "stock": 1}
    ]

    sorted_list = sort_list(prods, 'stock')
    assert sorted_list[0].get('stock') == 1
    assert sorted_list[1].get('stock') == 3
    assert sorted_list[2].get('stock') == 5

    sorted_list = sort_list(prods, 'stock', False)
    assert sorted_list[0].get('stock') == 5
    assert sorted_list[1].get('stock') == 3
    assert sorted_list[2].get('stock') == 1


def test_list_products_without_sort_key():
    prods = [
        {"name": "Product C", "price": 100, "stock": 5},
        {"name": "Product A", "price": 200, "stock": 3},
        {"name": "Product B", "price": 50, "stock": 1}
    ]

    sorted_list = sort_list(prods, '')
    assert sorted_list[0].get('name') == 'Product A'
    assert sorted_list[1].get('name') == 'Product B'
    assert sorted_list[2].get('name') == 'Product C'


def test_list_products_empty_list():
    prods = []

    sorted_list = sort_list(prods, '')
    assert not sorted_list
