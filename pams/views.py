from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from pams.models import PamsAnswer, PamsQuiz, PamsFeedback
from django.contrib.auth.models import User
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from . import radar_chart
import matplotlib.pyplot as plt
 
@login_required
def index(request):
	login_user_id = request.user.id
	ans = PamsAnswer.objects.get(user_id=login_user_id)
	elif ans.ans_last == 1:
		tmp = {
			'message': 'PaMSを開始します'
		}
	elif ans.ans_last > 100:
		tmp = {
			'message': '結果を表示します'
		}
	else:
		tmp = {
			'message': 'PaMSを再開します'
		}
	return render(request, 'index.html', tmp)

@login_required
def quiz(request):
	login_user_id = request.user.id
	ans = PamsAnswer.objects.get(user_id=login_user_id)
	if 'button_1' in request.GET:
		exec('ans.ans_'+str(ans.ans_last).zfill(3)+'=1')
		ans.ans_last = ans.ans_last+1
		ans.save()
	if 'button_2' in request.GET:
		exec('ans.ans_'+str(ans.ans_last).zfill(3)+'=2')
		ans.ans_last = ans.ans_last+1
		ans.save()
	if 'button_3' in request.GET:
		exec('ans.ans_'+str(ans.ans_last).zfill(3)+'=3')
		ans.ans_last = ans.ans_last+1
		ans.save()
	if 'button_4' in request.GET:
		exec('ans.ans_'+str(ans.ans_last).zfill(3)+'=4')
		ans.ans_last = ans.ans_last+1
		ans.save()
	if 'button_5' in request.GET:
		exec('ans.ans_'+str(ans.ans_last).zfill(3)+'=5')
		ans.ans_last = ans.ans_last+1
		ans.save()
	qiz = PamsQuiz.objects.filter(quiz_id=ans.ans_last)
	if ans.ans_last > 100:
		ans.res_001 = ((6 - ans.ans_020)+(6 - ans.ans_021)+(6 - ans.ans_046)+(6 - ans.ans_062)+(6 - ans.ans_095))*2
		ans.res_002 = (ans.ans_002+ans.ans_006+(6 - ans.ans_010)+ans.ans_026+(6 - ans.ans_028)+ans.ans_058)*5/3
		ans.res_003 = ((6 - ans.ans_005)+(6 - ans.ans_009)+(6 - ans.ans_015)+(6 - ans.ans_019)+ans.ans_026+ans.ans_066+(6 - ans.ans_077)+(6 - ans.ans_078))*5/4
		ans.res_004 = (ans.ans_008+(6 - ans.ans_013)+ans.ans_063+ans.ans_068+ans.ans_069+ans.ans_072+ans.ans_079+ans.ans_085+ans.ans_086+ans.ans_092+ans.ans_099)*5/6
		ans.res_005 = (ans.ans_001+(6 - ans.ans_007)+ans.ans_012+ans.ans_022+(6 - ans.ans_024)+(6 - ans.ans_027)+(6 - ans.ans_036)+ans.ans_048+ans.ans_051+(6 - ans.ans_052)+ans.ans_055+(6 - ans.ans_057)+ans.ans_080+ans.ans_094)*5/7
		ans.res_006 = (ans.ans_032+ans.ans_061+ans.ans_070+ans.ans_089+ans.ans_090+ans.ans_100)*5/3
		ans.res_007 = (ans.ans_059+ans.ans_073+ans.ans_075+ans.ans_082+ans.ans_083+ans.ans_084)*5/3
		ans.res_008 = (ans.ans_003+ans.ans_053+ans.ans_071+ans.ans_081+(6 - ans.ans_087)+ans.ans_093+ans.ans_096+ans.ans_097)*5/4
		ans.res_009 = (ans.ans_004+ans.ans_011+ans.ans_014+ans.ans_018+ans.ans_023+ans.ans_035+ans.ans_056+ans.ans_064+ans.ans_065+ans.ans_067+ans.ans_091+ans.ans_098)*10/13
		ans.res_010 = (ans.ans_016+(6 - ans.ans_017)+(6 - ans.ans_031)+(6 - ans.ans_039)+ans.ans_088)*2
		ans.save()
		if ans.res_001 > 30:
				A = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_001 > 25:
				A = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				A = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_002 > 30:
				B = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_002 > 25:
				B = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				B = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_003 > 30:
				C = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_003 > 25:
				C = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				C = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_004 > 30:
				D = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_004 > 25:
				D = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				D = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_005 > 30:
				E = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_005 > 25:
				E = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				E = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_006 > 30:
				F = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_006 > 25:
				F = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				F = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_007 > 30:
				G = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_007 > 25:
				G = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				G = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_008 > 30:
				H = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_008 > 25:
				H = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				H = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_009 > 30:
				I = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_009 > 25:
				I = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				I = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		if ans.res_010 > 30:
				J = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=1)
		elif ans.res_010 > 25:
				J = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=0)
		else:
				J = PamsFeedback.objects.all().filter(fb_type='幸福性').filter(fb_num=-1)
		return render(request, 'result.html', {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J})
	return render(request, 'quiz.html', {'qiz': qiz})

@login_required
def chart(request):
	login_user_id = request.user.id
	ans = PamsAnswer.objects.get(userID=login_user_id)
	N = 10
	theta = radar_chart.radar_factory(N, frame='polygon')
	label= ['A','B','C','D','E','F','G','H','I','J']
	data = []
	for i in range(10):
		exec('data.append(ans.res_'+str(i+1).zfill(3)+')')
	# create figure
	fig = plt.figure(1,figsize=(5,5))
	ax = plt.subplot(projection='radar')
	# chartの範囲を0-3
	ax.set_ylim(0, 50)
	# Grid線を位置の指定
	ax.set_rgrids([10, 20, 30, 40, 50])
	# 描画処理
	ax.plot(theta, data, 'c.-')
	ax.fill(theta, data, facecolor='cyan', alpha=0.3)
	ax.set_varlabels(label)
	# 標準のグリッド線は円形なので消す（放射方向だけ残す）
	ax.yaxis.grid(False)
	# 替わりグリッド線を描く
	ax.plot(theta, [10]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
	ax.plot(theta, [20]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
	ax.plot(theta, [30]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
	ax.plot(theta, [40]*N, 'k-', marker=None, linewidth=0.5, alpha=0.3)
	# Return
	canvas=FigureCanvas(fig)
	response=HttpResponse(content_type='image/png')
	canvas.print_png(response)
	return response
