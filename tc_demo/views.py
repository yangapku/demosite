from django.shortcuts import render
from django.http import HttpResponse

FilePath='D:\\demosite\\tc_demo\\rawdata\\srcfile\\'
ResultPath='D:\\demosite\\tc_demo\\rawdata\\resultfile\\'
# Create your views here.
def index(request):
	return render(request,'tc_demo/index.html',{
		'input_word':'Powered by Bootstrap and Django'
	})

def getfile(request):
	inputid=request.GET['id']
	text=open(FilePath+str(inputid)+'.json',encoding='utf-8').read()
	return HttpResponse(text)

def getresult(request):
	fileid=request.GET['id']
	text=open(ResultPath+'res_'+str(fileid)+'.txt',encoding='utf-8').read()
	return HttpResponse(text)