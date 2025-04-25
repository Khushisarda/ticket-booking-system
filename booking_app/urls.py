from django.urls import path
from .views.home import HomeView
from .views.auth_views import RegisterView, LoginView, LogoutView
from .views.show_views import ShowListView
from .views.booking_views import BookingView, BookingHistoryView
from .views.admin_views import AdminDashboardView, ShowCreateView
from .views.admin_views import ShowUpdateView
from .views.admin_views import ShowDeleteView
from .views.admin_views import BookingHistoryView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),                    
    path('register/', RegisterView.as_view(), name='register'),   
    path('login/', LoginView.as_view(), name='login'),     
    path('logout/', LogoutView.as_view(), name='logout'),      
    path('admin-dashboard/shows/add/', ShowCreateView.as_view(), name='add_show'),
    path('shows/', ShowListView.as_view(), name='show_list'),  
    path('book/<int:show_id>/', BookingView.as_view(), name='book_show'),  
    path('history/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin-dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin-dashboard/shows/edit/<int:show_id>/', ShowUpdateView.as_view(), name='edit_show'),
    path('admin/create_show/', ShowCreateView.as_view(), name='create_show'),
    path('booking-history/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin-dashboard/shows/delete/<int:show_id>/', ShowDeleteView.as_view(), name='delete_show'),
]

