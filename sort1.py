def liczenie_n(nums):
    n = 0
    for x in nums:
        n += 1
    return n
def sortowanie_bambelkowe(n):
    liczenie_n(nums)
    i = 0
    for j in range(0, n):
        for i in range(0, n - 1 - i):
            if (nums[i] > nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1],nums[i]

def proste_wstawianie(n):
    for i in range(1, n):
        x = nums[i]
        j = i
        while j > 0 and x < nums[j - 1]:
            nums[j] = nums[j - 1]
            j = j - 1
        nums[j] = x

def scalanie(nums):
    if (liczenie_n(nums)) > 1:
        mid = int(liczenie_n(nums) / 2)
        le = nums[:mid]
        ri = nums[mid:]
        scalanie(le)
        scalanie(ri)

        i = 0
        j = 0
        k = 0
        while i < liczenie_n(le) and j < liczenie_n(ri):
            if le[i] < ri[j]:
                nums[k] = le[i]
                i += 1
            else:
                nums[k] = ri[j]
                j += 1
            k += 1

        #pętla sprawdzająca
        while i < liczenie_n(le):
            nums[k] = le[i]
            i += 1
            k += 1
        while j < liczenie_n(ri):
            nums[k] = ri[j]
            j += 1
            k += 1

def zliczanie(nums):
    i = 0
    while i < liczenie_n(nums):
        klucz = nums[i]
        j = i - 1
        while j >= 0 and klucz < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = klucz
        i += 1

def wybieranie(nums):
    i = 0
    while i < liczenie_n(nums) -1:
        index = i
        j = i + 1
        while j < liczenie_n(nums):
            if nums[index] > nums[j]:
                index = j
            j += 1
        nums[i],nums[index]=nums[index],nums[i]
        i += 1

def binarne(nums,x):
    licznik = 0
    same = 0
    #zasięg od najmniejszego do największego
    lo = 0
    hi = liczenie_n(nums)
    while lo <= hi:
        #rozpoczęcie wyszukiwania od środka
        mid = lo + int((hi - lo) / 2)
        licznik += 1

        #znalezienie szukenj liczby x
        if nums[mid] == x:
            print('Ilość zgadywania: ', licznik)
            return mid

        #jesli szukana x jest większa od środka
        elif nums[mid] < x:
            lo = mid + 1

        #jesli szukana x jest mniejsza od środka
        else:
            hi = mid - 1
    print('Ilość zgadywania: ', licznik)
    return 'Brak'

#       wstawianie

with open('sort1.txt', 'r') as f:
    nums = [int(num) for num in f.read().replace('\n', '').split('\t')]

print('Sortowanie przez wstawianie')
start = time.time()
proste_wstawianie(liczenie_n(nums))
stop = time.time()
print("--- %s sekund ---\n" % round( stop - start, 2))

#       scalanie

with open('sort1.txt', 'r') as f:
    nums = [int(num) for num in f.read().replace('\n', '').split('\t')]

print('Sortowanie przez scalaniee')
start = time.time()
scalanie(nums)
stop = time.time()
print("--- %s sekund ---\n" % round( stop - start, 2))

#       zliczanie

with open('sort1.txt', 'r') as f:
    nums = [int(num) for num in f.read().replace('\n', '').split('\t')]

print('Sortowanie przez zliczanie')
start = time.time()
zliczanie(nums)
stop = time.time()
print("--- %s sekund ---\n" % round( stop - start, 2))

#       szukana liczba
print('Szukana wartość to: ',x,'\n')

#       wyszukiwanie binarne

proste_wstawianie(liczenie_n(nums))
print('Pozycja nr: ',binarne(nums,x))


#       wybieranie

with open('sort1.txt', 'r') as f:
    nums = [int(num) for num in f.read().replace('\n', '').split('\t')]

print('Sortowanie przez wybieranie')
start = time.time()
wybieranie(nums)
stop = time.time()
print("--- %s sekund ---\n" % round( stop - start, 2))


#       babelkowe

with open('sort1.txt', 'r') as f:
    nums = [int(num) for num in f.read().replace('\n', '').split('\t')]

print('Sortowanie bombelkowe')
start = time.time()
sortowanie_bambelkowe(liczenie_n(nums))
stop = time.time()
print("--- %s sekund ---\n" % round( stop - start, 2))