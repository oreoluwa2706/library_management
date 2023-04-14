from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserCreateSerializer
from book.models import Book, Author, BookInstance


# class AuthorSerializer(serializers.ModelSerializer):
#   class Meta:
#      model = Author
#     fields = ['first_name', 'last_name', 'date_of_birth']

class BookInstanceSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = BookInstance
        fields = ['user_id', 'due_back', 'status', 'book', 'imprint', 'borrower']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ('title', 'description', 'author', 'price', 'language', 'genre',
                  'isbn', 'discount_price')

    discount_price = serializers.SerializerMethodField(method_name='discount')

    def discount(self, book: Book):
        return book.price * 25 / 100

    author = serializers.HyperlinkedRelatedField(queryset=Author.objects.all(),
                                                 view_name='author_detail',
                                                 lookup_field='pk')


class BookCreatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'isbn', 'description')


class UserCreate(UserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', ]


"""
class BookDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id"]

"""

#  price = serializers.IntegerField()
# discount_price = serializers.SerializerMethodField(method_name='get_discount')

# get_discount(self: Author):
#   return self.price - 20
