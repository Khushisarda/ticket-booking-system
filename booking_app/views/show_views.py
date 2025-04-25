from django.views import View
from django.shortcuts import render
from booking_app.models import Show

class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all().order_by('datetime')
        return render(request, 'show_list.html', { 'shows': shows })

