import java.util.Calendar;

public class CalculateYearsOld {
  //Calculate years old based on days, months and years.
  public static void main(String[] args) {
   Calendar actualDate = Calendar.getInstance();
   
   int birthDay = 22;
   int birthMonth = 06;
   int birthYear = 2000;
   
   int actualDay = actualDate.get(Calendar.DAY_OF_MONTH);
   int actualMonth = actualDate.get(Calendar.MONTH + 1);
   int actualYear = actualDate.get(Calendar.YEAR);
   
   int yearsOld = 0;
   
   if(actualMonth < birthMonth){
     yearsOld = actualYear - birthYear - 1;
   } else if(actualMonth > birthMonth){
     yearsOld = actualYear - birthYear;
   } else {
     if(actualDay < birthDay){
       yearsOld = actualYear - birthYear - 1;
     } else if(actualDay > birthDay){
       yearsOld = actualYear - birthYear;
     } else {
       System.out.println("Happy birthday!");
       yearsOld = actualYear - birthYear;
     }
   }
   
   System.out.println(yearsOld+" years old");
  }
}