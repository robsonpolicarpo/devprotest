def sort_list(products: [], sort_key: str, ascending: bool = True):
    if not sort_key and products:
        sort_key = list(products[0].keys())[0]

    if ascending:
        return sorted(products, key=lambda d: d[sort_key])

    return sorted(products, key=lambda d: d[sort_key], reverse=True)
