class Error:
    
    @staticmethod
    def protocolo():
        print("Protocolo apresenta erro")
        
    @staticmethod
    def entrada():
        print("Parametros incorretos")
        
    @staticmethod
    def error_500():
        print("Internal Server Error")
        
    @staticmethod
    def error_404():
        print("Not Found")
        
        
Error.error_500()
Error.entrada()