from django.shortcuts import render
def home(request):
    total=None
    gst_amount=None
    if request.method=="POST":
        price=float(request.POST.get("price"))
        gst=float(request.POST.get("gst"))
        gst_amount=(price*gst)/100
        total=price+gst_amount

    return render(request, 'home.html', {'total': total, 'gst_amount': gst_amount})
