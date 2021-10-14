from tools import TimeTool, ECalculator

if __name__ == "__main__":
    timer = TimeTool()
    timer.start()
    calculator = ECalculator()
    calculator.value_e(100000)
    value_e = calculator.get_e()

    print("E = %12.8f | A = %d | N = %d" % (value_e, calculator.a, calculator.n))
    print("TIME = %.6f seconds" % (timer.get_time()))
