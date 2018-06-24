from webapp.forms import SForm
from django.views.generic.edit import FormView
from django import forms


class HomePageView(FormView):
    template_name = 'home.html'
    form_class = SForm
    success_url = '/'
    ctx = dict()

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        answer = form.check_string()
        self.ctx['answer'] = answer
        
        return super(HomePageView, self).form_valid(form)

    def get_context_data(self, **kwargs):
    	context = super(HomePageView, self).get_context_data(**kwargs)
    	if 'answer' in self.ctx:
    		context['answer'] = self.ctx['answer']
    	return context




