from django.http import JsonResponse
from django.views.decorators.http import require_GET

from .data import PRODUCTS, STORES


@require_GET
def health(request):
    return JsonResponse({"status": "ok", "service": "MarketHouse API"})


@require_GET
def stores(request):
    return JsonResponse({"stores": STORES})


@require_GET
def products(request):
    store_id = request.GET.get("store")
    items = PRODUCTS
    if store_id:
        items = [product for product in PRODUCTS if product["storeId"] == store_id]
    return JsonResponse({"products": items})


@require_GET
def catalog(request):
    return JsonResponse({"stores": STORES, "products": PRODUCTS})
