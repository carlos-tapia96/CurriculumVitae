from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

from django.views import generic

from .forms import ContactForm


#En resumen, esta vista IndexView se utiliza para renderizar la plantilla
# "main/index.html" y proporciona datos adicionales al contexto de la
# plantilla. Los datos incluyen testimonios, certificados, blogs y
# elementos del portafolio que están marcados como activos en tu sitio
# web. Estos datos se pueden utilizar en la plantilla HTML para mostrar
# contenido dinámico en la página de inicio de tu sitio.
class IndexView(generic.TemplateView):
    template_name = "main/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)
        
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context

#En resumen, esta vista ContactView se utiliza para mostrar un formulario 
# de contacto en la página "main/contact.html". Cuando el formulario se 
# envía correctamente, se guarda y se muestra un mensaje de éxito al 
# usuario, y luego se redirige al usuario a la página de inicio.
class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    success_url = "/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)
    
#En resumen, esta vista PortfolioView se utiliza para mostrar una lista 
# paginada de objetos del modelo Portfolio en la plantilla 
# "main/portfolio.html". Los objetos que se muestran son solo aquellos 
# que tienen is_active establecido en True. Si tienes más de 10 objetos, 
# se dividirán en páginas separadas con 10 objetos por página.

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    


#En resumen, esta vista se utiliza para mostrar los detalles de un objeto 
# específico del modelo Portfolio en la plantilla "main/portfolio-detail.html".
# Es útil cuando deseas permitir a los usuarios ver los detalles completos de
# un elemento del portafolio específico en tu sitio web.
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name= "main/portfolio-detail.html"
    


#En resumen, esta vista BlogView se utiliza para mostrar una lista 
# paginada de entradas de blog (objetos del modelo Blog) en la plantilla
# "main/blog.html". Los objetos que se muestran son solo aquellos que
# tienen is_active establecido en True. Si tienes más de 10 entradas de
# blog, se dividirán en páginas separadas con 10 entradas por página.
class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
