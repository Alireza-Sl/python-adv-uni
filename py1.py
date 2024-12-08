import requests as r

class fetcher:
    __students = []
    
    
    def __init__(self):
        self.__students =r.get ("https://cdn.ituring.ir/ex/users.json").json()
    
    
    
    def nerds(self):
        list1= set()
        for i in self.__students:
            if i["score"]>18.5:
                list1.add(i["name"] + "_" + i["last _name"])
        return list1
    
    
    def sultans(self):
        list1 =[]
        max = 0
        for i in self.__students:
           if i ["score"] > max:
               max = i["score"]
               
        for i in  self.__students:
           if i["score"] == max:
               list1.append(i["name"] + "_" + i["last _name"])
        return tuple(list1)
    
    def mean(self):
        min =0
        for i in self.__students:
            min += i["score"]
        min/=len(self.__students)
        return min
    
    
    
    def get_students(self):
        list1 =[]
        for i in self.__students:
            list1.append((i["name"],i["last_name"]))
        return list1
    
    
    
    
    
    