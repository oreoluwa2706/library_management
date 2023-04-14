from django.urls import path, include



from api import views
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

#  path('books/', views.book_list, name="book_list1"),
# path('book/<int:id>/', views.book_details),
# path('authors/', views.get_authors),
# path('author/first_name/last_name/', views.author_details)


# path('books/', views.BookCreateApiView.as_view()),
# path('book/', views.BookCreateApiView.as_view()),

#router = SimpleRouter()
router = DefaultRouter()

router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('book_instance', views.BookInstanceViewSet)
#router.register('book_author', views.BookCreateApiView)
#router = SimpleRouter()
#router.register('books', views.BookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('createbook/', views.BookCreateApiView.as_view()),
    #path('books/', views.BookCreateApiView.as_view()),
   # path('author/<int:pk>/', views.AuthorDetailView.as_view()),
    #path('books/', views.GetAllBooks.as_view()),
    path('author/<int:pk>/', views.author_detail, name='author_detail')
    # path('book/<ink:pk>/', views.GetAuthorById.as_view()),
]

# path('<int:pk>/delete/', views.book_delete, name="delete")
