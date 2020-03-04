from django.db import models
from django.utils.translation import gettext_lazy as _


class Info(models.Model):

    pid = models.CharField(_('사이트 내 식별자'), max_length=255)
    url = models.CharField(_('게시글 주소'), max_length=1023)
    site_url = models.CharField(_('사이트 주소'), max_length=1023)
    site_name = models.CharField(_('사이트 이름'), max_length=255)
    content = models.CharField(_('내용'), max_length=1023)
    post_created_at = models.DateTimeField(_('게시글 생성일자'), blank=True)
    created_at = models.DateTimeField(_('생성일자'), auto_now_add=True)
    edited_at = models.DateTimeField(_('수정일자'), auto_now=True)

    class Meta:
        verbose_name = _('크롤링한 정보')
        verbose_name_plural = _('크롤링한 정보들')
