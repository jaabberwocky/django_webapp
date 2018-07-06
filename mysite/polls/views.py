from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
	# generates top 5 most recent questions
	template_name = "polls/index.html"
	context_object_name = "latest_question_list"

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'

# older detail/results "hard way" functions left below for reference
# rewritten to use get_object_or_404
def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

# still used
def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# redisplay the question voting form
		return render(request, 'polls/detail.html', {
			'question':question,
			'error_message':"You didn't select a choice!",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()

		# always return HttpResponseRedirect after successfully dealing with POST data
		# prevents users from posting data twice if user hits back button
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))