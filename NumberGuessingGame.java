import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    private static final Scanner scanner = new Scanner(System.in);
    private static final Random random = new Random();

    public static void main(String[] args) {
        int round = 1;
        int totalAttempts = 0;

        System.out.println("=================================");
        System.out.println("       NUMBER GUESSING GAME");
        System.out.println("=================================");

        boolean playAgain = true;
        while (playAgain) {
            int secretNumber = random.nextInt(100) + 1;
            int maxAttempts = 7;
            int attempts = 0;
            boolean guessedCorrectly = false;

            System.out.println("\\nRound " + round + " — Guess a number from 1 to 100.");
            System.out.println("You have " + maxAttempts + " attempts.");

            while (attempts < maxAttempts) {
                System.out.print("Attempt " + (attempts + 1) + "/" + maxAttempts + ": ");
                String input = scanner.nextLine().trim();

                int guess;
                try {
                    guess = Integer.parseInt(input);
                } catch (NumberFormatException e) {
                    System.out.println("Please enter a valid whole number.");
                    continue;
                }

                if (guess < 1 || guess > 100) {
                    System.out.println("Enter a number between 1 and 100.");
                    continue;
                }

                attempts++;
                totalAttempts++;

                if (guess == secretNumber) {
                    guessedCorrectly = true;
                    System.out.println("Correct! You guessed it in " + attempts + " attempt(s).");
                    break;
                } else if (guess > secretNumber) {
                    System.out.println("Too High!");
                } else {
                    System.out.println("Too Low!");
                }

                System.out.println("Attempts remaining: " + (maxAttempts - attempts));
            }

            if (!guessedCorrectly) {
                System.out.println("You Lost! The number was " + secretNumber + ".");
            }

            System.out.println("Round " + round + " summary: " +
                    (guessedCorrectly ? "guessed in " + attempts + " attempt(s)" : "failed after " + attempts + " attempt(s)"));
            System.out.print("Play again? (yes/no): ");
            String answer = scanner.nextLine().trim().toLowerCase();
            playAgain = answer.equals("yes") || answer.equals("y");
            round++;
        }

        System.out.println("\\nThanks for playing!");
        System.out.println("Rounds played: " + (round - 1));
        System.out.println("Total valid guesses: " + totalAttempts);
        scanner.close();
    }
}
