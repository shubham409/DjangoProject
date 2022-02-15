def give_error(message :str)->dict:
    '''
        This Function will return error in dictionary fomat having error as key and message as value
    '''
    dct = {
        'error':message
    }
    return dct
def give_message(message :str)->dict:
    '''
        This Function will return message in dictionary fomat having error as key and message as value
    '''
    dct = {
        'message':message
    }
    return dct
def success_message(message :str)->dict:
    '''
        This Function will return success message in dictionary fomat having error as key and message as value
    '''
    dct = {
        'success':message
    }
    return dct