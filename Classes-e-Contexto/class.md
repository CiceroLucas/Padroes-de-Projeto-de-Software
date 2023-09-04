# Classes

- ***Atributo x Método:***
    - ***Atributo:***

        Um atributo de uma classe é basicamente uma variável de uma classe.
        ```python3
        class Personagem:
            mana = 200
        ```
    - ***Método:***

        Um método de uma classe é basicamente uma função de uma classe.
        ```python3
        class Personagem:
            def andar(self) -> None:
                pass
        ```

- ***"self":***

    O self é usado em classes para indicar que está referenciado alguma coisa do próprio objeto (sejam eles atributos ou métodos) - na verdade, o self é o próprio objeto em si.
    ```python3
    class Personagem:
        def __init__(self, name: str) -> None:
            self.name = name

        def get_name(self) -> str:
            return self.name
    ```

- ***Métodos especias:***

    - ***\_\_init__:***
 
        É um método chamado toda vez q a classe é instanciada.

        ```python3
            class Personagem:
                def __init__(self, name: str) -> None:
                # método construtor: ele irá iniciar toda vez q a classe for chamada.
                self.name = name

         ```


    - ***\_\_str__:***
 
        Usado para retornar uma representação de string de um objeto.
         - sem o método \_\_str__:
         
              ```python3
              class Personagem:
                  pass
              ```
            
        
        - com o método \_\_str__:
            ```python3
            class Personagem:
                def __str__(self) -> str:
                    return f"This is a class"
            ```
            

- ***Instanciando uma classe:***

    Para instanciarmos uma classe, basta fazermos como qual uma variável.
    ```python3
    class Personagem:
        def __init__(self, name: str) -> None:
            self.name = name

        def print_name(self) -> str:
            print(self.name)

    ```
   
