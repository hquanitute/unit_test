public class file{
    public int sum(int a, int b) {
        return a + b;
    }
    public int subtraction(int a, int b) {
        return a - b;
    }
    public int multiplication(int a, int b) {
        return a * b;
    }
    public int divison(int a, int b) throws Exception {
        if (b == 0) {
            throw new Exception("Divider can't be zero");
        }
        return a / b;
    }
    public boolean equalIntegers(int a, int b) {
        boolean result = false;
        if (a == b) {
            result = true;
        }
        return result;
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
    private static file calculator;
    @BeforeClass
    public static void initCalculator() {
        calculator = new file();
    }
    @Before
    public void beforeEachTest() {
        System.out.println("This is executed before each Test");
    }
    @After
    public void afterEachTest() {
        System.out.println("This is exceuted after each Test");
    }
    @Test
    public void testSum() {
        int result = calculator.sum(3, 4);
        assertEquals(7, result);
    }
    @Test
    public void testDivison() {
        try {
            int result = calculator.divison(10, 2);
            tassertEquals(5, result);
        } catch (Exception e) {
            e.printStackTrace(System.err);
        }
    }
    @Test(expected = Exception.class)
    public void testDivisionException() throws Exception {
        calculator.divison(10, 0);
    }
    @Ignore
    @Test
    public void testEqual() {
        boolean result = calculator.equalIntegers(20, 20);
        assertFalse(result);
    }
    @Test(expected = AssertionError.class)
    public void testSubstraction() {
        int result = 10 - 3;
        assertTrue(result == 9);
    }
}