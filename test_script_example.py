import opstrat as op


"""
This is an options profit and loss simulator
"""

model=input("To run vanilla call or put payoff plot simulator press 1")

if model =="1":
    op_type=input("Enter roption type (c)all or (p)ut:")
    spot=float(input("Enter spot price"))
    spot_range=float(input("Enter spot % range, here +/- 1 x scaled vol. has 68% chance of happening:"))
    strike=float(input("Enter strike price:"))
    tr_type=input("Enter transaction type (b) for long (s) for short:")
    op.single_plotter(op_type,spot,spot_range,strike,tr_type)
    
