def give_error(message :str)->dict:
    '''
        This Function will return error in dictionary fomat having error as key and message as value
    '''
    dct = {
        'error':message
    }
    return dct