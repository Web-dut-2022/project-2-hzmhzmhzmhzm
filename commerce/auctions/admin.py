from django.contrib import admin
from .models import AuctionsListings, BidRecord, Comments, Watched, User

# Register your models here.
admin.site.register(AuctionsListings)
admin.site.register(BidRecord)
admin.site.register(Comments)
admin.site.register(Watched)
admin.site.register(User)