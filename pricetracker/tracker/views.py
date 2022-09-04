from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from .models import Item,Itemprices
from .forms import AddLinkForm, AddNewPrice
from .scrape import get_link_data

# Create your views here.

class ItemListView(View):
    def get (self, request, *args, **kwargs):

        no_discounted = 0
        error = None

        form = AddLinkForm(request.POST)

        if request.method == 'POST':
            try:
                if form.is_valid():
                    form.save()
            except AttributeError:
                error = "couldn't get the name or the price"
            except:
                error = "something went wrong"

        form = AddLinkForm()

        items = Item.objects.all().order_by('price_difference', 'created')
        items_no = items.count()

        if items_no > 0:
            discount_list = []
            for item in items:
                if item.old_price > item.current_price:
                    discount_list.append(item)
                no_discounted = len(discount_list)

        context = {
            'item_list': items,
            'items_no': items_no,
            'no_discounted': no_discounted,
            'form': form,
            'error': error,
        }
        return render (request, 'tracker/item_list.html' , context )

    def post (self, request, *args, **kwargs):
        items = Item.objects.all().order_by('price_difference', 'created')
        form = AddLinkForm(request.POST)
        if form.is_valid():
            
            new_item =form.save(commit=False)
            name, price, imageurl = get_link_data(new_item.url)
            
            new_item.name = name
            new_item.current_price = price
            new_item.price1 = price * 0.8
            new_item.price2 = price * 1.2
            new_item.price3 = price * 0.7
            new_item.imageurl = imageurl
            new_item.poster = request.user
            new_item.save()
        
        context = {
            'item_list': items,
            'form': form,

        }
        return render (request, 'tracker/item_list.html' , context )

class ItemDetailView(View):
    def get (self, request, pk, *args,**kwargs):
        item = Item.objects.get(pk=pk)

        context = {
            'item' : item
        }

        return render (request, 'tracker/item_detail.html' , context )

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'tracker/del_confirm.html'
    success_url = reverse_lazy('item-list')


def update_prices(request):
    item = Item.objects.all()

    for items in item:
        items.save()

    context = {
        'item' : item
    }
    return redirect('item-list')
