from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name ="Titulo")
    description = models.TextField(verbose_name ="Descripcion")
    
    image = models.ImageField(verbose_name ="Imagen", upload_to="projects") 
    #upload_to para que se guarde dentro de ese directorio PROJECTS dentro de MEDIA que ya configuramos en setting
    
    created_date = models.DateTimeField(auto_now_add=True,verbose_name ="Fecha de creacion") 
    updated_date = models.DateTimeField(auto_now=True,verbose_name ="Fecha de edicion")
    ## Django oculta las fechas con auto_now para no poder editarlas
    ## Para mostrarlas vamos a  editar el admin.py de portfolio añadiendo una clase ProjectAdmin() --- y el readonly_fields

    link = models.URLField(verbose_name ="Direccion Web",null=True, blank=True)


    class Meta: #sub clase Meta  para añadir metadatos extendidos
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created_date"] # Para ordenarlos por el campo creted_date .. el guion espara  que vaya de mayor a menor

    def __str__(self):
        return self.title       # para cambiarlo el nombre del project en la lista