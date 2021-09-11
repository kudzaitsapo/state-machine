# State Machine
This is a state machine for chatbots which rely on user input to determine the reponse.

eg: <br />
User> Hi <br />
Bot> Hello, what do you want? <br />
     1. Fried rice <br />
     2. Chicken <br />
     3. Dumplings <br />
     4. Something else <br />
     
User> 1 <br />
Bot> You want fried rice? Choose drink: <br />
    1. Coke <br />
    2. Pepsi <br />
    3. Orange Juice <br />
    4. Water <br />
    5. Apple Juice <br />
    
User> 5 <br />
Bot> You will get your fried rice with apple juice in 5 mins. <br />


In the above scenario, the user had multiple options and it can be difficult to keep track of. The solution to this issue, is to use a state machine. This is 
an example of a state machine that can be used for such.

NB: It's not perfect, but for what I wanted, it worked so :man_shrugging:
