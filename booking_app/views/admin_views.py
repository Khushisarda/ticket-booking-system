from django.views import View
from booking_app.models import Show, Booking
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

@method_decorator(login_required, name='dispatch')
class AdminDashboardView(View):
    def get(self, request):
        if not request.user.is_admin:
            return redirect('home')  # Non-admins redirected to home page
        
        shows = Show.objects.all()
        bookings = Booking.objects.select_related('user', 'show')
        return render(request, 'admin_dashboard.html', {
            'shows': shows,
            'bookings': bookings
        })
    

@method_decorator(login_required, name='dispatch')
class ShowCreateView(View):
    def get(self, request):
        if not request.user.is_admin:
            return redirect('home')
        return render(request, 'create_show.html')

    def post(self, request):
        if not request.user.is_admin:
            return redirect('home')
        
        title = request.POST['title']
        description = request.POST['description']
        dt_str = request.POST['datetime']  # "YYYY-MM-DDTHH:MM"
        datetime_obj = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M')
        total_seats = int(request.POST['total_seats'])
        
        # Create the new show
        show = Show.objects.create(
            title=title,
            description=description,
            datetime=datetime_obj,
            total_seats=total_seats,
            available_seats=total_seats
        )
        return redirect('admin_dashboard')


@method_decorator(login_required, name='dispatch')
class ShowUpdateView(View):
    def get(self, request, show_id):
        if not request.user.is_admin:
            return redirect('home')
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'edit_show.html', { 'show': show })

    def post(self, request, show_id):
        if not request.user.is_admin:
            return redirect('home')
        show = get_object_or_404(Show, id=show_id)

        # Update fields from the form
        show.title           = request.POST['title']
        show.description     = request.POST['description']
        dt_str               = request.POST['datetime']  # "YYYY-MM-DDTHH:MM"
        show.datetime        = datetime.strptime(dt_str, '%Y-%m-%dT%H:%M')

        # Read both total and available seats explicitly
        show.total_seats     = int(request.POST['total_seats'])
        show.available_seats = int(request.POST['available_seats'])

        show.save()
        return redirect('admin_dashboard')
@method_decorator(login_required, name='dispatch')
class ShowDeleteView(View):
    def get(self, request, show_id):
        # Confirmation page
        if not request.user.is_admin:
            return redirect('home')
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'confirm_delete_show.html', { 'show': show })

    def post(self, request, show_id):
        # Handle the deletion
        if not request.user.is_admin:
            return redirect('home')
        show = get_object_or_404(Show, id=show_id)
        show.delete()
        return redirect('admin_dashboard')
 
class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_history.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).order_by('-booking_time')
    
