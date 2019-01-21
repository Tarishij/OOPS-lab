class Date{
    private int day;
    private int month;
    private int year;
     Date(){
        day=12;
        month=3;
        year=1993;
      }
     Date(int day,int month,int year){
        this.day=day;
        this.month=month;
        this.year=year;
      }
     Date(Date d){
        day=d.day;
        month=d.month;
        year=d.year;
     }
    public void print(){
        System.out.println("Day:"+day+" Month:"+month+" Year:"+year);
    }
}

