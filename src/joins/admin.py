from django.contrib import admin

# Register your models here.
from .models import Join, Newsletter


class JoinAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'first_name','last_name','friend', 'timestamp', 'updated']
	class Meta:
		model = Join

class NewsletterAdmin(admin.ModelAdmin):
	list_display = ['__unicode__','active']
	class Meta:
		model = Newsletter

admin.site.register(Join, JoinAdmin)

admin.site.register(Newsletter,NewsletterAdmin)

