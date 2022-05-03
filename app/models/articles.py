class Sources:
    '''
    Sources class to define news source objects
    '''
    def __init__(self,id,title,urlToImage,category,description,url):
        self.id = id
        self.title = title
        self.urlToImage=urlToImage
        self.category = category
        self.description = description
        self.url=url
    