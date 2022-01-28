from email.encoders import encode_7or8bit
from enum import unique
import rubik.cube as rubik
from collections import defaultdict

def _check(parms):
    result={}
    encodedCube = parms.get('cube',None)     

    def has_correct_colors(cube: str):
        unique_color_count = defaultdict(int)

        for color in cube:
            unique_color_count[color] += 1

        # check if there are 6 unique colors
        if (len(unique_color_count) != 6):
            return False
        
        # check for 9 occurences of each color
        for color, occur in unique_color_count.items():
            if occur != 9:
                return False
        
        return True
        
    if(encodedCube == None):
        result['status'] = 'error: no value present'
    elif(not isinstance(encodedCube, str)):
        result['status'] = 'error: value is of wrong type'
    elif(len(encodedCube) != 54):
        result['status'] = 'error: incorrect character count'
    elif(not has_correct_colors(encodedCube)):
        result['status'] = 'error: incorrect character count'
    else:
        result['status'] = 'ok'
    return result