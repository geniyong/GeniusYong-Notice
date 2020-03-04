from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class MainView(View):

    template_name = 'portal/main/index.html'

    def get(self, request):
        # 뷰 로직 작성
        context = {
            'name': request.user.username,
        }
        return render(request, self.template_name, context)