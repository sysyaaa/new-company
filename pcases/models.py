from django.db import models


class PrevCases(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    create_date = models.DateTimeField(verbose_name="작성일자")
    image = models.ImageField(verbose_name="첨부 이미지")

    verbose_name = "업무 사례 게시판 관리"
