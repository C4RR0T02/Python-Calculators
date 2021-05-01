#Programme to calculate Total Cost

#User input options

item = str(input("Enter item name: "))
cost = float(input("Enter cost of item in $: "))
gst_rate = float(input("Enter the GST rate in %: "))

#cost of product after GST

gst = cost * gst_rate
total_cost = cost + gst

#round off value

total_rounded = round(total_cost,2)

#output of cosft after GST

#print ("The cost of ", item, " is $", total_rounded, " after GST.")
print ("The cost after GST is $", total_rounded, " .")
