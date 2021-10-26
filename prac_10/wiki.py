import wikipedia

search_phrase = input("search: ")
while search_phrase != "":
    try:
        wiki_page = wikipedia.page(search_phrase, None, False)
        print(f"{wiki_page.title} \n{wiki_page.summary} \n{wiki_page.url}")
    except wikipedia.exceptions.DisambiguationError as disambiguation_error:
        print(disambiguation_error.options)
    search_phrase = input("search: ")
