import webbrowser


def islem(query):
    if not query:
     return print("Aratmam için bir şeyler söylemen gerek!")
    else:
     webbrowser.open("https://www.google.com/search?q=" + query)

exec = {
    "araştır": {
        "exec": lambda query: islem(query) 
    
    }
}
