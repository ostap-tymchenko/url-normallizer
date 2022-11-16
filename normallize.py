# make a function to normallize a url
# make sure the function adds https:// and www

def normalize_url(url):
    if url.startswith("https://"):
        pass
    else:
        url = "https://" + url
    if url.startswith ("https://www."):
        pass
    return url

# take tui input and print the normalized url
url = input("Enter a url: ")
print(normalize_url(url))
