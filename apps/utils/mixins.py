from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator


class GetObjectMixin:
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        instance = self.queryset.filter(slug=slug).owned(self.request.user)
        if instance:
            return instance.first()
        raise Http404


class MemberRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        print('requireing..?')
        instance = self.get_object()
        user = request.user
        if user.is_staff:
            return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)
        if instance.free:
            return super(MemberRequiredMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponse('<h1>Restricted content</h1>')


class StaffMemberRequiredMixin:
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffMemberRequiredMixin, self).dispatch(request, *args, **kwargs)