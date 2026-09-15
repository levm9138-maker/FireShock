self.sr = int(np.mean(np.array(f["store"])))
for _ in range(len(f["store"])):
            f["store"][b][0] = f["store"][b][0]+self.sr
            f["store"][b][1] = f["store"][b][1]+self.sr
            b = b+1
        b = 0
        for _ in range(len(f["store"])):
            f["store"][b][0] = f["store"][b][0]+x
            f["store"][b][1] = f["store"][b][1]+y
            b = b+1
        b = 0
===================
=====================
==================
    @classmethod
    def namste_1(self):
        global c, cou
        c = 0
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            self.stog[c][0] = self.data["store"][c][0]+self.data["winds_min"][cou]
            self.stog[c][1] = self.data["store"][c][1]+self.data["winds_min"][cou]
            c = c+1
        c = 0
        cou = 0
    @classmethod
    def namste_2(self):
        global c, cou, b
        self.data = self.f
        self.stog = self.data["store"]
        for _ in range(len(self.data["store"])):
            cou = np.random.randint(0, len(self.data["winds_min"])-1)
            if b==2:
                b = 0
                self.stog[c][1] = self.data["store"][c][1]-self.data["winds_min"][cou]
                self.stog[c][0] = self.data["store"][c][0]-self.data["winds_min"][cou]
            c = np.random.randint(0, len(self.data["store"]))
            b = b+1
        c = 0
        b = 0
        cou = 0
    @classmethod
    def polygon_shadow_2(self):
        global st, b
        for _ in range(len(self.stog)):
            if self.stog[b][0]<self.numb['X']:
                st.append(self.stog[b])
            b += 1
        pygame.draw.polygon(self.sc, self.data["shadow"], st, width=0)
        st = []
        b = 0
