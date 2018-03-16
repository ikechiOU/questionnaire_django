from django.contrib import admin
from pams.models import PamsAnswer, PamsQuiz, PamsFeedback


class PamsAnswerAdmin(admin.ModelAdmin):
	tmp = ['userID', 'user_type', 'ans_last', 'team_1', 'team_2']
	for i in range(10):
		tmp.append('res_'+str(i+1).zfill(3))
	list_display = tuple(tmp)

admin.site.register(PamsAnswer, PamsAnswerAdmin)


class PamsQuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_id', 'quiz_text')

admin.site.register(PamsQuiz, PamsQuizAdmin)


class PamsFeedbackAdmin(admin.ModelAdmin):
    list_display = ('fb_type', 'fb_num', 'fb_text')

admin.site.register(PamsFeedback, PamsFeedbackAdmin)
