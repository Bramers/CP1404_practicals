import wikipedia

search_phrase = input("search: ")
while search_phrase != "":
    try:
        print(wikipedia.summary(search_phrase))
    except wikipedia.exceptions.DisambiguationError as disambiguation_error:
        print(disambiguation_error.options)
    search_phrase = input("search: ")

