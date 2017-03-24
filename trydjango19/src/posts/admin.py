from django.contrib import admin

# Register your models here.
from .models import post

class PostModelAdmin(admin.ModelAdmin):

	list_display =["title","updated","timestamp"]
	list_display_links = ["updated"]
	search_fields = ["content","title"]
	list_filter = ["updated","timestamp"]
	class Meta:

		model = post


admin.site.register(post,PostModelAdmin)
