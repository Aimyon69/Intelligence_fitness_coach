import numpy as np
class Squatcounter():
    def __init__(self,angle):
        self.pre_state=0 if angle<90 else 1
        self.angle=angle
        self.valid=False
        self.count=0
    def update_angle(self,com_poi,poi1,poi2):
        '''
        angle 的 Docstring
        
        :param com_poi: 输入numpy数组[x,y],公共点坐标
        :param poi1: 输入numpy数组[x,y],p1点坐标
        :param poi2: 输入numpy数组[x,y],p2点坐标
        '''
        v1=poi1-com_poi
        v2=poi2-com_poi
        ang=(np.dot(v1,v2))/(np.linalg.norm(v1)*np.linalg.norm(v2))
        self.angle=np.arccos(ang)*180/np.pi
        return np.arccos(ang)*180/np.pi
    def state_machine(self):
        if self.angle>160:
            current_state=1
        elif self.angle<80:
            current_state=0
        else:
            return
        if self.pre_state==1 and current_state==0:
            self.valid=True
            self.pre_state=current_state
            return
        if self.valid and self.pre_state==0 and current_state==1:
            self.count+=1
            self.valid=False
        self.pre_state=current_state
        return

        
    


