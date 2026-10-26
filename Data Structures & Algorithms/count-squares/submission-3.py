class CountSquares:

    def __init__(self):
        self.l = []
        self.hm = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.l.append(point)
        self.hm[tuple(point)]+=1
        

    def count(self, point: List[int]) -> int:
        res = 0
        for x,y in self.l:
            diffx = abs(point[0]-x)
            diffy = abs(point[1]-y)
            if diffx != 0 and diffx == diffy:
                p1 = (point[0],y)
                p2 = (x,point[1])
                p3 = (x,y)
                res+=self.hm[p1]*self.hm[p2]
        return res
        
