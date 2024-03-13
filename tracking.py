import requests
from bs4 import BeautifulSoup

products_to_track = [
    {
        "product_url": "https://www.amazon.in/Samsung-Storage-Expandable-MediaTek-Dimensity/dp/B0CP7WCMB3/ref=sr_1_4?crid=290LX8DUO6V8H&dib=eyJ2IjoiMSJ9.mZy5d08cqNFO-4MZK3GCu9zfYOnrrNUXAqwGjp3B-lLGQRWGdmtjWDXU-ay1KEa9cVAlyq03qRSwKVTk9C2EQEe7VKPrKe_bXPPpsZf0mE1S6Z18saoO8XKRAgRjlx2qUhd870p6l4b7yE0DR6zrcuOf9g6h_v1dwwmg-F45vzD8meFNntfrk6G_SAQFvDFJeZaAEnN_CnV8tPlS2Mi4rfwrqr3u7JEhkX6i1a2RkxoyQgOC6RFm2NUDanTAL4UPFBZe8MyanHLs1Yoq5yzPvVQwekxQeRxwYOYDl3xb4v8.4PujOH06OZO_JNSgmcrZl502dzuMfNlb7G9D6GazUeg&dib_tag=se&keywords=SAMSUNG&qid=1709676457&refinements=p_89%3ASamsung%2Cp_36%3A1318506031&rnid=1318502031&s=electronics&sprefix=samsung+%2Caps%2C1393&sr=1-4",
         "name" : "Samsung Galaxy A15  ",
         "target_price": 19000
    },
    {
        "product_url": "https://www.amazon.in/Samsung-Galaxy-Light-128GB-Storage/dp/B0BS193NXQ/ref=sr_1_20?crid=290LX8DUO6V8H&dib=eyJ2IjoiMSJ9.s1zqEg21bzmlWSn4k16if-xt9-OseEw_W09LvQlDo4d2WR7_blQNJQ3sCtCwqN04Y5VLZr6hnws5rYhd5BsGOoiyfikWQ4DJmcVnIBjaywx9y4U5QJlC7LIU01TfWYY3ByUZVj-ar08wSMHDAdPRvlRnM0NDyhaLLmT_nn8FXKlm8XSG8a6qrMZ4LRP_qqQQO3_2AmBZ0CYW2m3AX2ZRsMLRhUV1PbUm3dpgHc5Mwl0-fakwvdB4KUkrH8NhIUEV3jhHoNAFSO-cXfermnAhQDovU33-3Of92KcVYBhmiKc.3bGEffl5VP37aC0mqlZvR4M34Ov0U-Mg1Lg8D2OKIQs&dib_tag=se&keywords=SAMSUNG&qid=1709676811&refinements=p_89%3ASamsung%2Cp_36%3A1318507031&rnid=1318502031&s=electronics&sprefix=samsung+%2Caps%2C1393&sr=1-20",
        "name": "Samsung Galaxy A23 ",
        "target_price": 20000
    },
    {
        "product_url": "https://www.amazon.in/Samsung-sAMOLED-Display-Battery-Security/dp/B0CHJ59XBG/ref=sr_1_3?crid=290LX8DUO6V8H&dib=eyJ2IjoiMSJ9.mZy5d08cqNFO-4MZK3GCu9zfYOnrrNUXAqwGjp3B-lLGQRWGdmtjWDXU-ay1KEa9cVAlyq03qRSwKVTk9C2EQEe7VKPrKe_bXPPpsZf0mE1S6Z18saoO8XKRAgRjlx2qUhd870p6l4b7yE0DR6zrcuOf9g6h_v1dwwmg-F45vzD8meFNntfrk6G_SAQFvDFJeZaAEnN_CnV8tPlS2Mi4rfwrqr3u7JEhkX6i1a2RkxoyQgOC6RFm2NUDanTAL4UPFBZe8MyanHLs1Yoq5yzPvVQwekxQeRxwYOYDl3xb4v8.4PujOH06OZO_JNSgmcrZl502dzuMfNlb7G9D6GazUeg&dib_tag=se&keywords=SAMSUNG&qid=1709676457&refinements=p_89%3ASamsung%2Cp_36%3A1318506031&rnid=1318502031&s=electronics&sprefix=samsung+%2Caps%2C1393&sr=1-3",
        "name": "Samsung Galaxy M34",
        "target_price": 19000

    }

]

def give_product_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    product_price = soup.find(class_="a-price-whole")


    return product_price.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        product_price_returned = give_product_price(every_product.get("product_url"))
        print(product_price_returned + " - " + every_product.get("name"))

        my_product_price = product_price_returned[2:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get(
                "name") + ' -  \t' + ' Available at Target Price ' + ' Current Price - ' + str(
                my_product_price) + '\n')

        else:
            print("Still at current price")

finally:
    result_file.close()














