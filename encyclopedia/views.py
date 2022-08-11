from django.shortcuts import render
from markdown2 import Markdown

from . import util


def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()

    if content is None:
        return None
    return markdowner.convert(content)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    content = convert_md_to_html(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "This entry does not exist"})
    return render(request, "encyclopedia/entry.html", context={"title": title, "content": content})


def search(request):
    if request.method == "POST":
        entry_search = request.POST["q"]
        content = convert_md_to_html(entry_search)
        if content is not None:
            return render(request, "encyclopedia/entry.html",
                          context={"title": entry_search, "content": content})
        else:
            all_entries = util.list_entries()
            results = []
            for page in all_entries:
                if entry_search.lower() in page.lower():
                    results.append(page)
            return render(request, "encyclopedia/search.html", context={"results": results})


def create(request):
    return render(request, "encyclopedia/create.html")