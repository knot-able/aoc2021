
lanternfish = [3,5,1,2,5,4,1,5,1,2,5,5,1,3,1,5,1,3,2,1,5,1,1,1,2,3,1,3,1,2,1,1,5,1,5,4,5,5,3,3,1,5,1,1,5,5,1,3,5,5,3,2,2,4,1,5,3,4,2,5,4,1,2,2,5,1,1,2,4,4,1,3,1,3,1,1,2,2,1,1,5,1,1,4,4,5,5,1,2,1,4,1,1,4,4,3,4,2,2,3,3,2,1,3,3,2,1,1,1,2,1,4,2,2,1,5,5,3,4,5,5,2,5,2,2,5,3,3,1,2,4,2,1,5,1,1,2,3,5,5,1,1,5,5,1,4,5,3,5,2,3,2,4,3,1,4,2,5,1,3,2,1,1,3,4,2,1,1,1,1,2,1,4,3,1,3,1,2,4,1,2,4,3,2,3,5,5,3,3,1,2,3,4,5,2,4,5,1,1,1,4,5,3,5,3,5,1,1,5,1,5,3,1,2,3,4,1,1,4,1,2,4,1,5,4,1,5,4,2,1,5,2,1,3,5,5,4,5,5,1,1,4,1,2,3,5,3,3,1,1,1,4,3,1,1,4,1,5,3,5,1,4,2,5,1,1,4,4,4,2,5,1,2,5,2,1,3,1,5,1,2,1,1,5,2,4,2,1,3,5,5,4,1,1,1,5,5,2,1,1]
lanternfish_test = [3,4,3,1,2]

# def part1(lanternfish):
#     lanternfish_start = lanternfish.copy()
#     lanternfish_end = lanternfish.copy()
#     turn = 0

#     while turn < 80:
#         for i, fish in enumerate(lanternfish_start):
#             lanternfish_end[i] -= 1
#             if lanternfish_end[i] < 0:
#                 lanternfish_end[i] = 6
#                 lanternfish_end.append(8)
#         turn += 1
#         lanternfish_start = lanternfish_end.copy()

#     number_of_fish = len(lanternfish_end)
#     return number_of_fish


# fish = [data.count(i) for i in range(9)]
# for i in range(256):
#     num = fish.pop(0)
#     fish[6] += num
#     fish.append(num)
#     assert len(fish) == 9
# print(sum(fish))

def simulate_fish(days, lanternfish):
    
    blank = {k:0 for k in range(9)}
    
    initial_state = blank.copy()
    for fish in lanternfish:
        initial_state[fish] += 1

    for day in range(days):
        end_state = blank.copy()
        for k, v in initial_state.items():
            if k != 0:
                end_state[k - 1] += v
            elif k == 0:
                end_state[8] += v
                end_state[6] += v
        initial_state = end_state.copy()

    total_fish = sum(initial_state.values())

    return total_fish
    

if __name__ == "__main__":
    print(f'Ans 1: {simulate_fish(80,lanternfish)}')
    print(f'Ans 2: {simulate_fish(256,lanternfish)}')
    # print([lanternfish_test.count(i) for i in range(9)])

