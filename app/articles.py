class Sources:
    '''
    Sources class to define news source objects
    '''
    def __init__(self,id,name,urlToImage,category,description,url):
        self.id = id
        self.name = name
        self.urlToImage=urlToImage
        self.category = category
        self.description = description
        self.url=url
    