lst =[1,3,5,4,2,6,9,7,8,10]
# IT WILL SORT THE ABOVE LIST [1,2,3,4,5,6,7,8,9,10]
lst.sort()
# FOR FIRST PLACE
first=0
# FOR LAST PLACE
last=len(lst)-1
# FOR MIDDILE
mid=(first+last)//2
# FOR SEARCHING THE NUMBER
searchNum=int(input("Enter the number you want to search: "))
found=False
while(first<=last and not found):
    mid=(first+last)//2
    # IT WILL MATCH THE CONDITIONS THE FIND THE MID POSITION 
    # IF NUMBER AT MID POSITION THEN IT WILL PRINT THIS
    if lst[mid] == searchNum:
        print(f"The number is at location {mid}")
        found=True
    # IF NOT THEN AGAIN IT WILL SEARCH FROM MID POSITION
    else:
        if searchNum< lst[mid]:
            last=mid-1
        else:
            first=mid+1
# IF NUMBER IS NOT IN THE LIST
if found== False:
    print("The number was not found")