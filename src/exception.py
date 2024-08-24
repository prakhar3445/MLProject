import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    #above line will give details in which line the exception has appeared
    file_name=exc_tb.tb_frame.f_code.co_filename
    #above line will give us the file name
    error_message="Error has occured in python scrip name [{0}] in the line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error)
        )
    return error_message
    
class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e, sys)
 