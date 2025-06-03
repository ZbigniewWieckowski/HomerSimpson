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
Homer Simpson ... working  
D'oh!  
Homer Simpson noticed a safety hazard at the plant!  
Homer Simpson is still working hard at the plant...fixed the issue and moving on.  
Homer Simpson ... working  
Woohoo!  
Homer Simpson ... working  
Woohoo!  
Homer Simpson noticed a safety hazard at the plant!  
Traceback (most recent call last):  
  File "/home/.../Homer/Homer.py", line 62, in <module>  
    homer.keepWorking()  
  File "/home/.../Homer/Homer.py", line 55, in keepWorking  
    raise MissingDonutException("Homer's workday was interrupted by a donut craving!")  
MissingDonutException: Homer's workday was interrupted by a donut craving!  
