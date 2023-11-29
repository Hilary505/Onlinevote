
from django.contrib import admin
from .models import Candidate, Position

# The admin.site.register() method is used to register the models to the admin site
admin.site.register(Position)
# The PositionAdmin class is used to create the admin site for the Position model
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Candidate)
# The CandidateAdmin class is used to create the admin site for the Candidate model
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)