from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import Min
from .models import Item
import json

def index(request):
    items = Item.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        items = items.filter(title__icontains=search_query) | items.filter(description__icontains=search_query)
    
    # Filter by type
    type_filter = request.GET.get('type', '')
    if type_filter:
        items = items.filter(type=type_filter)
    
    # Filter by market
    market_filter = request.GET.get('market', '')
    if market_filter:
        items = items.filter(market_name=market_filter)
    
    # Sort functionality
    sort_by = request.GET.get('sort', '')
    if sort_by == 'price_asc':
        items = items.order_by('price')
    elif sort_by == 'price_desc':
        items = items.order_by('-price')
    elif sort_by == 'name_asc':
        items = items.order_by('title')
    elif sort_by == 'name_desc':
        items = items.order_by('-title')
    elif sort_by == 'rating':
        items = items.order_by('-rating')
    
    # Get unique types and markets for filter dropdowns
    types = Item.objects.values_list('type', flat=True).distinct().order_by('type')
    markets = Item.objects.values_list('market_name', flat=True).distinct().order_by('market_name')
    
    # Find cheapest price for each item
    item_prices = {}
    for item in items:
        if item.title not in item_prices:
            item_prices[item.title] = {
                'min_price': item.price,
                'market': item.market_name
            }
        else:
            if item.price < item_prices[item.title]['min_price']:
                item_prices[item.title]['min_price'] = item.price
                item_prices[item.title]['market'] = item.market_name
    
    context = {
        'items': items,
        'types': types,
        'markets': markets,
        'current_type': type_filter,
        'current_market': market_filter,
        'current_sort': sort_by,
        'search_query': search_query,
        'item_prices': item_prices,
    }
    return render(request, 'market/index.html', context)

@csrf_exempt
@require_http_methods(["GET"])
def get_items(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def create_item(request):
    try:
        data = json.loads(request.body)
        item = Item.objects.create(
            title=data['title'],
            type=data['type'],
            description=data.get('description', ''),
            price=data['price'],
            rating=data.get('rating', 0)
        )
        return JsonResponse({'id': item.id, 'message': 'Item created successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    try:
        item = get_object_or_404(Item, id=item_id)
        data = json.loads(request.body)
        
        item.title = data.get('title', item.title)
        item.type = data.get('type', item.type)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        item.rating = data.get('rating', item.rating)
        
        item.save()
        return JsonResponse({'message': 'Item updated successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    try:
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
