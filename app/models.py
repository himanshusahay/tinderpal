from __future__ import unicode_literals

from django.db import models

class Tag(models.Model):
	tag_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.tag_name + "\n"

	class Meta:
		ordering = ('tag_name', )

class Category(models.Model):
	category_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.category_name + "\n"

	class Meta:
		ordering = ('category_name', )
		verbose_name_plural = "categories"

class Line(models.Model):
	line_text = models.TextField()
	tags = models.ManyToManyField(Tag)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.line_text + "\n"

	class Meta:
		ordering = ('line_text', )