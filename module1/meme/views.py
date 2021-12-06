# this stuff is for csv model
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
#this stuff is for displaying dashboard
from .new import *
# this stuff is for login logout
from django.shortcuts import render, HttpResponse, redirect
from meme.models import datacsv, signup
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate,login


# Create your views here.
def index(request):
    context = {
        "variable1":"This is sent",
        "variable2":"Rohan is great"
    }

    return render(request, 'index.html', context)
    #return HttpResponse("This is homepage.")


def about(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        symbol = symbol.upper()
    else:
        symbol = 'BTCUSD'

    data = spotquote(symbol)
    pricedata = pricechange(symbol)
    moredata = pricechange(symbol)


    ts_df = candles(symbol)

    #PlotlyGraph
    def candlestick():
        figure = go.Figure(
            data = [
                    go.Candlestick(
                      x = ts_df.index,
                      high = ts_df['high'],
                      low = ts_df['low'],
                      open = ts_df['open'],
                      close = ts_df['close'],
                    )
                  ]
        )

        candlestick_div = plot(figure, output_type='div')
        return candlestick_div
    #endPlotlyGraph
    percentchange = pricedata['priceChangePercent']
    buyers = pricedata['askQty']
    sellers = pricedata['bidQty']

    eth = pricechange(symbol='ETHUSD')
    btc = pricechange(symbol="BTCUSD")
    ltc = pricechange(symbol="LTCUSD")

    context={
    'moredata': moredata,
    'eth': eth,
    'btc': btc,
    'ltc': ltc,
    'percentchange': percentchange,
    'buyers': buyers,
    'sellers': sellers,
    'data': data,
    'candlestick': candlestick(),
    }
    return render(request, 'about.html', context)

    #return render(request, 'about.html')
    #return HttpResponse("This is about page.")   


def product(request):
     return render(request, 'product.html')
    #return HttpResponse("This is product page.")

def contact(request):
     return render(request, 'contact.html')
    #return HttpResponse("This is contact page.")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
                   
        print(username, password)
        #check if user has entered correct crendentials
        user = authenticate(username=username, password=password)
        if user is not None:
          # A backend authenticated the credentials
          login(request,user,password)
          return redirect("/loggedin")
        else:
          # No backend authenticated the credentials
          return redirect(request,"login.html" )
    return render(request, 'login.html')
    #return HttpResponse("This is login page.")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        checkbox = request.POST.get('checkbox')
        signup = signup (username=username, password=password, checkbox=checkbox)
        signup.save()
    return render(request, 'signup.html')
    #return HttpResponse("This is signup page.")

def loggedin(request):
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'loggedin.html')
    #return HttpResponse("This is login page.")

def loggedout(request):
    logout(request)
    return redirect("/login")
    #return HttpResponse("This is login page.")

#csv file code

@permission_required('admin.can_add_log_entry')
def dataupload(request):
    template="dataupload.html"

    prompt={
        'order':'order of csv should be symbol,name,last_sale,net_change,country,industry'
    }

    if request.method == "GET":
        return render(request, template, prompt)
     
    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    
    data_set= csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _,  created = datacsv.objects.update_or_create(
            symbol=column[0],
            name=column[1],
            last_sale=column[2],
            net_change=column[3],
            #percentage_change=column[4],
            country=column[4],
            industry=column[5],
        )

    context = {}  
    return render(request, template, context)


    #post csv data

    







