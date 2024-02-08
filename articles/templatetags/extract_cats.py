from django import template

register = template.Library()


def cats(article_cat):
    return ', '.join([str(name) for name in article_cat])

register.filter('cats', cats)