"""
Input dictonary
"""
dictonary = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }

def group_by_owners(dictonary):
    '''
    This function takes an dictonary of files with owner names as inputs and returns
     a new dictonary with owner as key and list of files as output
    :param dictonary:
    :return result:
    '''
    result = {}
    for key,value in dictonary.items():
        if value not in result.keys():
            result[value] = [key]
        else:
            result[value].append(key)
    return result

#calling the function
print(group_by_owners(dictonary))