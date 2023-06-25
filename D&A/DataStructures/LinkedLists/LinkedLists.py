{
  "value": 4,
  "next" : None
}

# !This is what a node essentially is but not exactly this. 

# *So if we want to point Node 7 at Node 4 > This is kinda how it would it look
{
  "value": 7,
  "next" : {
              "value": 4,
              "next" : None
            }
}

# head -> (11) -> (3) -> (23) -> (7) -> tail-> (4) (APPENDING 4)
 
head = { 
          "value": 11, 
          "next" : {
                      "value": 3,
                      "next" : {
                                "value": 23,
                                "next" : {
                                            "value": 7,
                                            "next" : {
                                                        "value": 4, # <-Tail
                                                        "next" : None
                                                      }
                                          }
                                }
                    }
        }

print(head["next"]["next"]["value"]) #! Prints 23

# !!!!!! THIS IS HOW WE RUN AN ACTUAL LINKED LIST
# ?print(my_linked_list.head.next.next.value)