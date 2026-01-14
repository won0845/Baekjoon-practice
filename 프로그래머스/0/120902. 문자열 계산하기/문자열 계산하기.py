def solution(my_string):
    # "3 + 12 - 35"
    my_string = my_string.replace(" ","")
    my_string = my_string.replace("-","+-")
    
    # "3 + 12 +-35"
    my_string = my_string.split("+")
    my_string = [i for i in my_string if i != ""]
    
    print(my_string)
    
    answer = sum(list(map(int, my_string)))
    
    return answer