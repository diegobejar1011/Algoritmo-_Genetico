from classes.GeneticAlgorithm import GeneticAlgorithm
#     global people

#     a = int(input())
#     b = int(input())
#     dx = float(input())

#     n = getN(b, a, dx)
#     n_bits = getBits(n)

#     dx_ajustada = getDx(b, a, n_bits)

#     max = getMaxBinary(n_bits)

#     print(f"Puntos: {n}")
#     print(f"Bits: {n_bits}")
#     print(f"Dx: {dx_ajustada}")

#     setPeople(max, dx_ajustada, a)
    
#     people = orderPeople(people)

#     print("People")
    
#     print(people[:10])

#     people_in_bits = [toBinary(ind, n_bits, dx_ajustada, a) for ind in people]

#     toMatch(people_in_bits)

#     setChildren(matches, n_bits)

#     toMutate(childrens)

#     toMow(people_in_bits, mutations)

def main():

    a = int(input())
    b = int(input())
    dx = float(input())

    ag = GeneticAlgorithm(a, b, dx)


    res = "Y"
    while(res == "Y"):
        ag.start()
        print("Do you want continue? Y/N")
        res = input()

    
main()














