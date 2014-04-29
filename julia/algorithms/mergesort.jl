function mergesort(array_in)

    n = length(array_in)

    if n <= 1
        return array_in
    else
        subarray1 = array_in[1:ceil(n/2)]
        subarray2 = array_in[ceil(n/2)+1:n]
        a = mergesort(subarray1)
        b = mergesort(subarray2)
        array_out = qmerge(a, b)
        return array_out
    end

end

function qmerge(array1, array2)

    imax = length(array1)
    jmax = length(array2)
    kmax = imax + jmax + 1

    array_out = zeros(imax+jmax)

    i = 1
    j = 1
    k = 1

    while k < kmax

        # Check if at end of either array
        if i == (imax + 1)
            array_out[k:end] = array2[j:end]
            return array_out
        end

        if j == (jmax + 1)
            array_out[k:end] = array1[i:end]
            return array_out
        end

        # Standard Case
        if array1[i] < array2[j]
            array_out[k] = array1[i]
            i += 1
            k += 1
        else
            array_out[k] = array2[j]
            j += 1
            k += 1
        end
    end
end
