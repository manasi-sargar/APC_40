morning={"Amit","Rahul","Sneha","Priya","Neha"}
afternoon={"Sneha","Priya","Rohit","Kiran","Amit"}
print("Present in both sessions:",morning&afternoon)
print("Only in morning:",morning-afternoon)
print("Only in afternoon:",afternoon-morning)
print("Present in at least one session:",morning|afternoon)