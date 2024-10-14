import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class LotterySystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);        
        // 產生中獎號碼
        int[] winningNumbers = generateWinningNumbers();
        int specialNumber = winningNumbers[6];
        int[] regularWinningNumbers = Arrays.copyOf(winningNumbers, 6);

        System.out.println("開獎號碼是: " + Arrays.toString(regularWinningNumbers));
        System.out.println("特別號碼是: " + specialNumber);

        while (true) {    
            // 輸入使用者號碼
            int[] userNumbers = new int[6];
            Set<Integer> userNumbersSet = new HashSet<>();
            System.out.println("請輸入你的 6 個號碼 (範圍 1-49): ");
            for (int i = 0; i < 6; i++) {
                int num = scanner.nextInt();
                if (num < 1 || num > 49) {
                    System.out.println("輸入的號碼不在範圍內，請重新輸入號碼。");
                    i--;  
                } else if (userNumbersSet.contains(num)) {
                    System.out.println("輸入的號碼已經存在，請重新輸入號碼。");
                    i--;  
                } else {
                    userNumbers[i] = num;
                    userNumbersSet.add(num);
                }
            }

            // 對獎
            String prize = checkPrize(userNumbers, regularWinningNumbers, specialNumber);
            System.out.println("恭喜你中了: " + prize);

            System.out.println("請選擇：");
            System.out.println("1. 再玩一次!!!");
            System.out.println("2. 離開");

            int choice = scanner.nextInt();
            if (choice == 2) {
                System.out.println("感謝使用，再見！");
                break;
            }
        }
        
        scanner.close();
    }

    // 使用 Math 套件生成中獎號碼
    private static int[] generateWinningNumbers() {
        Set<Integer> numberSet = new HashSet<>();
        Random random = new Random();
        while (numberSet.size() < 7) {
            int number = random.nextInt(49) + 1;
            numberSet.add(number);
        }
        int[] numbers = numberSet.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(numbers, 0, 6); 
        return numbers;
    }

    // 對獎函式
    private static String checkPrize(int[] userNumbers, int[] winningNumbers, int specialNumber) {
        int matchCount = 0;
        boolean specialMatch = false;
        Set<Integer> winningSet = new HashSet<>();
        
        for (int num : winningNumbers) {
            winningSet.add(num);
        }

        for (int num : userNumbers) {
            if (winningSet.contains(num)) {
                matchCount++;
            }
            if (num == specialNumber) {
                specialMatch = true;
            }
        }

        if (matchCount == 6) {
            return "頭獎";
        } else if (matchCount == 5 && specialMatch) {
            return "貳獎";
        } else if (matchCount == 5) {
            return "參獎";
        } else if (matchCount == 4 && specialMatch) {
            return "肆獎";
        } else if (matchCount == 4) {
            return "伍獎";
        } else if (matchCount == 3 && specialMatch) {
            return "陸獎";
        } else if (matchCount == 2 && specialMatch) {
            return "柒獎";
        } else if (matchCount == 3) {
            return "普獎";
        } else {
            return "未中獎";
        }
    }
}