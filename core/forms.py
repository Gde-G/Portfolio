from django import forms
from .models import Technology, ThirdParty, Testimonial, Category, Project, Consult, Certificate
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'logo', 'type_tech']


class ThirdPartyForm(forms.ModelForm):
    class Meta:
        model = ThirdParty
        fields = ['name', 'kind', 'description']


class TestimonialForm(forms.ModelForm):

    class Meta:
        model = Testimonial
        fields = ['name', 'testimonial', 'image']


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name', 'description']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'logo', 'db_diagram',
            'link', 'category', 'technologies', 'third_parties'
        ]


class ConsultForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = Consult
        fields = ['first_name', 'last_name', 'email', 'msg']


class CertificateForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    class Meta:
        model = Certificate
        fields = ['title', 'link', 'image']
