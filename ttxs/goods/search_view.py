from haystack.generic_views import SearchView

# from search_view import MySearchView


class MySearchView(SearchView):

    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        context["show_cart"] = "1"
        return context



