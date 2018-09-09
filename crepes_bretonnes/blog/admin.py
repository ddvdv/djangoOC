from django.contrib import admin
from django.utils.text import Truncator

from .models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')
    prepopulated_fields = {'slug':('titre',),}
    fieldsets = (
            ('Général', {
                'classes':['collapse',],
                'fields':('titre', 'auteur', 'categorie')
            }),
            ('Contenu de l\'article', {
                'description': 'Le formulaire accepte les balises HTML. Utilises-les à bon escient!',
                'fields':('contenu',)
            }),
    )

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

# Register your models here.
admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)
