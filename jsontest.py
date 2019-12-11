def add(args):
    with open('pricedata.json', mode='a+', encoding='utf-8')as feedsjson:
        feeds = json.load(feedsjson)
    with open('pricedata.json', mode='a+', encoding='utf-8')as feedsjson:
        entry = {}
        entry['name'] = args.name
        entry['url'] = args.url
        json.dump(entry, feedsjson)



def add(args):
    with open('pricedata.json', mode='a+', encoding='utf-8')as feedsjson:
        entry = {}
        list_prices.append(entry)
        entry['time'] = args.time
        entry['price'] = args.price
        json.dump(list_prices, feedsjson)

        with open('pricedata.json', mode='w', encoding='utf-8') as f:

            json.dump([], f)