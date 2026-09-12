N = int(input())
c = int(input())
p = int(input())

if p <= N:
    ticket_cost = c
else:
    positions_beyond = p - N
    ticket_cost = c + (5 * positions_beyond)

print(ticket_cost)


    
    
