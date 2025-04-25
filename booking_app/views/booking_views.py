from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from booking_app.models import Show, Booking

class BookingView(View):
    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        return render(request, 'booking_form.html', { 'show': show })

    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats_requested = int(request.POST['seats_booked'])

        if seats_requested <= show.available_seats:
            show.available_seats -= seats_requested
            show.save()
            Booking.objects.create(
                user=request.user,
                show=show,
                seats_booked=seats_requested
            )
            return redirect('show_list')
        else:
            error = 'Only %d seats left' % show.available_seats
            return render(request, 'booking_form.html', { 'show': show, 'error': error })
class BookingHistoryView(View):
    def get(self, request):
       
        if not request.user.is_authenticated:
            return redirect('login')
        
        bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')
        return render(request, 'booking_history.html', { 'bookings': bookings })

