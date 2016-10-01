"""
This function searches through a mass list l for peaks k with a user-specified ppm cutoff.

Parameters:
    k: 1D numpy array object containing the masses we want to search for.

    l: 1D numpy array object containing the spectrum (peak list) that we want to search through.

    ppm: ppm cutoff. Masses in k that are not present in l within tolerance will be rejected.

Returns:
    il: numpy array object the same size as k. if il[i] >= 0 then k[i] ~= l[il[i]] within 10 ppm.
        If il[i] < 0 then there is no match for k[i] in l.

"""
import numpy as np


def searchppm(l, k, ppm=10):
    ln = np.size(l)
    # Run numpy's built-in binary search to generate indices idx
    idx = np.searchsorted(l, k)

    # process idx so it doesn't contain entries greater than ln-1.
    idx = idx - (idx==ln)*1

    # This step makes sure that indices in idx always point to the CLOSEST match
    # in l for entries in k. Standard behavior of np.searchsorted is to assign k[i]
    # to the first index j in l for which j[l] > k[i]. e.g.:
    #               l = [1000, 2000, 3000] and k=[2001]
    # we will have:
    #               idx = np.searchsorted(l, k) = 3
    #               np.abs(k-l[idx]) = 999
    #               np.abs(k-l[idx-1]) = 1
    #
    # So, idx = idx - 1, correcting the index.
    idx = idx - (np.abs(k-l[idx]) > np.abs(k-l[idx - 1]))*1

    # initialize an array of masses where corresponding to indices in idx.
    match_masses = l[idx]


    # array of ppm error values for matches.
    err = 1000000 * np.abs(match_masses - k) / match_masses

    # np.invert((err<=10)*1) is an array with 0's if there is a match within the specified ppm
    # and 1's if no match. 0 % 2 = 0, 1 % 2 = 1. So We end up with an array where 1 corresponds
    # to a match and -1 corresponds to no match.
    within_threshold =  (-1)**(np.invert(err <= ppm)*1 % 2 )

    # Final list of matching indices. Negative indices corespond to no match.
    il = idx * within_threshold

    return il






