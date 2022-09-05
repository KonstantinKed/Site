from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory, Pics
from .form import CreateItemForm, CreateBrandForm, UpdateItemForm, UploadPicsForm, ApartmentSelectForm
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def control(request):
    items = Inventory.objects.all()
    context = {'items': items}
    return render(request, 'sidebar.html', context=context)

def items(request):
    items = Inventory.objects.all()
    for item in items:
        pics = Pics.objects.filter(invent = item.id)
    if request.method == 'POST':
        apt_form = ApartmentSelectForm(request.POST) # apartment form to select in items page
        if apt_form.is_valid():
            items = Inventory.objects.filter(apt=apt_form.cleaned_data['apt'])  # selecting items according to selected apartment
    else:
        apt_form = ApartmentSelectForm()
    context = {'items': items, 'apt_form': apt_form}
    return render(request, 'items.html', context=context)

def create_item(request):
    if request.method == 'POST':
        item_form = CreateItemForm(request.POST)
        pic_form = UploadPicsForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save()
            uploaded_img = pic_form.save(commit=False)
            for img in request.FILES.getlist('images'):
                Pics.objects.create(img=img, invent=item)
                # pic_form.cleaned_data['img']
                # uploaded_img.img = img
                # # invent = get_object_or_404(Inventory, id=form.cleaned_data['invent_id'])
                # uploaded_img.invent = item
                # uploaded_img.save()
            return HttpResponseRedirect('/items')
    else:
        item_form = CreateItemForm()
        pic_form = UploadPicsForm()
    context = {'item_form': item_form, 'pic_form': pic_form}
    return render(request, 'create_item.html', context)

# Adding new brands to the list of brands
def create_brand(request):
    if request.method == 'POST':
        brand_form = CreateBrandForm(request.POST)
        if brand_form.is_valid():
            brand = brand_form.save()
            return HttpResponseRedirect('/items')
    else:
        brand_form = CreateBrandForm()
    return render(request, 'create_brand.html', {'brand_form': brand_form})

def view_item(request, id):
    instance = get_object_or_404(Inventory, id=id)
    pics = Pics.objects.filter(invent = id)
    # for item in instance:
    #     pics = Pics.objects.filter(invent = item.id)
    # if request.method == 'POST':
    #     form = UpdateItemForm(request.POST, instance=instance)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/items')
    # else:
    # form = UpdateItemForm(None, instance=instance)
    return render(request, 'view_item.html', {'instance': instance, 'pics': pics})

def update_item(request, id):
    instance = get_object_or_404(Inventory, id=id)
    if request.method == 'POST':
        form = UpdateItemForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/items')
    else:
        form = UpdateItemForm(None, instance=instance)
        pics = Pics.objects.filter(invent = id)
    return render(request, 'update_item.html', {'form': form, 'pics': pics})


def delete_item(request, id):
    instance = get_object_or_404(Inventory, id=id)
    instance.delete()
    return HttpResponseRedirect('/items')


def upload_pics(request):
    if request.method == 'POST':
        form = UploadPicsForm(request.POST, request.FILES)
        print(form.data)
        if form.is_valid():
            uploaded_img = form.save(commit=False)
            uploaded_img.image_data = form.cleaned_data['img'].file.read()
            invent = Inventory.objects.filter(invent_id = form.cleaned_data['invent_id']).first()
            # invent = get_object_or_404(Inventory, invent_id=form.cleaned_data['invent_id'])
            uploaded_img.invent_id = invent
            uploaded_img.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadPicsForm()
    return render(request, 'upload_pics.html', {'form': form})


