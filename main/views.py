from operator import le
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import HttpResponse  
from django.views.generic import View
from django.urls import reverse

from django.views.decorators.csrf import csrf_exempt

from django import forms

from .modules import CAtest, HFtest


# Create your views here.

class index(View):  
    @csrf_exempt
    def get(self, request):
        # return HttpResponse('result')
        return render(request, 'CA.html')


class CA_model(View):  
    @csrf_exempt
    def get(self, request):
        # return HttpResponse('result')
        return render(request, 'CA.html')
    
class CA_result(APIView):
    @csrf_exempt
    def post(self, request):
        metrics = request.POST['metrics']
        file = request.FILES.__getitem__('file')
        length = request.POST['length']
        sets = request.POST['sets']

        controler = CAtest(metrics,length,sets,file)
        loss_list, metric_list, avg_loss, avg_metric = controler.get_result()
        eval_list = []

        # 리스트 출력 https://wikidocs.net/111783
        avg_data = {'count': "평균", 'loss': avg_loss, 'metric': avg_metric}

        eval_list.append(avg_data)
        for i in range(len(loss_list)):
            eval_data = {'count': i,
                        'loss': loss_list[i],
                        'metric': metric_list[i]}
            eval_list.append(eval_data)
        

        context = {'eval_list': eval_list, 'avg_metric': avg_metric}

        return render(request, 'CA.html', context)


class HF_model(View):  
    @csrf_exempt
    def get(self, request):
        # return HttpResponse('result')
        return render(request, 'HF.html')
       

class HF_result(APIView):
    @csrf_exempt
    def post(self, request):
        metrics = request.POST['metrics']
        file = request.FILES.__getitem__('file')
        length = request.POST['length']
        sets = request.POST['sets']

        controler = HFtest(metrics,length,sets,file)
        loss_list, metric_list, avg_loss, avg_metric = controler.get_result()
        eval_list = []

        # 리스트 출력 https://wikidocs.net/111783
        avg_data = {'count': "평균", 'loss': avg_loss, 'metric': avg_metric}

        eval_list.append(avg_data)
        for i in range(len(loss_list)):
            eval_data = {'count': i,
                        'loss': loss_list[i],
                        'metric': metric_list[i]}
            eval_list.append(eval_data)
        

        context = {'eval_list': eval_list, 'avg_metric': avg_metric}

        return render(request, 'HF.html', context)