#full_data_alchemy/polos.py

class Polo:
    def __int__(self, size:str, color:str):
        self.size = size
        self.color = color
        
    def wash(self):
        print(f"washing the")





if __name__ == '__main__':


    polo = Polo(size="L", color="Blue")
    print(polo.size, polo.color)
    polo.wash()
    
    
    polo2 = Polo(size="S", color="Green")
    print(polo.size, polo.color)
    polo.wash()