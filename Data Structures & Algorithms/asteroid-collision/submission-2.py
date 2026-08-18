class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s= []

        for a in asteroids:
            if not s:
                s.append(a)
            elif s[-1] < 0:
                s.append(a)
            elif a > 0:
                s.append(a)
            else:
                #collision
                alive = True
                while s and alive and s[-1] > 0:
                    print("curr: ", s[-1], "to add:", a)
                    curr = s.pop()
                    if abs(curr) == abs(a):
                        alive = False
                    elif abs(curr) > abs(a):
                        s.append(curr)
                        alive = False
                    else:
                        continue
                if alive:
                    s.append(a)
        return s
                        

            
            
