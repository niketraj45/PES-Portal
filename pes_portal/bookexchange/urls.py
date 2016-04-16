from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^$',views.list_books_for_sale,name="list_books_for_sale"),
	# url(r'^do_sale/',views.do_sale,name="do_sale"),
	#url(r'^populate_students/',views.populate_students,name="populate_students"),
	#url(r'^populate_upforsale/',views.populate_upforsale,name="populate_upforsale"),
	url(r'^upload_book/',views.upload_book,name="upload_book"),
	url(r'^delete_book/',views.delete_book,name="delete_book"),
	url(r'^buy/',views.buy,name="buy"),
	url(r'^cancel_buy/',views.cancel_buy,name="cancel_buy"),
	url(r'^search_book',views.search_book,name="search_book"),
	url(r'^view_buyers',views.view_buyers,name="view_buyers"),



]