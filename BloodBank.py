class bloodbank:
    def __init__(self,id,name,age,bloodgrp,contact,date,expdate,unit):
        self.id=id
        self.name=name
        self.age=age
        self.bloodgrp=bloodgrp
        self.contact=contact
        self.date=date
        self.expdate=expdate
        self.unit=unit
        
    def __str__(self):
        return str(self.id)+","+self.name+","+str(self.age)+","+self.bloodgrp+","+str(self.contact)+","+str(self.date)+","+str(self.expdate)+","+str(self.unit)+"\n"

class bloodbag(bloodbank):
    def __init__(self, id, bloodgrp, date, expdate, quantity):
        super().__init__(id, None, None, bloodgrp, None, date, expdate, None)
        self.quantity = quantity

    def __str__(self):
        return str(self.id)+","+self.bloodgrp+","+str(self.date)+","+str(self.expdate)+"," +str(self.quantity) + "\n"
  

   