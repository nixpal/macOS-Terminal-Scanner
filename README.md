# macOS Terminal Wifi Scanner and Tracer V2
### Author : Tarek Talaat

- This is the second version of the other macOS Terminal wifi scanner. The first version using shell script with Awk
to print a nice organized output of airport utility on macOS.

- This version uses Python and it has three options for scanning.
  * First option is to use distance instead of dBi and the distance is measured in Meter
  * Second option is to use the normal dBi metric
  * Third option is to trace a specific AP by providing the mac address you get from one of the first two options.
  
  
### Usage: 
  - ./WiTracer -b ec:bb:59:aa:bc:50          
  - ./WiTracer -d -all 
  - ./WiTracer -x -all   
 
<img width="998" alt="dBi" src="https://user-images.githubusercontent.com/19849718/59215238-5c2b6a00-8b7e-11e9-97fc-edb62ff1ed38.png">

<img width="979" alt="Meter" src="https://user-images.githubusercontent.com/19849718/59215266-6cdbe000-8b7e-11e9-8a0b-599d2b6e138d.png">

<img width="1021" alt="far" src="https://user-images.githubusercontent.com/19849718/59215288-7f561980-8b7e-11e9-94fd-ae7ac999b617.png">

<img width="985" alt="home" src="https://user-images.githubusercontent.com/19849718/59215279-77967500-8b7e-11e9-9b97-f18481196dda.png">


  



### Thank you all.
