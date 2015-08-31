from django.views.generic import DetailView
from common.mixins import LoginRequiredMixin
from .models import UserProfile
# Create your views here.


class ProfileView(LoginRequiredMixin, DetailView):
        template_name = 'account/profile.html'
        context_object_name = 'user_profile'

        def get_object(self, queryset=None):
            authentication_user = self.request.user
            return UserProfile.objects.get(
                authentication_user=authentication_user
            )

        def get_context_data(self, **kwargs):
            context = super(ProfileView, self).get_context_data(**kwargs)
            user = self.request.user
            context['user_accounts'] = user.socialaccount_set.all()
            return context
