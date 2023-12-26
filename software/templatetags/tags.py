from django import template
from software.models import Software, Catagory, Comment, Download_Monitor

register = template.Library()


@register.filter(name='cat_count')
def cat_count(cat_name):
    cat = Catagory.objects.get(name=cat_name)
    count = Software.objects.filter(catagory=cat).count()
    return count


@register.filter(name='get_count')
def get_count(post_id):
    total = Comment.objects.filter(post=post_id).count()
    return total


@register.filter(name='total_download')
def total_download(post_name):
    post = Software.objects.get(name=post_name)
    total_download = Download_Monitor.objects.filter(name=post).count()
    return total_download


@register.filter(name='comment_filter')
def comment_filter(comment_id):
    cmt = Comment.objects.get(id=comment_id)
    cmt2 = Comment.objects.filter(parent=cmt)
    return cmt2
