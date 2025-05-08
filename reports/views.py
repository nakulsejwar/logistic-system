from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from django.db.models import Count, Sum
from parcels.models import Parcel
from drivers.models import Driver
from vehicles.models import Vehicle
from products.models import Product

class SystemReportView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data = {
            "total_parcels": Parcel.objects.count(),
            "pending_parcels": Parcel.objects.filter(status="pending").count(),
            "delivered_parcels": Parcel.objects.filter(status="delivered").count(),
            "drivers_count": Driver.objects.count(),
            "vehicles_count": Vehicle.objects.count(),
            "available_vehicles": Vehicle.objects.filter(is_available=True).count(),
            "total_stock_items": Product.objects.aggregate(total=Sum("stock_quantity"))["total"],
        }
        return Response(data)
