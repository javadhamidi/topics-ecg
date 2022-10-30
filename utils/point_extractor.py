
from scipy import signal


def get_r_peaks(lead):
    return signal.find_peaks(lead, height=((max(lead) - np.mean(lead)) * 0.75))


def get_s_points(lead, r_peaks):
    s_points = []

    for i in r_peaks:
        s_points.append(
            i + np.argmin(lead[i:i+50])
        )
        
    return s_points


def get_q_points(lead, r_peaks):
    q_points = []

    for i in r_peaks:
        q_points.append(
            i - np.argmin(np.flip(lead[i-50:i]))
        )
    return q_points


def get_j_points(lead, r_peaks):
    degree_poly = 5  # degree polynomial
    
    j_points = []
    
    for point in range(len(r_peaks) - 1):
        x_vals = np.array(range(1, 100))
        
        regress_func = np.poly1d(np.polyfit(x_vals, [ lead[r_peaks[point] + i] for i in x_vals ], degree_poly))

        j_point = signal.find_peaks(-np.gradient(regress_func(x_vals)))[0][0]
        j_points.append(r_peaks[point] + j_point)

    return j_points
    