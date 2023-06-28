# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 13:48:41 2022

@author: Sehan
"""



class Snowboard:
    
    #attributes like quartz fiber flexibility
    
    quartz_fiber=[0,0,0]
    fiberglass_e_bi=[0,0,0]
    fiberglass_e_tri=[0,0,0]
    
    
    #default purpose (style, sidecut profile) (camber) (board ratio)
            #beginner (tt, radial) (rocker)
            #tricks (tt, radial) (rocker)
            #intermedieate_all_mountain (td, directional radial) (hybrid_rocker) 
            #advanced_all_mountain (td, dual sidecut) (camber)
            #powder (d, progressive sidecut) (setback camber)
            
            
    #board ratio = [[nose%, contact  length%, tail%], [nosewidth:, center width:, tail width:]] 
        
    def __init__(self, purpose: str, board_length: int, settings='default',board_width=0.0, board_ratio=[[0,0,0],[0,0,0]]):
         
        if settings=='default' and board_width!=0 or board_ratio!=[[0,0,0][0,0,0]]:
            print('settings are set to default, user provided board_width and/or board_ratio will nto be taken into consideration')
        
        #run validations to receive arguments

        assert purpose=='beginner' or 'tricks' or 'powder' or 'intermedieate_all' or 'advanced_all', "purpose can only be beginner, tricks, powder, intermedeate_all, advanced_all"
            
        assert board_length>=140, "board length is not greater than 140cm"
        
        assert settings=='default' or 'manual'
        
        if board_ratio!=[[0,0,0],[0,0,0]]:
            assert board_ratio[0][0]+board_ratio[0][1]+board_ratio[0][2]==1, "nose length, tail length and contact length percentages should add up to 1"
            
        
        
        if board_width!=0:
            assert board_width>=0, 'board width cant be  less than 0cm'
            
        
        
        #assign to self object
        self.__purpose = purpose
        self.board_ratio = board_ratio
        self.__board_length = board_length
        self.board_width=board_width
        self.settings=settings
        
        # execute actions
        Snowboard.all.append(self)
        
    @property #create read only attributes
    def purpose(self):
        return self.__purpose
    
    @property
    def board_length(self):
        return self.__board_length
    
    
    def sidecut_radius(self, sidecut_profile='default'):
        
        if sidecut_profile!='default' or 'radial' or 'directional_radial' or 'progressive' or 'directional_progressive' or 'dual' or 'directional_dual':
            assert sidecut_profile == 'default' or 'radial' or 'directional_radial' or 'progressive' or 'directional_progressive' or 'dual' or 'directional_dual', 'sidecut can only be radial, progressive or dual with directiopnal options'
        
        centre_width = self.board_width/2
        contact_length= self.board_length * self.board_ratio[0][1]
        width_nose= (self.board_ratio[1][0] * centre_width)/self.board_ratio[1][1]
        width_tail = (self.board_ratio[1][2] * centre_width)/self.board_ratio[1][1]
        
        
        
        #default sidecut calculations using board purposes
        if self.settings=='default' :
            
            if self.__purpose == 'beginner' or 'tricks': #radial
               radius_sc = (contact_length^2 + centre_width^2 - width_nose^2)/((4*width_nose)-centre_width)
                
            elif self.__purpose == 'intermedieate_all_mountain': #directional radial
                pass
                
            elif self.__purpose == 'advanced_app_mountain': #directional dual 
                pass
            elif self.__purpiose == 'powder': #directional progressive
                pass
            
            else:
                radius_sc = "direction_shape variable incorrect"
                
                
        #overridde sidecut calculations    
        elif sidecut_profile == 'radial':
            
            radius_sc = (contact_length^2 + centre_width^2 - width_nose^2)/((4*width_nose)-centre_width)
            
        elif sidecut_profile == 'directional_radial':
            pass
            
        elif sidecut_profile == 'progressive' :
            pass
        
        elif sidecut_profile == 'directional_progressive' :
            pass
             
        elif sidecut_profile == 'dual':
            pass
        
        elif sidecut_profile == 'directional_dual':
            pass
        

            
        return radius_sc
    
   
    
    
    
    def Camber_height(self, camber_profile='default'):
        #rocker, camber, hybrid camber, setback camber
        if camber_profile!='default' or 'rocker' or 'camber' or 'hybrid camber':
            assert camber_profile== 'default' or 'rocker' or 'camber' or 'hybrid camber', "camber profile can only be rocker, camber or hybrid camber"
        
        elif camber_profile=='default':
            pass
        
        else:
            pass
        
        
        
    def nose_tail_shape(self):
        pass
    
    def Nose_tail_lift(self, height_n=0, height_t=0, settings='default', n_shape = 'radial', t_shape='radial'):
        # t is short for true, i.e. height for tail and nose is the same
        # f is short for false, i.e. height is not the same
        
        assert height_n>=0 and height_t>=0, 'error: height of nose and tail has to be greater than 0'
        assert settings == 'default' or 'override', 'error: settings can only be default or override'
        
        a=self.board_length
        
        
        #defualt settings
        if self.settings=='default':
            if self.__purpose == 'beginner' : #radial
            
               b=self.board_ratio[0][0]
               h=(a*b)*0.1 #default_ratio to be determined later
               radius_nt=((a*b)^2+h^2)/2*h
               
               return (radius_nt, radius_nt)
           
            
            elif self.__purpose == 'intermedieate_all_mountain': #directional radial
            
            #nose longer than tail,  both radial
            #height kept same for nose and tail lift
            
            
                h=(a*b)*0.1 #default_ratio to be determined later
                
                #length altered for directional model
                b=self.board_ratio[0][0]
                radius_n=((a*b)^2+h^2)/2*h
                
                b=self.board_ratio[0][2]
                radius_t=((a*b)^2+h^2)/2*h
                
                return (radius_n, radius_t)
                
            elif self.__purpose    =='tricks': # twin elliptical both
                pass
            
            
            elif self.__purpose == 'advanced_app_mountain': #directional dual 
                #elliptical nose, radial tail
                #longer nose, shorter tail
                pass
            
            elif self.__purpiose == 'powder': #directional progressive
            
                #long elliptial pointed nose , short flat radial tail
                pass
        
        #override seetings
        else:
            
            if n_shape == 'radial' and t_shape=='radial':
                #same height
                if height_n==height_t:
                    h=height_n
                    
                    #same length
                    if self.board_ratio[0][0]==self.board_ratio[0][2]:
                        b=self.board_ratio[0][0]
                        
                        radius_nt=((a*b)^2+h^2)/2*h
                        return (radius_nt, radius_nt)
                    
                    #different length
                    else :
                        
                        
                        #nose radius calc
                        b=self.board_ratio[0][0]
                        radius_n = ((a*b)^2+h^2)/2*h
                        
                        #tail radius calc
                        b=self.board_ratio[0][2]
                        radius_t =((a*b)^2+h^2)/2*h
                        
                        return (radius_n, radius_t)
                    
                #different height      
                else:
                    
                    #same length
                    if self.board_ratio[0][0]==self.board_ratio[0][2]:
                        
                        b=self.board_ratio[0][0]
                        
                        radius_n = ((a*b)^2+h^2)/2*height_n
                        
                        
                        radius_n = ((a*b)^2+h^2)/2*height_t
                        
                        return (radius_n, radius_t)
                    
                    #different length
                    else :
                        
                        b=self.board_ratio[0][0]
                        radius_n = ((a*b)^2+h^2)/2*height_n
                        
                        
                        b=self.board_ratio[0][2]
                        radius_t = ((a*b)^2+h^2)/2*height_t
                        
                        return (radius_n, radius_t)
            
            elif n_shape == 'elliptical' and t_shape=='elliptical':
                pass
            elif n_shape == 'elliptical' and t_shape=='radial':
                pass
            elif n_shape =='radial' and t_shape =='elliptical':
                pass
         
    

    
    def append_to_csv(self):
        pass
    def plot_snowboard(self):
        pass
    
    def __repr__(self):
        return f"Snowboard('{self.purpose}', '{self.board_length}','{self.camber_profile}','{self.sidecut_profile}')"



#creating board ratio array
def boardratio(nose_length, tail_length, contact_length, board_width, nose_width, tail_width):
    
    if nose_length+tail_length+contact_length!=1:
        print ('Error : nose, tail and contact length does not add up 100%')
    else:
        ratio=[[nose_length, contact_length, tail_length ],[ nose_width, board_width, tail_width]]
        return ratio

board1 = Snowboard(purpose='beginner', board_length=140)
