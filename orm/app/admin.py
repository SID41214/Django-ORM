from django.contrib import admin

# Register your models here.
from .models import Blog,Author,Entry,Restaurant,Rating

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['name','tagline']
    
@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name','email']
    

@admin.register(Entry)
class EntryModelAdmin(admin.ModelAdmin):
    def display_authors(self, obj):
        return ", ".join([author.name for author in obj.authors.all()])

    list_display = ['blog', 'headline', 'body_text', 'pub_date', 'mod_date', 'display_authors', 'number_of_comments',
                    'number_of_pingbacks', 'rating']

    # Add any other fields you want to display

    display_authors.short_description = 'Authors'
    
@admin.register(Restaurant)
class RestaurantModelAdmin(admin.ModelAdmin):
    list_display=['name','website','date_opened','latitude','longitude']
    
    
@admin.register(Rating)
class RatingModelAdmin(admin.ModelAdmin):
    list_display=['user','restaurant','rating']