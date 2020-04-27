class Source:
    '''
    Class to create the news source instances. 
    '''
    def __init__(self, id, name, description):
        '''
        Initilization method to instantiate Source objects.

        Args:
            id: The unique identification of Source object.
            name: The name of the Source object
            description: The description of the Source object
        '''
        self.id = id
        self.name = name
        self.description = description
 
        
class News_Article:
    '''
    Class to create the news article instances. 
    '''
    def __init__(self,id,author,title,description,publishedAt,image,content,url):
        '''
        '''
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.image = image
        self.content = content
        self.url = url