class A:
    def __init__(self) -> None:
        self.a = "hello world"
        self.b = [B() for _ in range(5)]
    
    def A(self):
        print("A")
        
class B:
    def __init__(self) -> None:
        self.a = "hello world from B"