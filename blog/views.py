from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import BlogArticle


class BlogArticleCreateView(CreateView):
    """
    Контроллер, который отвечает за создание статьи блога
    """
    model = BlogArticle
    fields = ('title', 'body', 'preview', )
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)


class BlogArticleListView(ListView):
    """
    Контроллер, который отвечает за просмотр списка статей блога
    """
    model = BlogArticle

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogArticleDetailView(DetailView):
    """
    Контроллер, который отвечает за просмотр статьи блога
    """
    model = BlogArticle

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogArticleUpdateView(UpdateView):
    """
    Контроллер, который отвечает за редактирование статьи блога
    """
    model = BlogArticle
    fields = ('title', 'body', 'preview', )

    def form_valid(self, form):
        if form.is_valid():
            new_article = form.save()
            new_article.slug = slugify(new_article.title)
            new_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogArticleDeleteView(DeleteView):
    """
    Контроллер, который отвечает за удаление статьи блога
    """
    model = BlogArticle
    success_url = reverse_lazy('blog:list')
