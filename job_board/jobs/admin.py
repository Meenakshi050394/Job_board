from django.contrib import admin
from jobs.models import Industries, Company, JobPost, Review, Application


admin.site.register(Industries)
admin.site.register(Company)
admin.site.register(JobPost)
admin.site.register(Review)
admin.site.register(Application)