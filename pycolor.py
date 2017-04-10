class pyColor:
    """ all the colors """
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[1;33m"
    blue = "\033[1;34m"
    cyan = "\033[36m"
    lcyan = "\033[1;36m"
    reset = "\033[0m"
    
    def error(self, text):
    	return(self.red+"[*]"+self.reset+text)
    def proc(self, text):
    	return(self.green+"[*]"+self.reset+text)
    def resulte(self, text):
    	return(self.green+"[c]"+self.reset+text)
    def resultp(self, text):
    	return(self.green+"[p]"+self.reset+text)
    def result(self, text):
    	return(self.lcyan+text+self.reset)