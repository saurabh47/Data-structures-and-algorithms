
# Problem: Your friend is working as a camp counselor, and he is in charge of organizing activities for a set of junior-high-school-age
# campers. One of his plans is the following mini-triathlon exercise: each contestant must swim 20 laps of a pool, then bike 10
# miles, then run 3 miles. The plan is to send the contestants out in a staggered fashion, via the following rule: the contestants
# must use the pool one at a time. In other words, first one contestant swims the 20 laps, gets out, and starts biking. As soon as
# this first person is out of the pool, a second contestant begins swimming the 20 laps; as soon as he or she is out and starts
# biking, a third contestant begins swimming . . . and so on.)
#
#Each contestant has a projected swimming time (the expected time it will take him or her to complete the 20 laps), a projected
# biking time (the expected time it will take him or her to complete the 10 miles of bicycling), and a projected running time (the
# time it will take him or her to complete the 3 miles of running). Your friend wants to decide on a schedule for the triathalon: an
# order in which to sequence the starts of the contestants. Let’s say that the completion time of a schedule is the earliest time at
# which all contestants will be finished with all three legs of the triathlon, assuming they each spend exactly their projected
# swimming, biking, and running times on the three parts. (Again, note that participants can bike and run simultaneously, but at
# most one person can be in the pool at any time.) What’s the best order for sending people out, if one wants the whole
# competition to be over as early as possible? More precisely, give an efficient algorithm that produces a schedule whose
# completion time is as small as possible.
#
# Solution: The solution is to sort the contestants by nonSwimTime (bike + run) in descending order. 
#

class Contestant:
    def __init__(self, name, swim, cycle, run):
        self.name = name
        self.swim = swim
        self.cycle = cycle
        self.run = run

    def total_time(self):
        return self.swim + self.cycle + self.run

    def nonSwimTime(self):
        return self.cycle + self.run

class Competition:
    def total_time(self, contestants):
        total = 0
        delta = 0
        for i in range(len(contestants)):
            total = max(delta+contestants[i].total_time(), total)
            delta = delta + contestants[i].swim
        return total

    def print_schedule(self, contestants):
        for contestant in contestants:
            print("Contestant: ", contestant.name, " Swim: ", contestant.swim, " Cycle: ", contestant.cycle, " Run: ", contestant.run)

    def optimal_schedule(self, contestants):
        # sort by nonSwimTime
        contestants.sort(key=lambda x: x.nonSwimTime(), reverse=True)
        self.print_schedule(contestants)
        total_time = self.total_time(contestants)
        print('Total time of competition: ', total_time)


if __name__ == '__main__':
    # # Create a list of Contestants
    contestants = []
    competition = Competition()

    contestants.append(Contestant('B', 30, 60, 10))
    contestants.append(Contestant('C', 40, 40, 20))
    contestants.append(Contestant('A', 20, 20, 30))
    contestants.append(Contestant('D', 10, 20, 40))
    competition1 = Competition()
    competition1.optimal_schedule(contestants)
    contestants = []
    contestants.append(Contestant('B', 30, 50, 60))
    contestants.append(Contestant('D', 20, 40, 35))
    contestants.append(Contestant('C', 10, 40, 45))
    contestants.append(Contestant('A', 20, 30, 50))
    competition.optimal_schedule(contestants)
    contestants = []
    contestants.append(Contestant('C', 10, 40, 45))
    contestants.append(Contestant('B', 30, 50, 60))
    contestants.append(Contestant('A', 20, 40, 10))
    contestants.append(Contestant('D', 20, 30, 50))
    # Create a Competition
    competition.optimal_schedule(contestants)

# Output:
# mahesh@Maheshs-MacBook-Air-M1 algorithms % python3 comp-scheduling.py
# Contestant:  B  Swim:  30  Cycle:  60  Run:  10
# Contestant:  C  Swim:  40  Cycle:  40  Run:  20
# Contestant:  D  Swim:  10  Cycle:  20  Run:  40
# Contestant:  A  Swim:  20  Cycle:  20  Run:  30
# Total time of competition:  150
# Contestant:  B  Swim:  30  Cycle:  50  Run:  60
# Contestant:  C  Swim:  10  Cycle:  40  Run:  45
# Contestant:  A  Swim:  20  Cycle:  30  Run:  50
# Contestant:  D  Swim:  20  Cycle:  40  Run:  35
# Total time of competition:  155
# Contestant:  B  Swim:  30  Cycle:  50  Run:  60
# Contestant:  C  Swim:  10  Cycle:  40  Run:  45
# Contestant:  D  Swim:  20  Cycle:  30  Run:  50
# Contestant:  A  Swim:  20  Cycle:  40  Run:  10
# Total time of competition:  140
# mahesh@Maheshs-MacBook-Air-M1 algorithms %