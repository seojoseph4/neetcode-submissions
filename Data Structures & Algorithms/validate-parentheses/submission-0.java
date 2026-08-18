class Solution {
    public boolean isValid(String s) {
        Stack<Character> open = new Stack<>();
        HashMap<Character, Character> match = new HashMap<>();
        match.put(')', '(');
        match.put('}', '{');
        match.put(']', '[');
        for(int i = 0; i < s.length(); i++) {
            char temp = s.charAt(i);
            if (temp=='(' || temp =='[' || temp=='{') {
                open.push(temp);
            } else{
                if (!open.isEmpty() && match.get(temp)==open.peek()) {
                    open.pop();
                } else {
                    return false;
                }
            }

        }
        return open.isEmpty();
    }
}
