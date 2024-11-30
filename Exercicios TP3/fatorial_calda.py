def fatorial_r_calda(n, reserva=1):
    if n == 0 or n == 1:
        return reserva
    else:
        return fatorial_r_calda(n-1, n * reserva)