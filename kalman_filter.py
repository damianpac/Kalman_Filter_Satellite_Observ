import numpy as np


def kalman_filter(signal):

    gpsnoise = 0.5                                          # GPS Noise
    Q = 0.1                                                 # Process Noise Covariance
    R = 0.09                                                # Measurement Noise Covariance
    length = len(signal)                                    # Number of observations
    duration = length                                       # Time of simulation
    dt = 1                                                  # Time step
    t = np.linspace(0, duration, duration)                  # Total time of measurement

    Em = np.mean(signal)                                    # Mean Value
    x = Em
    P = Q

    e_kal = []                                              # Empty data set for predicted values
    e_ds = []                                               # Empty data set for measured values

# Prediction and correction phase

    for i in range(duration):
            e_sym = signal[i]
            P = P + Q
            K = P*(P+R)**(-1)
            x = x + K*(e_sym-x)
            P = (1-K)*P
            e_ds.append(e_sym)
            e_kal.append(x)

    return np.array([np.transpose(e_kal)])