
from django.conf import settings
from django.db import models
from .utils import get_mailchimp_api
from django.db.models.signals import post_save
# Create your models here.

class Join(models.Model):
	first_name = models.CharField(max_length=75,null=True,blank=True)
	last_name = models.CharField(max_length=75,null=True,blank=True)
	email = models.EmailField()
	friend = models.ForeignKey("self", related_name='referral',
										null=True, blank=True)
	ref_id = models.CharField(max_length=120, default='ABC', unique=True)
	ip_address = models.CharField(max_length=120, default='ABC')
	timestamp = models.DateTimeField(auto_now_add = True, auto_now=False)
	updated = models.DateTimeField(auto_now_add = False, auto_now=True)

	def __unicode__(self):
		return "%s" %(self.email)

	class Meta:
		unique_together = ("email", "ref_id",)
#MailChimp 
class Newsletter(models.Model):
	user = models.OneToOneField(Join, on_delete=models.CASCADE,)
	active = models.BooleanField(default=True)

	def __unicode__(self):
		return "%s" %(self.user.email)

def verify_mailchimp(sender, instance, **kwargs):

	email = instance.user.email
	email = {"emails":{"email":email}}
	m = get_mailchimp_api()
	try:
		user_list = m.list.member_info('fef6ef8a08',email)
	except:
		user_list = False

	if user_list:
		for item in user_list['data']:
			try:
				if item['status'] == 'Unsubscribed':
					newsletter.active = False
					newsletter.save()
			except:
				pass
post_save.connect(verify_mailchimp, sender=Newsletter)

def add_remove_newsletter(sender, instance, **kwargs):
	email = {"email":instance.user.email}
	m = get_mailchimp_api()
	
	if not instance.active:
		m.lists.unsubscribe('fef6ef8a08', email,delete_member=False)
	else:
		m.lists.subscribe('fef6ef8a08', email, double_optin=True, update_existing=False, send_welcome=False)

post_save.connect(add_remove_newsletter, sender=Newsletter)