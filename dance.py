import time

frames =[
        [[" ", " ", " ", " ", " "],
        [" ", " ", "O", " ", " "],
        [" ", "_", "|", "_", "/"],
        ["/", " ", "|", " ", " "],
        [" ", "/", " ", "\\", " "],
        [" ", "\\", " ", "", " |"],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]],
        
        [[" ", " ", " ", " ", " "],
        [" ", " ", "O", " ", " "],
        [" ", "_", "|", "_", " "],
        ["|", " ", "|", " ", "|"],
        [" ", "/", " ", "\\", " "],
        [" ", "\\", " ", "/", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]],

        [[" ", " ", " ", " ", " "],
        [" ", " ", "O", " ", " "],
        ["\\", "_", "|", "_", " "],
        [" ", " ", "|", " ", "\\"],
        [" ", "/", " ", "\\", " "],
        [" ", "|", " ", "/", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]]
        ]


while(True):    
        for i in range(0, len(frames)):
                print("im the dancin man")
                for j in range(0, len(frames[0])):
                        for k in range(0, len(frames[0][0])):
                                print(frames[i][j][k], end="")
                        print()
                time.sleep(.3)