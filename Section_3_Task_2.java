/*
2. Tech Quiz App (C++/Java) 
Features: 
Console MCQ quiz  
Score display 
Restart option
*/
import java.util.*;

class QuizApp 
{
     static String[] javaQuestions = {
    "1. Which of the following is not a primitive data type in Java?\nA) int\nB) boolean\nC) String\nD) char",
    "2. What does JVM stand for?\nA) Java Virtual Machine\nB) Java Variable Machine\nC) Java Verified Machine\nD) Java Visual Machine",
    "3. Which keyword is used to create a class in Java?\nA) class\nB) create\nC) new\nD) function",
    "4. How do you declare an array in Java?\nA) int arr[];\nB) int[] arr;\nC) Both A and B\nD) float arr[]",
    "5. Which method is the entry point of a Java application?\nA) start()\nB) run()\nC) main()\nD) init()",
    "6. What is the default value of a boolean variable in Java?\nA) 0\nB) false\nC) true\nD) null",
    "7. Which of the following is a valid comment in Java?\nA) // comment\nB) /* comment */\nC) Both A and B\nD) None of the above",
    "8. What is the output of the following code: System.out.println(5 + 5 + '5');\nA) 55\nB) 105\nC) 10\nD) 5",
    "9. Which keyword is used to inherit a class in Java?\nA) implements\nB) extends\nC) inherits\nD) base",
    "10. What is the purpose of the final keyword in Java?\nA) To prevent a method from being overridden\nB) To prevent a class from being subclassed\nC) To create constants\nD) All of the above",
    "11. Which of the following is not an access modifier in Java?\nA) public\nB) private\nC) protected\nD) confidential",
    "12. What is an interface in Java?\nA) A class with abstract methods only\nB) A class that cannot be instantiated\nC) A contract for classes to implement\nD) Both A and C",
    "13. What will be the output of this code?\nint x = 10;\nif (x > 5) {\n    System.out.println(\"greater\");\n} else {\n    System.out.println(\"smaller\");\n}\nA) greater\nB) smaller\nC) error\nD) none",
    "14. Which collection class uses a key-value pair?\nA) ArrayList\nB) HashMap\nC) HashSet\nD) TreeSet",
    "15. What does the 'static' keyword mean in Java?\nA) The method can be called without creating an object\nB) The variable retains its value between instances\nC) Both A and B\nD) None of the above",
    "16. Which exception is thrown when an attempt is made to access an out-of-bounds index of an array?\nA) NullPointerException\nB) IndexOutOfBoundsException\nC) ArrayStoreException\nD) ArithmeticException",
    "17. How do you release unused memory in Java?\nA) Using free()\nB) Using delete()\nC) Using garbage collection\nD) Memory is managed automatically",
    "18. What is the purpose of the synchronized keyword?\nA) To ensure a method is executed by only one thread at a time\nB) To prevent deadlocks\nC) To lock an object\nD) All of the above",
    "19. Which of the following is a wrapper class for the int data type?\nA) Integer\nB) IntClass\nC) Number\nD) Float",
    "20. What is the output of the code below?\nString str = \"Hello\";\nstr.concat(\" World\");\nSystem.out.println(str);\nA) Hello\nB) Hello World\nC) error\nD) Hello World!"
    };

    static String[] javaAnswers = {
    "C",
    "A",
    "A",
    "C",
    "C",
    "B",
    "C",
    "B",
    "B",
    "D",
    "D",
    "D",
    "D",
    "B",
    "C",
    "A",
    "C",
    "D",
    "A",
    "A"
};


    public static void main(String[] args)
    {
        System.out.println("Welcome to Tech Quiz App");
         Scanner sc = new Scanner(System.in);
        int choice;
        do{
        int score = 0;
        for (int i = 0; i<20;i++)
        {
            System.out.println(javaQuestions[i]);
            System.out.println("Enter Your Choice");
           
            String userAnswer = sc.nextLine();
            if (userAnswer.equalsIgnoreCase(javaAnswers[i]))
            {
                System.out.println("Correct");
                score++;
            }
            else
            {
                System.out.println("Incorrect");
            }

        }
            System.out.println("Your score: " + score + "/" + javaQuestions.length);
            System.out.println("Do you want to play again? Enter 1 for Yes or 0 for No:");
            choice = Integer.parseInt(sc.nextLine());

        }while(choice==1);
        System.out.println("Thank you for playing!");


    }
}
