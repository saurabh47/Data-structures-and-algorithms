class ProposeRejectAlgorithm:

    def __init__(self):
        self.givenWomensPreference = {
        "Amy": ["Zeus", "Victor", "Wyatt", "Yancey", "Xavier"],
        "Bertha": ["Xavier", "Wyatt", "Yancey", "Victor", "Zeus"],
        "Clare": ["Wyatt", "Xavier", "Yancey", "Zeus", "Victor"],
        "Diane": ["Victor", "Zeus","Yancey", "Xavier", "Wyatt"],
        "Erika": ["Yancey","Wyatt", "Zeus", "Xavier", "Victor"]
        }
        self. givenMensPreference = {
        "Victor": ["Bertha", "Amy", "Diane", "Erika", "Clare"],
        "Wyatt": ["Diane", "Bertha", "Amy", "Clare", "Erika"],
        "Xavier": ["Bertha", "Erika", "Clare", "Diane", "Amy"],
        "Yancey": ["Amy", "Diane", "Clare","Bertha", "Erika"],
        "Zeus": ["Bertha", "Diane","Amy", "Erika", "Clare"]
        }
        self.initialize()

    def initialize(self):
        self.engaged = {}
        self.mensPreference = self.givenMensPreference
        self.womensPreference = self.givenWomensPreference
        self.freeMen = ["Victor", "Wyatt", "Xavier", "Yancey", "Zeus"]
        self.freeWomen = ["Amy", "Bertha", "Clare", "Diane", "Erika"]

    # Men Proposing Women
    def stableMatching(self):
        while len(self.freeMen) > 0:
            m = self.freeMen[0]
            w = self.mensPreference[m][0]
            if w not in self.engaged:
                self.engaged[w] = m
                # print(w, "matched to", m)
                self.freeMen.remove(m)
            else:
                mPrime = self.engaged[w]
                if self.womensPreference[w].index(m) < self.womensPreference[w].index(mPrime): 
                    self.engaged[w] = m
                    self.freeMen.remove(m)
                    self.freeMen.append(mPrime)
                else:
                    self.mensPreference[m].remove(w)
        return self.engaged

    def reverseMenPreference(self):
        # reverse the mens preference
        self.mensPreference = {
        "Zeus": ["Bertha", "Diane","Amy", "Erika", "Clare"],
        "Yancey": ["Amy", "Diane", "Clare","Bertha", "Erika"],
        "Xavier": ["Bertha", "Erika", "Clare", "Diane", "Amy"],
        "Wyatt": ["Diane", "Bertha", "Amy", "Clare", "Erika"],
        "Victor": ["Bertha", "Amy", "Diane", "Erika", "Clare"],
        }
        self.engaged = {}
        self.freeMen = ["Zeus", "Yancey", "Xavier", "Wyatt", "Victor"]
        return self.stableMatching()

    def womenProposingMen(self):
        while(len(self.freeWomen)>0):
            w = self.freeWomen[0]
            m = self.womensPreference[w][0]
            if m not in self.engaged:
                self.engaged[m] = w
                self.freeWomen.remove(w)
            else:
                wPrime = self.engaged[m]
                if self.mensPreference[m].index(w) < self.mensPreference[m].index(wPrime):
                    self.engaged[m] = w
                    self.freeWomen.remove(w)
                    self.freeWomen.append(wPrime)
                else:
                    self.womensPreference[w].remove(m)
        return self.engaged


if __name__ == "__main__":
    algorithm = ProposeRejectAlgorithm()
    print(algorithm.stableMatching())
    print(algorithm.reverseMenPreference())
    algorithm.initialize()
    print(algorithm.womenProposingMen())

# Output:
# {'Bertha': 'Xavier', 'Diane': 'Zeus', 'Amy': 'Victor', 'Clare': 'Wyatt', 'Erika': 'Yancey'}
# {'Bertha': 'Xavier', 'Amy': 'Victor', 'Diane': 'Zeus', 'Clare': 'Wyatt', 'Erika': 'Yancey'}
# {'Zeus': 'Amy', 'Xavier': 'Bertha', 'Wyatt': 'Clare', 'Victor': 'Diane', 'Yancey': 'Erika'}