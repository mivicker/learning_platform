from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from django.contrib import messages
from .models import User

@login_required
def profile(request, user_id):
#could probably use a generic class based view for this. DetailView
	user = User.objects.get(id = user_id)

	context = {
		'own_profile' : user_id == request.user.id,
		'user': user,
		'role': user.get_role_display(),
		}

	return render(request, "users/profile.html", context)

@login_required
def update_profile(request):
	if request.method == 'POST':
		profile_form = ProfileUpdateForm(request.POST, instance = request.user)
		if profile_form.is_valid():
			profile_form.save()
			messages.success(request, 'Your profile has been updated!')
			return redirect('users:profile')

	else:
		profile_form = ProfileUpdateForm(instance=request.user)

	return render(request, 'users/update_profile.html', {
		'profile_form': profile_form
	})

@login_required
def community(request):
	buddies = request.user.buddy.all()
	context = {'buddies' : buddies}
	return render(request, 'users/community.html', context)
