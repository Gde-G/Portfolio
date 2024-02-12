from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.db.models import Q
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .forms import (
    TechnologyForm, ThirdPartyForm, TestimonialForm,
    CategoryForm, ProjectForm, ConsultForm, CertificateForm
)
from .models import Testimonial, Category, Project, ProjectImages, Technology, ThirdParty, Certificate
import base64
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile


def index(request: HttpRequest):
    form_consult = ConsultForm()
    get_copy = request.GET.copy()

    parameters_url = get_copy.urlencode()

    context = {
        'form_consult': form_consult,
        'parameters_url': parameters_url
    }

    return render(request, 'core/index.html', context=context)


@staff_member_required
@require_http_methods(['POST'])
def load_preview_logo(request: HttpRequest):
    logo = request.FILES.get('logo')
    ext_logo = logo.name[logo.name.rfind('.'):].lower()
    logo_data = base64.b64encode(logo.read()).decode()
    final_logo = f'data:image/{ext_logo};base64,' + logo_data

    return HttpResponse(f'<div class="project-img-preview-portada" id="preview-logo" style="background: url({final_logo}); background-size: contain; background-position: center center; background-repeat: no-repeat;"></div >')


@require_http_methods(['GET'])
def clear_alert(request: HttpRequest):
    return HttpResponse('')

# Technology


@staff_member_required
@require_http_methods(['GET'])
def technology_form(request: HttpRequest):
    types = Technology.type_choices

    context = {
        'types': types
    }

    return render(request, 'partials/technology-form.html', context=context)


@staff_member_required
@require_http_methods(['POST'])
def create_technology(request: HttpRequest):

    form = TechnologyForm(request.POST, request.FILES)

    if form.is_valid():
        techno = form.save()
        messages.success(
            request, f'{techno.name} has been created successfully!')

    else:
        for field, error in form.errors.as_data().items():
            messages.error(request, f'{field}. {error[0].messages[0]}')
    return redirect('get-technologies')


@require_http_methods(['GET'])
def get_technologies(request: HttpRequest):
    all_techno = Technology.objects.all()
    frontend_techno, backend_techno, db_techno, cloud_techno = [], [], [], []

    for tech in all_techno:
        if tech.type_tech == 'frontend':
            frontend_techno.append(tech)
        elif tech.type_tech == 'backend':
            backend_techno.append(tech)
        elif tech.type_tech == 'database':
            db_techno.append(tech)
        elif tech.type_tech == 'cloud':
            cloud_techno.append(tech)

    context = {
        'front_tech': frontend_techno,
        'back_tech': backend_techno,
        'db_tech': db_techno,
        'cloud_tech': cloud_techno
    }
    return render(request, 'sections/technologies.html', context=context)

# Third party


@staff_member_required
@require_http_methods(['GET'])
def thirdparty_form(request: HttpRequest):
    context = {
        'kind_choices': ThirdParty.kind_choices
    }
    return render(request, 'partials/thirdparties-form.html', context=context)


@staff_member_required
@require_http_methods(['POST'])
def create_thirdparty(request: HttpRequest):
    form = ThirdPartyForm(request.POST)
    if form.is_valid():
        thrid_party = form.save()
        return HttpResponse(f"<option value='{thrid_party.id}' selected>{thrid_party.name}</option>")
    else:
        return HttpResponse()

# Testimonials


@staff_member_required
def create_testimonial(request: HttpRequest):
    formTesti = TestimonialForm()

    if request.method == 'POST':
        formTesti = TestimonialForm(request.POST, request.FILES)
        if formTesti.is_valid():
            formTesti = formTesti.save()
            messages.success(
                request, f"{formTesti.name} Testimonio, a sido creado de forma exitosa!!")
        else:
            for field, error in formTesti.errors.as_data().items():
                messages.error(request, f'ERROR: {field}, {error[0]}')
    context = {'form': formTesti}
    return render(request, 'core/addOrEdit-testimonial.html', context=context)


@require_http_methods(['GET'])
def get_testimonials(request: HttpRequest):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'sections/testimonials.html', context=context)


