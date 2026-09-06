# name: joosan tibbetts
# desc: towns made of adults and children

class Town:
    adults = 0
    children = 0
    name = ""

    def __init__(self, adults: int, children: int, name="") -> None:
        self.adults = adults
        self.children = children
        self.name = name or "Unamed town"

    def __str__(self) -> str:
        return f"{self.name}:\n\tAdults: {self.adults}\n\tChildren: {self.children}"

    def birth(self, children_to_add: int):
        if children_to_add > 0: 
            self.children += children_to_add
        print(self)

    def murder(self, seniors = None):
        if seniors is None:
            if self.adults: self.adults -= 1
            else: print("womp womp")
        elif seniors > self.adults:
            print(f"There are {self.adults} adults in this town. Cannot remove {seniors}.")
        else: 
            self.adults -= seniors
            self.__mature()
            self.children += 3

        print(self)

    def __mature(self):
        children_to_mature = int(self.children / 2)
        self.adults += children_to_mature
        self.children -= children_to_mature

    def get_adults(self):
        return self.adults

    def get_children(self):
        return self.children