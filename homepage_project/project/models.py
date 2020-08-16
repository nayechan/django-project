from django.db import models
from datetime import datetime
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

# Create your models here.

class Project(models.Model):
    projectName = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now(), editable=False)
    context = MarkdownxField('CONTENT')

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        db_table = 'project_project'
        ordering = ('-projectName','-version','-pub_date',)

    def formatted_markdown(self):
        return markdownify(self.context)
