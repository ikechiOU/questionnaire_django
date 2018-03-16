from django.db import models
from django.urls import reverse

class ReJapanUser(model.Model):
    """
    ユーザーモデル
    """
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = ((MALE, '男性'),(FEMALE, '女性'),)
    # ユーザーID
    user_id = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    # 組織ID
    team_id = models.IntegerField(default=0)
    # ユーザー名
    user_name = models.CharField(
        max_length = 20,
        blank = True,
    )
    # ユーザー生年月日
    birth_date = models.DateField(default=timezone.now)
    # ユーザー性別
    gender = models.IntegerField(choices=GENDER_CHOICES, blank=True)
    # ユーザー役職（？）
    position = models.CharField(
        max_length = 20,
        blank = True,
    )
    # ユーザー登録日
    registration_date = models.DateField(default=timezone.now)


class Team(model.Model):
    """
    組織モデル
    """
    # 組織ID
    team_id = models.IntegerField(default=0)
    # 組織名
    team_name = models.CharField(
        max_length = 50,
        blank = True,
    )


class PamsAuthority(model.Model):
    """
    アクセス権限モデル
    """
    # 管理者ユーザーID
    authorized_user_id = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    # 確認したい組織ID
    team_id = models.IntegerField(default=0)


class PamsAnswer(models.Model):
    """
    PaMS回答モデル
    """
    # ユーザーID
    user_id = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    # 進捗確認用
    ans_last = models.IntegerField(default=1)
    # 回答（配列表記の文字列）
    answers = models.CharField(
        max_length=201,
        blank=True,
    )
    # 結果（配列表記の文字列）
    results = models.CharField(
        max_length=21,
        blank=True,
    )
    # 回答日
    ans_date = models.DateField(default=timezone.now)


class PamsQuiz(models.Model):
    """
    PaMSテストモデル
    """
    # クイズ表示順
    quiz_id = models.IntegerField(default=0)
    # クイズ本文
    quiz_text = models.CharField(
        max_length=50,
        blank=True,
    )


class PamsFeedback(models.Model):
    """
    フィードバックモデル
    """
    # 因子
    fb_type = models.CharField(
        max_length=10,
        blank=True,
    )
    # 高中低フラグ
    fb_num = models.IntegerField(default=0)
    # フィードバックの本文
    fb_text = models.CharField(
        max_length=200,
        blank=True,
    )
