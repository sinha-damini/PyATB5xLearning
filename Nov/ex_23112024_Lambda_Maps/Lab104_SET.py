set1 = set(["TheTestingAcademy", "For", "TheTestingAcademy.","for","For"])
print(set1)
#{'for', 'TheTestingAcademy', 'TheTestingAcademy.', 'For'}
#For and for different.
#'TheTestingAcademy' and 'TheTestingAcademy.' are different.
print(len(set1))

for i in set1:
    print(i)

set1.add("Damini")
set1.add("Damini")
set1.add("Damini")
set1.add("TheTestingAcademy")
print(set1)
#{'For', 'TheTestingAcademy.', 'for', 'Damini', 'TheTestingAcademy'}
#will add uniue elements


