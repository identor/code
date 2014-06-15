from stopwatch import StopWatch

def main():
    s = StopWatch()
    s.start()
    import compute_pi
    s.stop()
    print("Elapsed time:", round(s.time(), 2), "seconds")

main()
