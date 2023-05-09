from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, UpdateView
from django.contrib import messages

from accounts.forms import ProfileForm
from accounts.models import Profile


# Create your views here.
# FBV (profile)
# def profile(request):
#   return render(request, 'profile.html')
# CBV (Profile)
class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'profile.html'

profile = ProfileView.as_view()

# CBV (profile_edit) # pk 값이 할당이 안됨
# class ProfileUpdateView(UpdateView):
#   model = Profile
#   form_class = ProfileForm
#
# profile_edit = ProfileUpdateView.as_view()
# FBV (profile_edit) # 프로필이 언제 생성? 프로필이 user와 매칭해서 값이 있으면 정상적으로 profile 페이지가 뜨지만 없을때도 있다.
@login_required
def profile_edit(request):
  # profile = get_object_or_404(Profile)  # = Profile.objects.get(user=request.user)
  try: # 프로필이 있으면
    profile = request.user.profile
  except Profile.DoesNotExist: # 없으면
    profile = None

  if request.method == "POST":
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = request.user
      form.save()
      messages.info(request,'프로필 수정이 완료되었습니다.')
      return redirect('profile')
  else:
    form = ProfileForm(instance=profile)
    return render(request,'profile_form.html',{'form':form,'profile':profile})

