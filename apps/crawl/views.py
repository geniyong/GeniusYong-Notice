from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from geniusYong_notice.conf.utils import get_private_info_value


class MainView(View):

    template_name = 'portal/main/index.html'

    def get(self, request):
        # 뷰 로직 작성
        context = {
            'name': request.user.username,
            'KAKAO_JS_KEY': get_private_info_value("KAKAO")['JS_API_KEY']
        }
        return render(request, self.template_name, context)