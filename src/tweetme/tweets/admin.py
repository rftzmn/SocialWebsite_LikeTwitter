from django.contrib import admin
from .forms import TweetModelForm
from .models import Tweet

# Register your models here.
# admin.site.register(Tweet)

class TweetModelAdmin(admin.ModelAdmin):
	# form = TweetModelForm
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetModelAdmin)