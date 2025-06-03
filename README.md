HomerSimpson - sample code for illustration of pitfalls of lower priority exception overriding higher priority exception inside the 'finally' block.

<b> Sample Run</b>

$ python Homer.py  

...

Homer Simpson ... working  
D'oh!  
Homer Simpson ... working  
Why you little!  
Homer Simpson ... working  
Mmm... donuts  
Homer Simpson ... working  
Woohoo!  
Homer Simpson ... working  
Woohoo!  
Homer Simpson ... working  
Why you little!   
Homer Simpson noticed a safety hazard at the plant!  
Traceback (most recent call last):  
  File "/home/PATH/Homer/Homer.py", line 47, in keepWorking  
    raise NuclearMeltdownException("Oh no!")  
NuclearMeltdownException: Oh no!  
  
During handling of the above exception, another exception occurred:  
  
Traceback (most recent call last):  
  File "/home/PATH//Homer/Homer.py", line 59, in <module>  
    homer.keepWorking()  
  File "/home/PATH//Homer/Homer.py", line 53, in keepWorking  
    raise MissingDonutException("Homer's workday was interrupted by a donut craving!")  
MissingDonutException: Homer's workday was interrupted by a donut craving!  
