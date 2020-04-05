from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .models import Campaign, Session
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

def sessionNew(request, campaign_id):
	campaign = get_object_or_404(Campaign, pk=campaign_id)
	session = campaign.session_set.create(date =request.POST['sessionDate'],description=request.POST['sessionDescr'])
	session.save()
	return HttpResponseRedirect(reverse('campaigns:campaignDetail', args=(campaign.id,)))

def sessionDetail(request, campaign_id, session_id): 
	campaign = get_object_or_404(Campaign, pk=campaign_id)
	session = get_object_or_404(Session, pk=session_id)
	return render(request, 'sessions/detail.html', {'campaign': campaign,'session': session})
 
