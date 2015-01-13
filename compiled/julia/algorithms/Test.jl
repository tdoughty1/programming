import Sorts

n = 10000000

j = 1
while j <= 10
    j += 1
    testArray = rand(n)

    start = time()
    i = 0
    while i <= 1
        Sorts.mergesort(testArray)
        i += 1
    end
    finish=time()

    alg_time = (finish-start)

    @printf("Algorithm took %.4f ms for n = %d\n", alg_time*1000, n)
end
