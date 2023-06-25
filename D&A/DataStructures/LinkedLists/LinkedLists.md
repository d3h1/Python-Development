# Linked Lists - (11-Head)->(3)->(23)->(7-Tail)->none

## BIG O Of Linked List
##### APPEND 4 TO end: O(1)
    (11)->(3)->(23)->(7)->(4)->none

    To make this occur . . . 

        - CURRENT LAST NODE needs to point to 
        new node being added. 

        - Tail will point to it and then 
        it is added to the list

        - It is O(1) because it takes
        same amount of operations each 
        time to add 

##### REMOVE 4 FROM end: O(n)
    (11)->(3)->(23)->(7)->none

    To make this occur . . .

        - TAIL on 4 must be brought back a node
        and made equal to the PREVIOUS NODE before 7 now
        which is NODE 23. 

        - Go through each value to get to NODE 23's pointer
        to NODE 7 and point the tail to that pointer 
        making NODE 7 the tail and end of the linked list after
        removing 4

        - Going through each value of a list is O(n)

##### APPEND 4 TO front: O(1)
    (4)->(11)->(3)->(23)->(7)->none

    To make this occur . . . 

        - The 4 NODE needs to point at the 11 NODE. 
        The head will be set equal to that pointer
        making 4 the new HEAD NODE

        - Same amount of operations making it O(1)

##### REMOVE 4 FROM front: O(1)
    (11)->(3)->(23)->(7)->none

    To make this occur . . . 

        - The 4 NODE is removed and then the head tag
        needs to point to the the 11 NODE.  

        - Using head.next() will move the head over to the 
        NEXT NODE once removing 4

        - Same amount of operations to remove it so O(1)

##### APPEND 4 TO middle: O(n)
    (11)->(3)->(23)->(4)->(7)->none

    To make this occur . . . 

        - Find the node by starting at HEAD and iterating 
        through the list until you reach NODE 23.

        - We want the 4 to point at the 7 NODE. So we have the pointer of 4 equal to the current pointer 
        of 23 (which is looking at 7) and then the pointer of 23
        look towards 4 now

        - Inserting 4 in the middle and having to look through the list
        makes this O(n)

##### REMOVE 4 FROM middle: O(n)
    (11)->(3)->(23)->(7)->none

    To make this occur . . . 

        - Look through the list and find NODE 4. 
        Since NODE 4's pointer is looking at 7, NODE 23 will equal to that pointer. 

        - This allows us to remove 4 from the linked list

        - Iterating through the list like that makes it O(n)


##### LOOKUP 23: O(n)
    (11)->(3)->(23)->(7)->none

    To make this occur . . . 

        - Iterate through the list untill you find 
        NODE 23

        - If looking by index, you have to start at head
        and iterate until index of 23


