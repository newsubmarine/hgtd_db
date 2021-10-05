import scipy
original = [0, 1, 0, 0, 1, 1, 0, 0]
impulse_response = [2, 1]
recorded = scipy.signal.convolve(impulse_response, original)
print(recorded)
# [0 2 1 0 2 3 1 0 0]
recovered, remainder = scipy.signal.deconvolve(recorded, impulse_response)
print(recovered, remainder)
# [ 0.  1.  0.  0.  1.  1.  0.  0.] [ 0.  0.  0.  0.  0.  0.  0.  0.  0.]
