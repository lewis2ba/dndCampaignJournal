from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse


from .models import Campaign
# Create your views here.

def index(request):
	latest_campaigns_list = Campaign.objects.order_by('-start_date')
	context = {
		'latest_campaigns_list' : latest_campaigns_list
	}
	return render(request, 'campaigns/index.html',context)

def campaignDetail(request, campaign_id):
		campaign = get_object_or_404(Campaign, pk=campaign_id)
		return render(request, 'campaigns/detail.html', {'campaign': campaign})

def sessionsView(request, campaign_id):
	response = "You're looking at the sessions for the campaign %s."	
	return HttpResponse(response % campaign_id)

def sessionDetail(request, campaign_id, session_id):
	response = "You're looking at session %s."
	return HttpResponse(response % session_id)
 
