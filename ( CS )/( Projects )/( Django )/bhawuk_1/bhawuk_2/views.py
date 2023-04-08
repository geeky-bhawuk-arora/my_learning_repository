from django.shortcuts import render
from bhawuk_2.models import Services

# Create your views here.

def home(request):
    return render(request,"home.html")
    
def about(request):
    return render(request,"about.html")


def ro_creation(request):
    if request.method == 'POST':
        creation_date = request.POST.get('creation_date')
        serial_no = request.POST.get('serial_no')
        publication = request.POST.get('publication')
        client_name = request.POST.get('client_name')
        publish_edition = request.POST.get('publish_edition')
        publish_date = request.POST.get('publish_date')
        particulars = request.POST.get('particulars')
        publish_space_position = request.POST.get('publish_space_position')
        remarks = request.POST.get('remarks')
        publish_rate = request.POST.get('publish_rate')
        remarks = request.POST.get('remarks')
        ro_order_final = Services(
            creation_date = creation_date,
            serial_no = serial_no,
            publication = publication,
            client_name = client_name,
            publish_edition = publish_edition,
            publish_date = publish_date,
            particulars = particulars,
            publish_space_position = publish_space_position,
            publish_rate = publish_rate,
            remarks = remarks,
            )
        ro_order_final.save()
    else:
        return render(request,"services.html")


    

def support(request):
    return render(request,"support.html")



