import json
import requests
from bs4 import BeautifulSoup

start_url = 'https://ordi.eu/lauaarvutid'


def parse(start_urls):
    """
    Main function to parse out items from given url.

    :param start_urls: string
    :return: None
    """
    page = requests.get(start_urls)
    soup = BeautifulSoup(page.text, 'html.parser')
    product_list_1 = soup.find_all("li", class_='item first')
    product_list_2 = soup.find_all("li", class_='item')
    product_list_3 = soup.find_all("li", class_='item last')

    itemlist = []

    for product in product_list_1:
        data = {'productName': '', 'Price': '', 'Picture href': ''}
        h2 = product.find('h2', class_="product-name")
        data['productName'] = h2.find('a').get_text()
        data['Price'] = product.find('span', class_="price").text
        data['Picture href'] = product.find('img')['src']
        itemlist.append(data)
    for product in product_list_2:
        data = {'productName': '', 'Price': '', 'Picture href': ''}
        h2 = product.find('h2', class_="product-name")
        data['productName'] = h2.find('a').get_text()
        data['Price'] = product.find('span', class_="price").text
        data['Picture href'] = product.find('img')['src']
        itemlist.append(data)
    for product in product_list_3:
        data = {'productName': '', 'Price': '', 'Picture href': ''}
        h2 = product.find('h2', class_="product-name")
        data['productName'] = h2.find('a').get_text()
        data['Price'] = product.find('span', class_="price").text
        data['Picture href'] = product.find('img')['src']
        itemlist.append(data)

    try:
        # find next button link
        next_page = soup.find("a", class_='next')['href']
        if next_page:
            print("parsing next page")
            write_data(itemlist)
            parse(next_page)
    except:
        write_data(itemlist)
        print("No more pages")


def write_data(itemlist):
    """
    Function to write given data to json file.

    :param itemlist: list of dicts.
    :return: None
    """
    with open('computers.txt', 'w') as json_file:
        print(len(itemlist))
        for item in itemlist:
            json.dump(item, json_file)


if __name__ == '__main__':
    parse(start_url)
