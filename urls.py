from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from loans.models import Loan, UserAccount

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Uncomment the admin/doc line below to enable admin documentation:
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	(r'^admin/', include(admin.site.urls)),

	(r'^$', 'home'),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	# (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
	(r'^accounts/logout/$', 'loans.views.logout_view'),
)

urlpatterns += patterns('loans.views',
	# url(r'^loans/$',
	#	  ListView.as_view(
	#		  queryset = Loan.objects.all().order_by('-signing_date')[:20],
	#		  context_object_name='loans',
	#		  template_name = 'loans/loans.html')),
	# url(r'^loans/(?P<pk>\d+)/$',
	#	  DetailView.as_view(
	#		  model = Loan,
	#		  template_name = 'loans/loan_detail.html')),
		
	(r'^loans/$', 'loans'),
	(r'^loans/(?P<loan_id>\d+)/$', 'loan_detail'),
	(r'^accounts/profile/$', 'user_profile')
)