from django.shortcuts import render,get_object_or_404
from .models import User_all_data



def Homepage(request):
    
    users = User_all_data.objects.all()  # Fetch all user data
    return render(request, 'Home.html', {'users': users})




def user_detail(request, pk):
    user = get_object_or_404(User_all_data, pk=pk)
    return render(request, 'data.html', {'user': user})
