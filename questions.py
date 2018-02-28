#Question Class
class question:
    #default Constructor, takes in a question
    def __init__(self, q = "" ):
        #Variable for question
        self.prompt = q
        #variable for choices array
        self.choices = []
        #Variable that records users response
        self.response = ""

    #Appends to Answer choices. 
    def AddChoice(self, a):
        self.choices.append(a)
    #sets response = input 
    def RecordResponse(self, a):
        self.response = a
