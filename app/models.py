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
        
class Articles:
    '''
    News Articles class to define news articles objects
    '''
    def __init__(self,title,urlToImage,content,author,publishedAt,url):
        self.title = title
        self.urlToImage = urlToImage
        self.content = content
        self.author = author
        self.publishedAt= publishedAt
        self.url=url
    