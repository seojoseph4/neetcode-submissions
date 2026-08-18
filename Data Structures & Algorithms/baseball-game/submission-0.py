class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        
        for op in operations:
            
            if op == "+":
                x = st.pop()
                y = st.pop()
                st.append(y)
                st.append(x)
                st.append(x+y)
            elif op == "C":
                st.pop()
            elif op == "D":
                x = st.pop()
                st.append(x)
                st.append(2*x)
            else:
                st.append(int(op))

        return sum(st)