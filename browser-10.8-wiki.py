import wikipedia
print('WikiBrowser: Search Anything')

search = input('Enter your search')

info = wikipedia.summary(search, sentences = 5)

print(info)
