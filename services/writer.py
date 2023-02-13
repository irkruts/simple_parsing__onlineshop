import json


def json_writer(name, price, text, url_img):
    try:
        data_json = json.load(open("data.json"))
    except: # noqa E722
        data_json = []
    data_json.append({"name": name, "price": price, "text": text, "url_img": url_img})
    with open("data.json", "w") as f:
        json.dump(data_json, f, indent=2)
