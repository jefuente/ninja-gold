from django.shortcuts import render, redirect
from random import randint
from datetime import datetime
import random
import time

def randInt(min=0,max=100):
	num = (random.random() * (max-min)+min)
	return round(num)
	print(randInt(10,20))

def home(request):
    contexto = {
        "oro":0,
        "logs":[]
    }
    if 'oro' in request.session:
        contexto['oro']=request.session['oro'];
    if 'log' in request.session:
        contexto['logs']=request.session['log'];    


    return render(request, 'home.html', contexto)


def procesar(request):


    if request.method == 'POST':
        print(request.POST)
        if 'log' not in request.session:
            request.session['log'] = []

        if request.POST['valor']=="granja":
            variacion = randInt(10,20)
            request.session['oro'] = request.session['oro'] + variacion
            datos_a_entregar = {
                'texto' : f"Entraste a {request.POST['valor']} y ganaste {variacion} monedas de oro a las {time.strftime('%H:%M:%S del dia %d-%m-%Y ', time.localtime())}",
                'color' : 'verde'
            }
            request.session['log'].append(datos_a_entregar)
            request.session.save()
            

        if request.POST['valor']=="cueva":
            variacion = randInt(5,10)
            request.session['oro'] = request.session['oro'] + variacion
            datos_a_entregar = {
                'texto' : f"Entraste a {request.POST['valor']} y ganaste {variacion} monedas de oro a las {time.strftime('%H:%M:%S del dia %d-%m-%Y ', time.localtime())}",
                'color' : 'verde'
            }
            request.session['log'].append(datos_a_entregar)
            request.session.save()
            
        

        if request.POST['valor']=="casa":
            variacion = randInt(2,5)
            request.session['oro'] = request.session['oro'] + variacion
            datos_a_entregar = {
                'texto' : f"Entraste a {request.POST['valor']} y ganaste {variacion} monedas de oro a las {time.strftime('%H:%M:%S del dia %d-%m-%Y ', time.localtime())}",
                'color' : 'verde'
            }
            request.session['log'].append(datos_a_entregar)
            request.session.save()
            
           

        if request.POST['valor']=="casino":
            variacion = randInt(-50,50)
            if variacion >=0:
                request.session['oro'] = request.session['oro'] + variacion
                datos_a_entregar = {
                    'texto' : f"Entraste a {request.POST['valor']} y ganaste {variacion} monedas de oro a las {time.strftime('%H:%M:%S del dia %d-%m-%Y ', time.localtime())}",
                    'color' : 'verde'
                }
                request.session['log'].append(datos_a_entregar)
                request.session.save()

            if variacion<0:
                request.session['oro'] = request.session['oro'] + variacion
                datos_a_entregar = {
                    'texto' : f"Entraste a {request.POST['valor']} y perdiste {variacion} monedas de oro a las {time.strftime('%H:%M:%S del dia %d-%m-%Y ', time.localtime())}",
                    'color' : 'rojo'
                }
                request.session['log'].append(datos_a_entregar)
                request.session.save()
           

        return redirect('/')

def limpiar(request):
    request.session['oro']=0
    request.session['log'] = []
    print("Datos limpios")
    return redirect('/')