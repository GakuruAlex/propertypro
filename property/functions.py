from django.core.paginator import Paginator


class MyPaginator:
    def make_pages_with_pk(pk,request,query_list,items_per_page):
        paginator = Paginator(query_list,items_per_page)
        page_number = request.GET.get("page")
        page_object = paginator.get_page(page_number)
        
        return page_object
