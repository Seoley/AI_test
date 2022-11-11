from operator import le
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django.http import HttpResponse  
from django.views.generic import View
from django.urls import reverse
from django.conf import settings


from django.views.decorators.csrf import csrf_exempt

from django import forms

from .modules import CAtest, HFtest

import os


# Create your views here.

class index(View):  
    @csrf_exempt
    def get(self, request):
        # return HttpResponse('result')
        return render(request, 'CA.html')


class CA_model(View):  
    @csrf_exempt
    def get(self, request):
        try:
        # return HttpResponse('result')
            return render(request, 'CA.html')
        except:
            print("CA test 페이지 에러")
            return redirect('/main/CAtest/')
       
    
class CA_result(APIView):
    @csrf_exempt
    def post(self, request):
        # try:
            metrics = request.POST['metrics']
            file = request.FILES.__getitem__('file')
            length = request.POST['length']
            sets = request.POST['sets']

            controler = CAtest(metrics,length,sets,file)
            loss_list, metric_list, avg_loss, avg_metric, file_folder, file_list = controler.get_result()
            eval_list = []

            # 리스트 출력 https://wikidocs.net/111783
            avg_data = {'count': "평균", 'loss': avg_loss, 'metric': avg_metric}

            eval_list.append(avg_data)
            for i in range(len(loss_list)):

                eval_data = {'count': i,
                            'loss': loss_list[i],
                            'metric': metric_list[i],
                            'file_folder': file_folder,
                            'file_name': file_list[i]}
                eval_list.append(eval_data)
            
            context = {'length':length, 'sets': sets, 'eval_list': eval_list, 'avg_metric': avg_metric}
            response = render(request, 'CA.html', context)
            response.set_cookie(key='metrics', value=metrics)
            # response.set_cookie(key='file', value=file)
            response.set_cookie(key='length', value=length)
            response.set_cookie(key='sets', value=sets)
            print("부정맥 테스트 종료")

            return response
        # except:
        #     print("CA 페이지 에러")
        #     return redirect('/main/CAtest/')




class HF_model(View):  
    @csrf_exempt
    def get(self, request):
        try:
        # return HttpResponse('result')
            return render(request, 'HF.html')
        except:
            print("HF test 페이지 에러")
            return redirect('/main/HFtest/')
       

class HF_result(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            metrics = request.POST['metrics']
            file = request.FILES.__getitem__('file')
            length = request.POST['length']
            sets = request.POST['sets']

            controler = HFtest(metrics,length,sets,file)
            loss_list, metric_list, avg_loss, avg_metric, file_folder, file_list = controler.get_result()
            eval_list = []

            # 리스트 출력 https://wikidocs.net/111783
            avg_data = {'count': "평균", 'loss': avg_loss, 'metric': avg_metric}

            eval_list.append(avg_data)
            for i in range(len(loss_list)):

                eval_data = {'count': i,
                            'loss': loss_list[i],
                            'metric': metric_list[i],
                            'file_folder': file_folder,
                            'file_name': file_list[i]}
                eval_list.append(eval_data)
            
            context = {'length':length, 'sets': sets, 'eval_list': eval_list, 'avg_metric': avg_metric}
            response = render(request, 'HF.html', context)
            response.set_cookie(key='metrics', value=metrics)
            response.set_cookie(key='length', value=length)
            response.set_cookie(key='sets', value=sets)
            print("심부전 테스트 종료")

            return response
        except:
            print("HF 페이지 에러")
            return redirect('/main/HFtest/')

def file_download(request):
    # path = request.GET['path']
    file_folder = request.GET.get('file_folder')
    file_name = request.GET.get('file_name')

    path = file_folder+'/'+file_name+'.csv'
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    print(file_path)
    if os.path.exists(file_path):
        binary_file = open(file_path, 'rb')
        response = HttpResponse(binary_file.read(), content_type="application/octet-stream; charset=utf-8")
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
        return response
    else:
        message = '알 수 없는 오류가 발행하였습니다.'
        return HttpResponse("<script>alert('"+ message +"');history.back()'</script>")