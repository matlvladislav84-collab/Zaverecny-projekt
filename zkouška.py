class KomoraSvacina:
    def __init__(self):
        self.vahy = []
        self.objemy = []
        # zadat limity přímo sem mě nenapadlo :)
        self.limitVahy = 0.5
        self.limitObjemu = 1.0

    def pridani_svacina(self, objem: float, vaha: float) -> bool:
        # pokud jsem to dobře pochopil tak se bude procházet seznam a splní se podmínka limitů tak se na základě True povolí přídání sváči?
        muzu_pridat_svacinu = True

        # do proměnné hodnoty ,,vaha_v_seznamu,, mohu načítat z externího souboru typu excel? nebo musím z listu?
        # na výběr ze seznamu svacin budou cca 3 druhy, vkladat se bude pouze 1
        # potom bych to napsal pouze takto:
        svacina_vaha = 0
        for vaha_v_seznamu in self.vahy:
            svacina_vaha = vaha_v_seznamu

        # no a teď bych jenom dal podmínky jestli splním limit váhy a objemu
        if svacina_vaha <= self.limitVahy:
            print("Svačina se váhově vejde do aktovky")
        else:
            muzu_pridat_svacinu = False
            print("Svacina se vahove nevejde do aktovky")

        # objem vložených svačin bude vždy nula aktovka je prazdná, nemá žadnou sváču
        svacina_objem = 0
        for objem_v_seznamu in self.objemy:
            svacina_objem = objem_v_seznamu

        if svacina_objem <= self.limitObjemu:
            print("Svačina se objemove vejde do komory")
        else:
            muzu_pridat_svacinu = False
            print("Svačina se objemove nevejde do komory")

        if muzu_pridat_svacinu:
            # tady to na zakladě podmínek True a False buď přidá nebo nepřidá
            self.objemy.append(objem)
            self.vahy.append(vaha)

        return muzu_pridat_svacinu
