from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def profile(request):
    return render(request, 'page/profile.html')

def receipt(request):
    status = request.GET.get('status')
    
    if status == 'processing':
        return render(request, 'page/receiptProcessing.html')
    elif status == 'completed':
        return render(request, 'page/receiptCompleted.html')
    elif status == 'cancel':
        return render(request, 'page/receiptCancel.html')
    else:
        return render(request, 'page/receipt.html')

def receiptdetails(request):
    return render(request, 'page/receiptdetails.html')