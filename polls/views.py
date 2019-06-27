
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from django.urls import reverse
from django.views import generic

from .models import Vote, Question, VoteValue


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    param = request.POST['vote']
    question.vote_set.create(value=VoteValue[param].name)

    return render(request, 'polls/index.html')


    # try:
    #     selected_vote = question.vote_set.get(pk=request.POST['vote'])
    # except (KeyError, Vote.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_vote.votes += 1
    #     selected_vote.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))