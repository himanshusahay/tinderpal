from __future__ import unicode_literals

from django.db import models

class Line(models.Model):
	line_id = models.BigIntegerField()
	line_text = models.TextField()
	tags = models.ForeignKey(Tag)
	categories = models.ForeignKey(Category)

	def __str__(self):
		return self.line_text + "\n"

class Tag(models.Model):
	tag_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.tag_name + "\n"

class Category(models.Model):
	category_name = models.CharField(max_length = 50)

	def __str__(self):
		return self.category_name + "\n"

