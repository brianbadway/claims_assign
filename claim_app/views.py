from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string
import random

def index(request):
    return render(request, 'index.html')

def to_assign(request):
    return render(request, 'assign.html')

def create_policyholder(request):
    claim_number = f'{random.randint(100, 999)}-{random.randint(1000, 9999)}'
    return redirect('/adj_assign')

def adj_assign(request):

    return render(request, 'create_claim.html')

