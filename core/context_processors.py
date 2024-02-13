from .forms import ConsultForm

def get_consult_form(request):

    return {
        "form_consult": ConsultForm()
    }