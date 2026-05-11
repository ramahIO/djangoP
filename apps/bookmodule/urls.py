from django.urls import path
from . import views



urlpatterns = [
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('html5/links/', views.links, name='links'),
path("html5/text/formatting/", views.formatting, name="books.formatting"),
path("html5/listing/", views.listing, name="books.listing"),
path("html5/tables/",views.tables, name= "book.tables"),
path('search', views.searchBooks, name='book-search'),
path('insert/', views.insertBooks, name='book-insert'),
path('simple/query', views.simple_query, name='simple-query'),
path('complex/query', views.complex_query, name='complex-query'),
path('lab8/task1', views.lab8_task1, name='lab8-task1'),
path('lab8/task2', views.lab8_task2, name='lab8-task2'),
path('lab8/task3', views.lab8_task3, name='lab8-task3'),
path('lab8/task4', views.lab8_task4, name='lab8-task4'),
path('lab8/task5', views.lab8_task5, name='lab8-task5'),
path('lab8/task7', views.lab8_task7, name='lab8-task7'),
path('lab9_part1/listbooks', views.p1_listbooks, name='p1-listbooks'),
path('lab9_part1/addbook', views.p1_addbook, name='p1-addbook'),
path('lab9_part1/editbook/<int:id>', views.p1_editbook, name='p1-editbook'),
path('lab9_part1/deletebook/<int:id>', views.p1_deletebook, name='p1-deletebook'),
path('lab9_part2/listbooks', views.p2_listbooks, name='p2-listbooks'),
path('lab9_part2/addbook', views.p2_addbook, name='p2-addbook'),
path('lab9_part2/editbook/<int:id>', views.p2_editbook, name='p2-editbook'),
path('lab9_part2/deletebook/<int:id>', views.p2_deletebook, name='p2-deletebook'),
path('lab11/task1/students', views.t1_list, name='t1-list'),
path('lab11/task1/addstudent', views.t1_add, name='t1-add'),
path('lab11/task1/editstudent/<int:id>', views.t1_edit, name='t1-edit'),
path('lab11/task1/deletestudent/<int:id>', views.t1_delete, name='t1-delete'),
path('lab11/task2/students', views.t2_list, name='t2-list'),
path('lab11/task2/addstudent', views.t2_add, name='t2-add'),
path('lab11/task2/editstudent/<int:id>', views.t2_edit, name='t2-edit'),
path('lab11/task2/deletestudent/<int:id>', views.t2_delete, name='t2-delete'),
path('lab11/task3/products', views.t3_list, name='t3-list'),
path('lab11/task3/addproduct', views.t3_add, name='t3-add'),



]
