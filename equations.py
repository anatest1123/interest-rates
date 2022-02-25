def interest_equation(u_t,u_o,r_v0,r_s1,r_s2):
    if u_t <= 80:
        r_v = r_v0 + (u_t/(u_o/100)) * (r_s1/100)
    elif u_t > 80:
        r_v = r_v0 + r_s1 + (u_t-u_o)/(1-(u_o/100)) * r_s2/100
    return r_v