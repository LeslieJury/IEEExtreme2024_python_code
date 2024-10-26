def arrange_bricks():
    N, x = map(int, input().split())
    
    bricks = list(map(int, input().split()))

    bricks.sort()

    stacks = []

    for brick in bricks:
        placed = False
        for stack in stacks:
            if stack[-1] + x <= brick:
                stack.append(brick)
                placed = True
                break
        
        if not placed:
            
            stacks.append([brick])


    print(len(stacks)) 
    for stack in stacks:
        print(len(stack), ' '.join(map(str, stack[::-1])))


arrange_bricks()