@staff_member_required
def update_testimonial(request: HttpRequest, pk):
    testimonial = Testimonial.objects.get(id=int(pk))

    formTesti = TestimonialForm(instance=testimonial)

    if request.method == 'POST':
        testimonial.name = request.POST.get('name')
        testimonial.rol = request.POST.get('rol')
        testimonial.testimonial = request.POST.get('testimonial')
        testimonial.save()
        messages.success(
            request, f"{testimonial.name} Testimonio, a sido Editado de forma exitosa!!")
        return redirect('index')

    context = {'form': formTesti,
               'page': 'update',
               'testimonial': testimonial}
    return render(request, 'core/addOrEdit-testimonial.html', context=context)


@staff_member_required
@require_http_methods(['DELETE'])
def delete_testimonial(request: HttpRequest, pk):
    testi = Testimonial.objects.get(id=int(pk))
    testimonials = Testimonial.objects.all()

    name = testi.name
    testi.delete()
    messages.success(request, f'The Testimonial {name} be deleated!')
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'sections/testimonials.html', context=context)

# Category


@staff_member_required
def create_category(request: HttpRequest):
    formCate = CategoryForm()

    if request.method == 'POST':
        formCate = CategoryForm(request.POST)
        if formCate.is_valid():
            formCate = formCate.save()
            messages.success(
                request, f"{formCate.name} Categoria, a sido creada exitosamente!")
        else:
            for field, error in formCate.errors.as_data().items():
                messages.error(request, f'ERROR: {field}, {error[0]}')
    context = {'formCate': formCate}

    return render(request, 'core/addOrEdit-Category.html', context=context)


@staff_member_required
def update_category(request: HttpRequest, pk):
    cate = Category.objects.get(id=int(pk))

    formCate = CategoryForm(instance=cate)

    if request.method == 'POST':
        cate.name = request.POST.get('name')
        cate.description = request.POST.get('description')
        cate.save()
        messages.success(
            request, f"{cate.name} Categoria, a sido Editado de forma exitosa!!")
        return redirect('index')

    context = {'form': formCate,
               'page': 'update',
               'cate': cate}
    return render(request, 'core/addOrEdit-Category.html', context=context)


@staff_member_required
def delete_category(request: HttpRequest, pk):
    cate = Category.objects.get(id=int(pk))
    cate.delete()
    categories = Category.objects.all()
    return render(request, 'partials/categories.html', {'categories': categories})

# Projects


@require_http_methods(['GET'])
def get_portfolio(request: HttpRequest):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q == '':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(Q(category__name__icontains=q))
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'categories': categories
    }
    return render(request, 'sections/portfolio.html', context=context)


@staff_member_required
def create_project(request: HttpRequest):
    categories = Category.objects.all()
    technologies = Technology.objects.all()
    third_parties = ThirdParty.objects.all()
    formProj = ProjectForm()

    if request.method == 'POST':
        formProj = ProjectForm(request.POST, request.FILES)
        if formProj.is_valid():
            project = formProj.save()
            project.technologies.set(formProj.cleaned_data['technologies'])
            project.third_parties.set(formProj.cleaned_data['third_parties'])
            messages.success(
                request, f"Projecto {project.name}, a sido creada exitosamente!")
        else:
            for error, field in formProj.errors.as_data().items():
                messages.error(request, f'ERROR: {field}, {error[0]}')

    context = {
        'formProj': formProj,
        'categories': categories,
        'technologies': technologies,
        'third_parties': third_parties
    }

    return render(request, 'core/addOrEdit-Project.html', context=context)


@require_http_methods(['GET'])
def get_projects(request: HttpRequest):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    if q == '':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(Q(category__name__icontains=q))

    return render(request, 'partials/projects.html', context={'projects': projects})


