import numpy as np
import matplotlib.pyplot as plt


def main():
    n = 10000
    d = 10
    end_time = 1.0
    times = np.linspace(0.0, end_time, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n - 1, d))
    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)
    plt.plot(times, B)
    # plt.plot(times, quadratic_variation(B))
    plt.show()


if __name__ == "__main__":
    main()
