from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def listings(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)
    paginator=Paginator(listings,6)
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    # listings=Listing.objects.all().filter(is_published=True).order_by('-list_date')
    context = {"listings": paged_listings}
    return render(request, 'listings/listings.html', context)
    # return render(request, 'listings/listings.html', {'name': 'Medical Center Listings'})  

def listing(request,listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {"listing":listing}
    return render(request, 'listings/listing.html',context)

def search(request):
    return render(request, 'listings/search.html')