def get_project(request: HttpRequest, slug):
    project = Project.objects.prefetch_related(
        'category', 'technologies', 'third_parties').get(slug=slug)
    proj_images = ProjectImages.objects.filter(project=project)

    front_tech = project.technologies.filter(type_tech='frontend')
    back_tech = project.technologies.filter(type_tech='backend')
    db_tech = project.technologies.filter(type_tech='database')
    cloud_tech = project.technologies.filter(type_tech='cloud')

    api_third = project.third_parties.filter(kind='API')
    library_third = project.third_parties.filter(kind='Library')
    other_third = project.third_parties.filter(kind='Other')

    third_exists = api_third.exists() or library_third.exists() or other_third.exists()
    context = {
        'project': project,
        'proj_images': proj_images,
        'front_tech': front_tech,
        'back_tech': back_tech,
        'db_tech': db_tech,
        'cloud_tech': cloud_tech,
        'third_exists':third_exists,
        'api_third': api_third,
        'library_third': library_third,
        'other_third': other_third
    }
    return render(request, 'core/project.html', context=context)


@staff_member_required
def update_project(request: HttpRequest, pk):
    project = get_object_or_404(Project.objects.prefetch_related(
        'category', 'technologies'), id=int(pk))
    formProj = ProjectForm(instance=project)
    technologies = Technology.objects.all()
    third_parties = ThirdParty.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        formProj = ProjectForm(request.POST, request.FILES, instance=project)

        if formProj.is_valid():
            project.save()
            project.technologies.set(formProj.cleaned_data['technologies'])
            project.third_parties.set(formProj.cleaned_data['third_parties'])
            return redirect('index')
        else:
            for f, e in formProj.errors.as_data().items():
                messages.error(request, f'{f}, {e[0].messages}')
            return redirect('edit-project', project.id)

    context = {
        'form': formProj,
        'page': 'update',
        'project': project,
        'categories': categories,
        'technologies': technologies,
        'third_parties': third_parties
    }

    return render(request, 'core/addOrEdit-Project.html', context)


@staff_member_required
@require_http_methods(['DELETE'])
def delete_project(request: HttpRequest, pk):
    project = Project.objects.get(id=int(pk))

    name = project.name
    project.delete()
    projects = Project.objects.all()
    messages.success(request, f"The project {name} be deleted")

    return render(request, 'partials/projects.html', {'projects': projects})

# Consult


@require_http_methods(['POST'])
def consult(request: HttpRequest):

    formConsu = ConsultForm(request.POST)

    if formConsu.is_valid():
        try:
            consult = formConsu.save()
            if len(consult.msg) == 0:
                messages.error(
                    request, 'Es imposible enviar una consulta vacia.')
                return redirect(request.META['HTTP_REFERER'])
            context = {
                'first_name': consult.first_name,
                'last_name': consult.last_name,
                'email': consult.email,
                'msg': consult.msg
            }

            temp = get_template('core/email_template.html')

            content = temp.render(context)

            corr = EmailMultiAlternatives(
                subject='Consulta desde pasoanchova.com',
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[consult.email])

            corr.attach_alternative(content, 'text/html')
            corr.send(fail_silently=False)

            messages.success(
                request, 'The consultation was sent successfully! We will contact you through the email entered.')
        except:
            messages.error(
                request, 'The consultation was NOT sent due to an error. Please try again later!')

    else:
        for field, errors in formConsu.errors.as_data().items():
            if field == "captcha" and errors[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue
            messages.error(request, f"ERROR: {field}, {errors[0].messages[0]}")

    return render(request, 'partials/contact-form.html')

# Certificates


@require_http_methods(['GET'])
def get_certificates(request: HttpRequest):
    certificates = Certificate.objects.all()
    form = CertificateForm()
    return render(
        request, 'partials/certificates-modal.html',
        context={'certificates': certificates, 'form': form}
    )


@require_http_methods(['POST'])
@staff_member_required
def create_certificate(request: HttpRequest):
    certificates = Certificate.objects.all()
    form = CertificateForm(request.POST, request.FILES)

    if form.is_valid():
        certificate = form.save()
    else:
        for f, e in form.errors.as_data().items():
            messages.error(request, f'{f}, {e[0].messages}')

    return render(request, 'core/certificates.html', context={'certificates': certificates})
