public class file{
    public int triangleObject(int a, String charater) {
        for (int i=1;i <= a ; i++){
            for (int j=1; j <= i; j++){
                System.out.print(charater);
            }
            System.out.println("  ");
        }
        return 1;
    }
}

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import org.junit.After;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Test;

public class test {
    private static file code;
    @BeforeClass
    public static void initTest() {
        code = new file();
    }
    @Before
    public void beforeEachTest() {
    }
    @After
    public void afterEachTest() {
    }
    @Test
    public void FixedTests() {
        assertEquals("Ths wbst s fr lsrs LL!" ,
                    code.disemvowel("This website is for losers LOL!"));
        assertEquals("N ffns bt,\nYr wrtng s mng th wrst 'v vr rd",
                code.disemvowel
                ("No offense but,\nYour writing is among the worst I've ever read"));
        assertEquals("Wht r y,  cmmnst?" , code.disemvowel("What are you, a communist?"));
    }
    public static String generateRandomChars(String candidateChars, int length) {
        StringBuilder sb = new StringBuilder();
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            sb.append(candidateChars.charAt(random.nextInt(candidateChars.length())));
        }
        return sb.toString();
    }
    public static String C(String Z) {
        return Z.replaceAll("(?i)[aeiou]" , "");
    }
    @Test
    public void RandomTests() {
        for(int i = 0; i < 100; i++) {
            String X = generateRandomChars(
                "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", i + 3);
            assertEquals(C(X) , code.disemvowel(X));
        }
    }
}  
