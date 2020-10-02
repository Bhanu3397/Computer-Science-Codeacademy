ls_jokes=[{"id":280,"type":"general","setup":"What's brown and sticky?","punchline":"A stick."},{"id":100,"type":"general","setup":"Did you hear the joke about the wandering nun?","punchline":"She was a roman catholic."},{"id":72,"type":"programming","setup":"I was gonna tell you a joke about UDP...","punchline":"...but you might not get it."},{"id":224,"type":"general","setup":"What do you call a pig that knows karate?","punchline":"A pork chop!"},{"id":285,"type":"general","setup":"What's the difference between a hippo and a zippo?","punchline":"One is really heavy, the other is a little lighter."},{"id":119,"type":"general","setup":"How did the hipster burn the roof of his mouth?","punchline":"He ate the pizza before it was cool."},{"id":374,"type":"general","setup":"Why does Norway have barcodes on their battleships?","punchline":"So when they get back to port, they can Scandinavian."},{"id":283,"type":"general","setup":"What's the best thing about elevator jokes?","punchline":"They work on so many levels."},{"id":51,"type":"general","setup":"When a dad drives past a graveyard: Did you know that's a popular cemetery?","punchline":"Yep, people are just dying to get in there"},{"id":83,"type":"general","setup":"Can February march?","punchline":"No, but April may."}]

index=0
for ids in ls_jokes:
    # for key,val in ids.items():
    print("{}={}".format(ids["setup"],ids["punchline"]))

# url="https://official-joke-api.appspot.com/jokes/random"
