class bsearch:
    def __init__(self,data,searchinput):
        self.data = data
        self.search = searchinput
        

    def mysearch(self):
        data = list(self.data)
        lenght = len(data)
        mid = int(lenght/2)
        first = 0
        last = lenght-1
        pivot = mid
        while((pivot != first) or (pivot != last)):
            if(int(self.search) == int(data[pivot - 1])):
                return pivot
                break
            elif(self.search > data[pivot - 1]):
                mid =  int((last-first)/2)
                first = pivot
                pivot = pivot + mid
            elif(self.search < data[pivot - 1]):
                last = pivot
                pivot = int(pivot / 2)
                
       


        