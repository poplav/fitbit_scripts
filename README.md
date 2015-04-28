fitbit_scripts
======

Crunch the numbers on your fitbit data specifically sleep

print getAvgValLookBack(38, "Minutes Asleep")
print getAvgValOnDay(1, "Minutes Asleep")
print getValDayDistribution("Minutes Asleep")

453
497
[442, 497, 320, 495, 450, 468]

         Date  Minutes Asleep  Minutes Awake  Number of Awakenings  \
46 2015-04-16             495             40                    25   
47 2015-04-17             543             63                    37   
48 2015-04-18             516             39                    22   
49 2015-04-19             492             66                    46   
50 2015-04-20             473             53                    35   
51 2015-04-21             484             25                    22   

    Time in Bed  weekday  
46          553        3  
47          623        4  
48          585        5  
49          588        6  
50          545        0  
51          559        1 
