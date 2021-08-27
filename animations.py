## Increase in size by scale amount
def Increase(self, mobj, scale, time):
  self.play(mobj.scale, scale, run_time=time)
