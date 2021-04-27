from django.http import HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import time


def index(request):
    search_item = request.POST.get('productname')
    return render(request, 'index.html', {'search_item': search_item})


def search(request):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    if request.method == 'GET':
        qry = request.GET.get('productname')
        name1 = qry.replace(" ", "+")  # iphone x  -> iphone+x
        flipkart = f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(
            f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',
            headers=headers)
        soup = BeautifulSoup(res.text, 'html.parser')
        # New Class For Product Name
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()
        flipkart_price = soup.select('._1_WHN1')[0].getText().strip()
        flipkart_name = flipkart_name.upper()
        if qry.upper() in flipkart_name:
            # New Class For Product Price
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()
         # --------amazon------------------------------
        name2 = qry.replace(" ", "-")
        name3 = qry.replace(" ", "+")
        amazon = f'https://www.amazon.in/{name2}/s?k={name3}'
        res = requests.get(
            f'https://www.amazon.in/{name2}/s?k={name3}', headers=headers)
        print("\nSearching in amazon:")
        soup = BeautifulSoup(res.text, 'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        amazon_price = soup.select(
            '.a-price-whole')[0].getText().strip().upper()
        name = qry.upper()
        amazon_name = soup.select(
            '.a-color-base.a-text-normal')[0].getText().strip().upper()
        amazon_name = soup.select(
            '.a-color-base.a-text-normal')[0].getText().strip().upper()
        amazon_price = soup.select(
            '.a-price-whole')[0].getText().strip().upper()
      # -----------------------end------------------------------------

    # return HttpResponse('Flifkart Price:'+flipkart_price+' Amazon Price:' + amazon_price)
    return render(request, 'index.html', {'product_name': qry, 'flifkart_price': flipkart_price, 'amazon_price': amazon_price})


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
