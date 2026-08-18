class Solution {
    public boolean isPalindrome(String s) {

        s = s.toLowerCase();
        String result = s.replaceAll("[\\p{Punct}]", "");
        result = result.replaceAll("\\s", "");
        int pointone = 0;
        int pointtwo = result.length()-1;
        System.out.println(result);
        while (pointone < pointtwo) {
            // while(!Character.isLetter(s.charAt(pointone)) ||!Character.isLetter(s.charAt(pointtwo))) {
            //     if(pointone >= pointtwo){
            //         break;
            //     }
            //     if(!Character.isLetter(s.charAt(pointone))) {
            //         pointone++;
            //     }
            //     if(!Character.isLetter(s.charAt(pointtwo))) {
            //         pointtwo--;
            //     }
            // }
            char one = result.charAt(pointone);
            char two = result.charAt(pointtwo);
            System.out.println(one);
            System.out.println(two);
            if (one != two) {
                return false;
            }
            pointone++;
            pointtwo--;
        }

        return true;
    }
}
