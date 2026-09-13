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