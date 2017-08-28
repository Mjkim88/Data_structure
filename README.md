# Data structure Assignment Manual
Data Structure Assignment

1. Run init.py first, then you can select the menu you want:
   if you select '99', the system quits
2. init.py calls the functions from menu.py depending on your demand.
3. Next, menu.py calls functions from functions.py.
4. For menu 8, 9, each uses scc.py and dijsktra.py. 

In case of menu 8, where users can find strongly connected components, due to the huge number of users, you can encounter 'RuntimeError: maximum recursion depth exceeded'. Therefore I recommend you to implement menu 7 first, to delete some users, and select menu 8. 
