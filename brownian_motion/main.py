import numpy as np
import matplotlib.pyplot as plt

def main():
    n = 20
    T = 1.
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]

    dB = np.sqrt(dt) * np.random.normal(size=(n-1,))
    B0 = np.zeros(shape=(1, ))
    B = np.concatenate((B0, np.cumsum(dB)))
    plt.plot(times, B)
    plt.show()


if __name__ == "__main__":
    main()